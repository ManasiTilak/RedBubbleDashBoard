from distutils import extension
import os

def navigate_images(to_clean_folder):
        images = os.listdir(to_clean_folder)
        for image_name_ext in images:
                edit_image(to_clean_folder, image_name_ext)
        print("Image Folder is Now clean. You may proceed to uploading images")

def edit_image(folder_name,image_name):

        import cv2
        from PIL import Image, ImageEnhance

        THRESHOLD_WIDTH = 3840
        THRESHOLD_HEIGHT = 3840
        EXTENSION = ['png', 'jpg']
        ext = image_name.split('.')[-1]
        print(f"Dealing with {image_name} with extension : {ext}")
        if ext in EXTENSION:
                image_full_address = folder_name + image_name
                image = cv2.imread(image_full_address)
                img_scale_up = cv2.resize(image, (0, 0), fx=2, fy=2)
                cv2.imwrite(image_full_address, img_scale_up)
                #opening new doubled img using pillow
                image = Image.open(image_full_address)
                #starting edits
                #Enhance Color
                color = ImageEnhance.Color(image)
                color_img = color.enhance(1.2)
                #Enhance Brightness
                brightness = ImageEnhance.Brightness(color_img)
                bright_img = brightness.enhance(1.1)
                #CONTRAST
                contrast = ImageEnhance.Contrast(bright_img)
                contrast_img = contrast.enhance(1.2)
                contrast_img.save(image_full_address)
                #checking edited image size
                final_image = Image.open(image_full_address)
                image_size = final_image.size
                width = image_size[0]
                height = image_size[1]
                if width <= THRESHOLD_WIDTH or height <= THRESHOLD_HEIGHT:   #Required height for art prints in redbubble
                        print(f'image {image_name} may be too small for your purposes.')
                else:
                        print(f"Image {image_name} has been edited")
