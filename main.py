from PIL import Image
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

rgb_sep = separate_rgb(map_pixels(img_resized))
rgb_text_list = "r_text.txt", "g_text.txt", "b_text.txt"
for i in range(3):
    write_2d(rgb_text_list[i], rgb_sep[i])

print(len(("80 98 106 108 114 120 124 128 137 141 143 149 151 154 148 114 120 125 124 120 94 91 96 92 89 84 83 88 105 103 103 100 97 104 102 129 147 134 134 99 92 86 93 92 78 99 102 74 85 87 88 94 91 80 63 61 64 60 56 63 64 76 87 84 74 59 55 53 47 39 37 35 28 26").split()))
# clear_all(rgb_text_list)