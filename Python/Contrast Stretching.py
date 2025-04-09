from PIL import Image
import numpy as np

def contrast_stretching(image_path, output_path, r1, s1, r2, s2):
    img = Image.open(image_path).convert('L')  
    img_array = np.array(img)
    def stretch_contrast(pixel_value):
        if pixel_value <= r1:
            return (s1 / r1) * pixel_value
        elif r1 < pixel_value <= r2:
            return ((s2 - s1) / (r2 - r1)) * (pixel_value - r1) + s1
        else:
            return ((255 - s2) / (255 - r2)) * (pixel_value - r2) + s2
    vectorized_stretch = np.vectorize(stretch_contrast)
    stretched_img_array = vectorized_stretch(img_array).astype(np.uint8)
    stretched_img = Image.fromarray(stretched_img_array)
    stretched_img.save(output_path)
    original_and_stretched = Image.new('L', (img.width + stretched_img.width, img.height))
    original_and_stretched.paste(img, (0, 0))
    original_and_stretched.paste(stretched_img, (img.width, 0))
    combined_output_path = output_path.replace('.jpg', '_combined.jpg')
    original_and_stretched.save(combined_output_path)
    original_and_stretched.show()
r1, s1 = 30, 10 
r2, s2 = 80, 245 
image_path = 'Enter the path to the image here'
contrast_stretching(image_path, output_path, r1, s1, r2, s2)
