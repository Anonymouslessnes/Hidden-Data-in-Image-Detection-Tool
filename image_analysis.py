from PIL import Image
from numpy import array
from matplotlib import pyplot
from os import path
from datetime import datetime

class Image_analysis:

    def __init__(self,file):
# Exracts metadata
        self.file=Image.open(file,'r')
        filedatecreated=path.getctime(file)
        filedatmodified=path.getmtime(file)
        self.filedatecreated=datetime.fromtimestamp(filedatecreated).strftime("%Y-%m-%d | %H:%M:%S")
        self.filedatmodified=datetime.fromtimestamp(filedatmodified).strftime("%Y-%m-%d | %H:%M:%S")
        self.img = Image.open(file)
        self.imgarray = array(self.img)
        self.fileformat=self.img.format
        self.filename=path.basename(file)
        self.filesize=path.getsize(file)
        self.filesize=f"{round(self.filesize/1024,2)} KB"
        self.file=Image.open(file)
        self.fileheight,self.filewidth,self.filechannel=self.imgarray.shape
        self.filemode=self.img.mode


    def lsb_analysis(self):
# Analyze the least significant bit plane .
        self.lsb_report=None
        analysis=''
        with open(r"analysis_template.txt",'r') as temp:
            report=temp.read()
            report=report.format(analysis)
            self.lsb_report=report


    def spread_spectrum(self):
# Analyze for spread-spectrum steganography
        self.ss_report=None
        analysis=''
        with open(r"analysis_template.txt",'r') as temp:
            report=temp.read()
            report=report.format(analysis)
            self.ss_report=report


    def msb_analysis(self):
# Analyze the most significant bit plane .
        self.msb_report=None
        analysis=''
        with open(r"analysis_template.txt",'r') as temp:
            report=temp.read()
            report=report.format(analysis)
            self.msb_report=report


    def bit_plane(self):
#Analyze the Bit planes of image
        self.bp_report=None
        analysis=''
        with open(r"analysis_template.txt",'r') as temp:
            report=temp.read()
            report=report.format(analysis)
            self.bp_report=report


    def report_gen(self):
# Gives a report of the analysis result
        with open('report_template.txt','r') as temp:
            report= temp.read()
            report=report.format(self.filename,
                self.fileformat,
                self.filesize,
                self.filemode,
                self.filechannel,
                self.filewidth,
                self.fileheight,
                self.filedatecreated,
                self.filedatmodified,
                self.lsb_report,
                self.msb_report,
                self.bp_report,
                self.ss_report)
            return report