from PIL import Image
import numpy as np
import math

def resize_width(img: Image, new_width: int):
    w, l = img.size
    return img.resize((new_width, int(l*new_width/w)))


def map_pixels(img: Image, image_func=lambda x, **kwargs: x, line=False, **kwargs):
    w, l = img.size
    pixels = img.load()
    if not line:
        return [[image_func(pixels[x, y], **kwargs) for y in range(l)] for x in range(w)]
    else:
        return [image_func([pixels[x, y] for y in range(l)], **kwargs) for x in range(w)]


def low_def(c, division=4):
    d = 256/division
    r, g, b = math.ceil(c[0]/d)*d, math.ceil(c[1]/d)*d, math.ceil(c[2]/d)*d
    if r == 0: r = 1
    if g == 0: g = 1
    if b == 0: b = 1
    return r-1, g-1, b-1


def transpose(array):
    new_array = [[] for i in range(len(array[0]))]
    for i in range(len(array)):
        for j in range(len(array[0])):
            new_array[j].append(array[i][j])
    return new_array


def separate_rgb(pixels_array):
    r_array, g_array, b_array = [], [], []
    for i in range(len(pixels_array)):
        r_line, g_line, b_line = [], [], []
        for j in range(len(pixels_array[0])):
            r, g, b = pixels_array[i][j]
            r_line.append(r)
            g_line.append(g)
            b_line.append(b)
        r_array.append(r_line)
        g_array.append(g_line)
        b_array.append(b_line)
    return r_array, g_array, b_array


def separate_rgb_zeros(pixels_array):
    r_array, g_array, b_array = [], [], []
    for i in range(len(pixels_array)):
        r_line, g_line, b_line = [], [], []
        for j in range(len(pixels_array[0])):
            r, g, b = pixels_array[i][j]
            r_line.append((r, 0,0))
            g_line.append((0, g, 0))
            b_line.append((0, 0, b))
        r_array.append(r_line)
        g_array.append(g_line)
        b_array.append(b_line)
    return r_array, g_array, b_array


def single_colour_image(img, color: int):
    for i in range(3):
        img = Image.fromarray(np.array(transpose(separate_rgb_zeros(map_pixels(img))[i]), dtype=np.uint8), mode='RGB')
        img.show()

def write_2d(file_name: str, lines):
    with open(file_name, "a") as file:
        for line in lines:
            file.writelines(" ".join(map(str, line))+"\n")


def clear_all(file_names):
    for i in file_names:
        with open(i, "w") as file:
            pass
