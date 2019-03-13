from color.color import get_palette_image
from webcolors import hex_to_rgb
import os


def main():
    filename = input('Image file:').strip('"')
    palette_height = range(1, 11)[5]
    palette_outline_width = range(1, 41)[20]

    file_path, ext = os.path.splitext(filename)

    f, pal2, hex_codes = get_palette_image(file_path=filename,
                                           palette_length_div=palette_height,
                                           outline_width=palette_outline_width,
                                           outline_color=hex_to_rgb('#FFFFFF'),
                                           num_colors=10)
    print(hex_codes)
    f.save(file_path + '_palette' + '.jpg', quality=95, optimize=True)


if __name__ == '__main__':
    main()
