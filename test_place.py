from image_analysis import Image_analysis

img=Image_analysis(r"samples\422737-german-longhaired-pointer-782498_1920.jpg")
img.lsb_analysis()
img.spread_spectrum()
img.msb_analysis()
img.bit_plane()
report=img.report_gen()
print(report)