- [Hidden Data in Image Detection Tool](#hidden-data-in-image-detection-tool)
  - [Overview](#overview)
  - [Tech Stack](#tech-stack)
  - [Project Structure](#project-structure)
  - [Setup](#setup)
  - [Sample workflow](#sample-workflow)
  - [Detection Methodology](#detection-methodology)
  - [Limitations](#limitations)
  - [Links](#links)


# Hidden Data in Image Detection Tool
- By Devika , Rajalakshmi , Megha , Vaibhav 

A web-app made using Python (NiceGUI) to detect and extract possible hidden data in  an image .

---
## Overview
Steganography is the practice of hiding secret data inside ordinary-looking files. Images are a common carrier — by modifying the **Least Significant Bit (LSB)** of each pixel value, an attacker can embed hidden text or data with almost no visible change to the image.

This Webapp implements **Steganalysis** ; The forensic of detecting whether an image has been tampered with to conceal hidden data.

---
## Tech Stack

| Tool | Version |
| ------- | :-------: |
| Python | 3.14.0+ |
| NiceGUI | >=3.18.0 |
| Pillow | >= 12.3.0 |
| NumPy|>= 2.3.5 |
| Matplotlib | >= 3.10.8 |

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
    |----------src\
    |     |____image_analysis.py
    |     |____report_template.txt
    |
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
2. Click on Code
![]()
3. Click on Download ZIP
```
cd ...\Hidden-Data-in-Image-Detection-Tool
pip install -r requirements.txt
python app.py
```
---
## Sample workflow
---
## Detection Methodology
---
## Limitations

---
## Links
Sample images obtained from [pixaby](https://pixabay.com/) .
