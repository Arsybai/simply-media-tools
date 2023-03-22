import cv2
import numpy as np
from PIL import Image
import os

def remove_background(image_path, output_path='output.png'):
    image = Image.open(image_path)
    image = image.convert('RGBA')
    pixel_data = image.load()
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            pixel = pixel_data[x, y]
            if pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200:
                pixel_data[x, y] = (0, 0, 0, 0)
    image.save(output_path, format='PNG')
   

def resize(image_path, width, height, output_path='resized_image.png'):
    with Image.open(image_path) as img:
        new_width = int(width)
        new_height = int(height)
        resized_img = img.resize((new_width, new_height))
        resized_img.save(output_path)


def profile_picture_maker(image_path, output_path='profile_picture_output.png'):
    remove_background(image_path, 'temp_ppmaker.png')
    resize('temp_ppmaker.png', 512, 512, 'temp_ppmaker.png')
    img = Image.open('temp_ppmaker.png').convert('RGBA')
    width, height = 512, 512
    background = np.zeros((height, width, 3), dtype=np.uint8)
    color = tuple(np.random.randint(256, size=3))
    background[:, :] = color
    background = Image.fromarray(background)
    background.paste(img, (0, 0), img)
    background.save(output_path)
    os.remove('temp_ppmaker.png')

def sharpen(image_path, output_path='sharpened.png'):
    img = cv2.imread(image_path)
    kernel = np.array([[-1,-1,-1], 
                    [-1, 9,-1],
                    [-1,-1,-1]])
    sharpened_img = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(output_path, sharpened_img)

def compress(image_path, compression_level:int, output_path='compressed.jpg'):
    img = Image.open(image_path)
    compression_level = compression_level
    img.save(output_path, optimize=True, quality=compression_level)