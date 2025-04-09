from PIL import Image, ImageChops
image_path = r'Enter the path to the image here'

try:
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    inv_img = ImageChops.invert(img)
    inv_img.show()
except Exception as e:
    print(f"An error occurred: {e}")
