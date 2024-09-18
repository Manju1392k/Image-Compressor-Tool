from PIL import Image
import os

# Function to show in their size format like 'kb', 'mb'.
def Image_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

# Image Compressor function.
def Image_Compressor(Img_path, Output_path, Scale_factor=0.5, Quality=80):

    try:
        # Opening the image file.
        with Image.open(Img_path) as img:

            # Showing current Image size.
            Original_image_size = os.path.getsize(Img_path)
            print(f"Original Image size: {Image_size_format(Original_image_size)}")
            
            # Calculating the Image dimensions
            New_Width = int(img.width * Scale_factor)
            New_Height = int(img.height * Scale_factor)
            
            # Resizing the image to reduce the size of image.
            img = img.resize((New_Width, New_Height), Image.LANCZOS)
            
            # Saving the compressed image in jpg format.
            img.save(Output_path, "JPEG", Quality=Quality, optimize=True, progressive=True)
            
            # Showing the compressed image size.
            Compressed_size = os.path.getsize(Output_path)
            print(f"Compressed Image size: {Image_size_format(Compressed_size)}")

            print('Image compressed successfully')

    except:
        print('Something went wrong')

# Calling the function with passing parameters.
Image_Compressor("Car3.jpg", "3-Compressed-Image.jpg", Scale_factor=0.5)
