from PIL import Image, ImageDraw
from webcolors import rgb_to_hex


def _get_colors(original_image, num_colors):
    result = original_image.resize((80, 80))
    result = result.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
    result = result.convert('RGB')
    return result.getcolors(80 * 80)


def get_palette_image(file_path, outline_width, palette_length_div, outline_color, num_colors=20):
    """
    Generate image with attached color palette
    :param file_path: FIle path of image image
    :param outline_width:
    :param palette_length_div:
    :param outline_color:
    :param num_colors:
    :return:
    """
    with Image.open(file_path) as original_image:
        original_image = original_image.convert('RGB')
        # Get palette of colors in the image
        colors = _get_colors(original_image, num_colors)

        # Create background image and copy original
        width, height = original_image.size
        palette_height = int(height / palette_length_div)

        background = original_image.crop((0, 0, width, height + palette_height))

    pal = Image.new("RGB", (width, palette_height))
    draw = ImageDraw.Draw(pal)

    color_width = width / num_colors
    hex_codes = []

    # making the palette
    for posx, (count, color) in enumerate(colors):
        draw.rectangle([posx * color_width, 0, posx * color_width + color_width, palette_height],
                       fill=color, width=outline_width, outline=outline_color)
        hex_codes.append(rgb_to_hex(color[:3]))

    # Delete draw object
    del draw

    # pasting image and palette on the canvas
    box = (0, height, width, height + palette_height)
    background.paste(pal, box)

    return background, hex_codes
