# Hidden Data in Image Detection Tool
- By Devika , Rajalakshmi , Megha , Vaibhav 

A web-app made using Python (NiceGUI) to detect and extract possible hidden text in  an image .

---
## Overview

Steganography is the practice of hiding secret data inside ordinary-looking files. Images are a common carrier — by modifying the **Least Significant Bit (LSB)** of each pixel value, an attacker can embed hidden text or data with almost no visible change to the image.

This Webapp tool implements **Steganalysis** ; The forensic of detecting if an image has been tampered with to conceal hidden data.

Steganalysis is performed by using the following python libraries PIL , NumPy . 

---
## Tools

| Tools/Libraries | Version |
| ------- | :-------: |
| Pillow | >= 12.3.0 |
| Python | 3.14.0+ |
| NiceGUI | >=3.18.0 |
| Numpy | >=2.3.5|
|  |  |

|Other Built-in Python Libraries used|
| ---- |
|os|
|datetime|
|pathlib|
|tempfile|
||
---
## Project Structure

```
    Hidden Data in Image Detection Tool\
    |------samples\
    |   |______422737-german-longhaired-pointer-782498_1920.jpg
    |   |______5598375-flower-3329845_1920.png
    |   |______aleshava-dog-5357794_1920.png
    |   |______gruendercoach-cat-8540772_1920.webp
    |   |______josch13-rose-320868_1920.jpg
    |   |______terex12-cat-7182671_1920.jpg
    |
    |
    |____image_analysis.py
    |____.gitignore
    |____app.py
    |____README.md
    |____requirements.txt
    |____settings.py
```
---
## Setup

On Windows ;
1. Go to the the repository .
2. Click on Code .
3. Click on Download ZIP
``` Powershell
cd <Extracted Directory>\Hidden-Data-in-Image-Detection-Tool
pip install -r requirements.txt
python app.py
```
<!-- add a gif to show how to setup in windows -->
---
## Sample workflow
<!-- add a gif to show sample workflow -->
---
## Detection Methodology

1. **Image Preprocessing** 
The input image is loaded and converted to RGB format using Pillow.
The RGB pixel data is then converted into a NumPy array and flattened into a one-dimensional sequence of colour-channel values. 

Each value represents an 8-bit red, green, or blue channel, allowing the tool to examine the image at the bit level.

2. **** 
3. **LSB(Least Significant Bit) Extraction**
The tool examines the lower bits of each colour-channel value to search for data that may have been embedded using LSB steganography.
It tests four extraction depths, from 1 to 4 bits per channel. 
At each depth, a bitmask isolates the selected lower bits, which are then extracted in a fixed order and combined into a continuous bitstream.

The bitstream is then divided into groups of eight bits and converted into bytes. This produces a byte sequence for further examination at each tested depth.

For each candidate byte sequence, the tool examines the first 25 bytes according to the assumed header layout of the targeted steganography format.

1. **Extraction & Decoding**

For candidates whose declared lengths fit within the available data, the tool extracts the assumed header and the specified number of subsequent bytes. It then attempts to decode the extracted bytes as UTF-8 text.

If decoding is sucsessful, the result text is recorded alongside the extraction depth, byte order, flags, declared length, and IV. If decoding fails, the raw bytes can still be retained for examination. The tool records these results as candidates rather than automatically treating them as confirmed hidden messages.

2. **Report Generation**

The result can be presented when the user uploads an image and includes a downloadable report .
The report can record successful candidate extractions, invalid length interpretations, extraction parameters, and relevant raw data. Keeping rejected candidates in the report provides transparency about the tested interpretations and allows the results to be thoroughly examined later.

---
## Limitations

##### - **Metadata Analysis Limitation**

1. Metadata could be absent : Some images contain little or no metadata, so the analysis may provide limited information.

2. Metadata could be modified or removed : Image editing, format conversion, social media uploads, and many other processing operations could remove or alter metadata.

3. Metadata could be misleading :Metadata values may be inaccurate, deliberately altered, or inconsistent with the image's actual history. This tool currently cannot assume that recorded values are authentic.

4. Limited Detection of concealed Metadata : Metadata analysis might not identify every form of data appended to an image, stored in unrecognised sections, or concealed through a specialised technique .

##### - **Limited coverage of Steganalysis techniques**

Ths tool focuses on sequential extraction of lower RGB channel bits.It currently **do not** cover every method used to hide data in images, such as transform-domain techniques, adaptive embedding, or methods that distribute data across selected pixels. 

Hidden data might also remain undetected if it was embedded using a different technique.

##### - **No guarentee of complete Data extraction**

The tool extracts only the number of bytes specified by the interpreted length field. If the header is damaged, the length incorrect, or if the format uses any additional  encoding, the extracted data may be incomplete or incorrectly interpreted. 

Therefore, the tool should be treated as a Text-recovery mechanism rather than a guarantee of complete message recovery.

---
## Real - World Applications
> * Digital watermarking — embed copyright or ownership information invisibly inside images
> * Covert communication — send hidden messages through innocuous image files
> * CTF (Capture The Flag) challenges — steganography puzzles are a staple of cybersecurity competitions
> * Digital forensics education — understand how investigators detect hidden payloads
> * Privacy research — explore information hiding for academic study
> (Referenced from [MonoCalc](https://monocalc.com/tool/encode_decode/image_steganography). )
---
## Links

Sample images obtained from [pixaby](https://pixabay.com/) .
Web app implimentation inspired from [MonoCalc](https://monocalc.com/tool/encode_decode/image_steganography).

Sample Images encoded using [MonoCalc](https://monocalc.com/tool/encode_decode/image_steganography).