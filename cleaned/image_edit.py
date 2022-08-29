def edit_image(folder_name,image_name):

        import cv2
        from PIL import Image, ImageEnhance

        THRESHOLD_WIDTH = 3840
        THRESHOLD_HEIGHT = 3840
        print(f"Editing {image_name}")
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
