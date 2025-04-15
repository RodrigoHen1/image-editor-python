from PIL import Image, ImageEnhance, ImageFilter
import os

input_directory = './imgs'
output_directory = './editedImgs'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for current_file_name in os.listdir(input_directory):
    original_image = Image.open(f"{input_directory}/{current_file_name}")

    processed_image = original_image.filter(ImageFilter.SMOOTH).convert('L')

    brightness_factor = 1.2
    enhancer = ImageEnhance.Brightness(processed_image)
    processed_image = enhancer.enhance(brightness_factor)

    contrast_factor = 1.5
    contrast_enhancer = ImageEnhance.Contrast(processed_image)
    processed_image = contrast_enhancer.enhance(contrast_factor)

    base_name = os.path.splitext(current_file_name)[0]

    processed_image.save(f'.{output_directory}/{base_name}_edited.jpg')
