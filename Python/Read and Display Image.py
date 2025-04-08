from PIL import Image
import os
image_path = input("Enter the path to the image: ").strip('"')

if not os.path.isfile(image_path):
    print(f"File not found: {image_path}")
else:
    try:
        image = Image.open(image_path)
        image.show()
    except Exception as e:
        print(f"Error opening image: {e}")
