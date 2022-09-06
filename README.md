RedBubble Dashboard
--

This combines all the work needed to automate images to Redbubble.


## Components

- Scrape all Image Links from Raw Pixel Website
- Download Images from RawPixel
- Clean the Image Folder : Increase Image size and add brightness, contrast, sharpness
- Finally upload the Images to Redbubble Profile

## Modules Used :
- PyQt5 : For the GUI
- Sqlite : To store and manipulate redbubble profile info.
- BeautifulSoup and Requests : To scrape RawPixels.
- Selenium : To automate image download and upload.
- OpenCV and Pillow to edit and clean images.

