import src.image_analysis as img #Image Analysis and report generation
from nicegui import ui ,app, events  #Webapp module
from pathlib import Path
from tempfile import NamedTemporaryFile
from io import BytesIO

# Add static files for sample images.
app.add_static_files('/samples', 'samples')  
# sample image filenames
sample_images = (
    ('sample 1','josch13-rose-320868_1920.jpg'),
    ('sample 2',"422737-german-longhaired-pointer-782498_1920.jpg"),
    ('sample 3','5598375-flower-3329845_1920.png'),
    ('sample 4',"aleshava-dog-5357794_1920.png"),
    ('sample 5','terex12-cat-7182671_1920.jpg'),
    ('sample 6','gruendercoach-cat-8540772_1920.webp')
    ) 

uploaded_path = None
selected_image = None
rep= '##### No report generated'

# pages
@ui.page('/')
def index():
    global theme_toggle,upload,clicked
    with ui.column().classes('w-full items-center'):
        ui.label("Hidden Data in Image Detection").classes("text-3xl font-bold")
        #Theme toggle
        change_theme_button()
        with ui.card(align_items='center').classes("items-center w-full max-w-md mt-8"):
            # File upload
            upload=ui.upload(auto_upload=True , max_files=1 ,max_file_size=1_000_000 , on_upload=handle_upload).props('accept="image/*"')    
            with ui.column().classes("items-center"):
                submit=ui.button(text='Submit',on_click=navto_analysis)
                with ui.dialog() as dialog,ui.card():
                    ui.label("Sample Images").classes("text-lg")
                    with ui.grid(columns=3,rows=2):
                        for label,path in sample_images:
                            with ui.column().classes("items-center"):
                                ui.image('/samples/'+Path(path).name).classes('w-32 h-32 object-cover')
                                ui.button(label,on_click=lambda path=path : select_sample(path))
                ui.button("Choose a Sample Image",on_click=dialog.open).classes('p-2')
                def select_sample(path):
                    global selected_image
                    selected_image = path
                    dialog.close()
                    navto_analysis()
    # footer
    add_footer()

# Analysis Page
@ui.page('/analysis',title="Image Analysis Report")
def analysis_page():
    with ui.column().classes('w-full items-center'):
        ui.html("<h2>Image Analysis</h2>").classes("text-3xl items-center font-bold")
        #Theme toggle
        change_theme_button()
        with ui.card(align_items='center').classes('w-full mt-25'):
            ui.markdown(rep)
    ui.link('Go back <-',index).classes("absolute right-4 bottom-4")
        # footer
    add_footer()

#---------------------------- Functions -------------------------------

#upload function for sample
def navto_analysis():
    global rep
    print("Submit clicked", "selected:", selected_image, "uploaded:", uploaded_path)
    if selected_image:
        file_path = Path("samples") / Path(selected_image).name
    elif uploaded_path:
        file_path = Path(uploaded_path)
    else:
        ui.notify("Please upload an image or choose a sample.", color="negative")
        return
    try:
        analyzer = img.Image_analysis(str(file_path))
        analyzer.lsb_analysis()
        can1= analyzer.extract_lsb()
        can2= analyzer.extract_lsb(channel=1)
        ca3n= analyzer.extract_lsb(channel=2)
        rep = analyzer.report_gen()
        ui.navigate.to("/analysis")
    except Exception as exc:
        print("Analysis failed:", repr(exc))
        ui.notify(f"Analysis failed: {exc}", color="negative")

# upload function for user
async def handle_upload(e: events.UploadEventArguments):
    global uploaded_path, selected_image
    try:
        uploaded_file = e.file
        name = uploaded_file.name
        content = uploaded_file._data  # bytes held by NiceGUI's SmallFileUpload
        suffix = Path(name).suffix.lower() or ".img"
        with NamedTemporaryFile(delete=False, suffix=suffix) as f:
            f.write(content)
            uploaded_path = f.name
        selected_image = None
        ui.notify(f"Uploaded {name}")
    except Exception as exc:
        print("Upload failed:", repr(exc))
        ui.notify(f"Upload failed: {exc}", color="negative")


#Footer
def add_footer():
    with ui.footer():
        ui.label("© 2026 ")
        ui.link("Github repository link", "https://github.com/Anonymouselss")

# Theme changing button inserting function
def change_theme_button():
    clicked=True
    def change_theme():
        nonlocal clicked
        if clicked:
            ui.dark_mode().enable()
            clicked=False
            theme_toggle.text="Dark"
        else:
            ui.dark_mode().disable()
            theme_toggle.text="Light"
            clicked=True
    theme_toggle=ui.button(text="Light",on_click=change_theme).classes("absolute right-4 top-4")


ui.run(title="Hidden Data in Image Detection",favicon='https://www.svgrepo.com/show/507920/arrow-down-left-square.svg')