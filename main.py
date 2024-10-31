from PIL import Image
import numpy as np
from image_edit import *
img = Image.open("mona_lisa.jpg")

# Display the image
img.show()

print("Image size:", img.size)  # (width, height)
print("Image format:", img.format)  # e.g., JPEG, PNG
print("Image mode:", img.mode)  # e.g., RGB, L (grayscale)


def resize_width(img, new_width):
    w, l = img.size
    return img.resize((new_width, int(l*new_width/w)))


img_resized = resize_width(img, 50)


img_resized.show()
print("Image size:", img_resized.size)  # (width, height)
print("Image format:", img_resized.format)  # e.g., JPEG, PNG
print("Image mode:", img_resized.mode)  # e.g., RGB, L (grayscale)

rgb_sep = separate_rgb(transpose(map_pixels(img_resized)))
rgb_text_list = "r_text.txt", "g_text.txt", "b_text.txt"
clear_all(rgb_text_list)
# for i in range(3):
#     write_2d(rgb_text_list[i], rgb_sep[i])

for i in range(1):
    new_img = Image.fromarray(np.array(transpose(separate_rgb_zeros(map_pixels(img))[i]), dtype=np.uint8), mode='RGB')
    new_img.show()

for i in range(1):
    new_img = Image.fromarray(np.array(transpose(separate_rgb_zeros(map_pixels(img, low_def))[i]), dtype=np.uint8), mode='RGB')
    new_img.show()