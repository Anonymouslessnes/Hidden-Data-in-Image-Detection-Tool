from PIL import Image , ExifTags
from numpy import array,newaxis,uint8,asarray,packbits
from os import path
from datetime import datetime
from pathlib import Path

class Image_analysis:
    def __init__(self,file):
        # Open image once
        with Image.open(file) as img:
            self.img = img.copy()
            self.fileformat = img.format
            self.filemode = img.mode
            self.filewidth, self.fileheight = img.size
            self.filechannel = (
                len(img.getbands())
            )
            # Extract more metadata
            self.meta=""
            for key,value in img.info.items():
                if isinstance(value,bytes):
                    value=f'\n* <binary data: {len(value)} bytes>'
                    self.meta+=f"\n* {key}   : {value}"
                else:
                    self.meta+=f'\n* {key}    : {value}'
            exifdata=img.getexif()
            if exifdata:
                self.meta+="\n<p style='text-align:center;font-size:medium;'>EXIF image info</p>\n"
                for tag,val in exifdata.items():
                    tagname=ExifTags.TAGS.get(tag,str(tag))
                    self.meta+=f'\n* {tagname}    :{val}\n'

        self.filename = path.basename(file)
        self.filedatecreated = datetime.fromtimestamp(
            path.getctime(file)
        ).strftime("%Y-%m-%d | %H:%M:%S")
        self.filemodified = datetime.fromtimestamp(
            path.getmtime(file)
        ).strftime("%Y-%m-%d | %H:%M:%S")
        self.filesize = path.getsize(file)
        self.filesize = f"{self.filesize / 1024:.2f} KB"
        # Image array
        self.imgarray = array(self.img)


    def lsb_analysis(self):
        pixels=self.imgarray
        if pixels.ndim==2:
            pixels=pixels[...,newaxis]
        channel_names={
            1: ['Gray'],
            2: ['Gray','Alpha'],
            3: ["Red","Green","Blue"],
            4: ["Red","Green","Blue",'Alpha']
        }.get(pixels.shape[-1], [f"Channel {i}" for i in range(pixels.shape[-1])])
        lines=[]
        for i,name in enumerate(channel_names):
            values=pixels[...,i].astype(uint8)
            bits= values & 1
            ones =int(bits.sum())
            total =bits.size
            proportion = ones/total if total else 0.0
            lines.append(
                f"\n* {name}: LSB 0s={total - ones}, LSB 1s={ones}, 1-proportion={proportion:.4f}"
            )
        analysis=''.join(lines)
    #Report
        self.lsb_report=f"\n<p style='text-align:center;font-size:x-large;'>LSB Analysis</p>\n {analysis}"

    def extract_lsb(self, channel=0):
        if channel not in (0, 1, 2):
            raise ValueError("channel must be 0 (red), 1 (green), or 2 (blue)")
        # Convert palette, grayscale, or other modes to a consistent RGB array.
        pixels = asarray(self.img.convert("RGB"), dtype=uint8)
        # One bit per pixel, in row-major order; pack groups of 8 into bytes.
        bits = (pixels[:, :, channel] & 1).reshape(-1)
        data = packbits(bits, bitorder="big").tobytes()
        data=data
        return data
    def report_gen(self):
# Gives a report of the analysis result
        with open('src/report_template.txt','r') as temp:
            report= temp.read()
            report=report.format(self.filename,
                self.fileformat,
                self.filesize,
                self.filemode,
                self.filechannel,
                self.filewidth,
                self.fileheight,
                self.filedatecreated,
                self.filemodified)
            report+=self.meta+self.lsb_report
            return report