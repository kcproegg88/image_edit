from PIL import Image


def resize_width(img: Image, new_width: int):
    w, l = img.size
    return img.resize((new_width, int(l*new_width/w)))


def map_pixels(img: Image, image_func=lambda x:x, line=False):
    w, l = img.size
    pixels = img.load()
    if not line:
        return [[image_func(pixels[x, y]) for y in range(l)] for x in range(w)]
    else:
        return [image_func([pixels[x, y] for y in range(l)]) for x in range(w)]


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


def write_2d(file_name: str, lines):
    with open(file_name, "a") as file:
        for line in lines:
            file.writelines(" ".join(map(str, line))+"\n")


def clear_all(file_names):
    for i in file_names:
        with open(i, "w") as file:
            pass
