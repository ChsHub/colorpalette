from PIL import Image, ImageDraw
from webcolors import rgb_to_hex


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
        # Get palette of colors in the image
        small_image = original_image.resize((80, 80))
        result = small_image.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
        result.putalpha(0)
        colors = result.getcolors(80 * 80)

        # Create background image and copy original
        width, height = original_image.size
        palette_height = int(height / palette_length_div)
        original_image.convert('RGB')
        background = original_image.crop((0, 0, width, height + palette_height))

    pal = Image.new("RGB", (width, palette_height))
    draw = ImageDraw.Draw(pal)

    swatchsize = width / num_colors
    hex_codes = []

    # making the palette
    posx = 0
    for count, color in colors:
        draw.rectangle([posx, 0, posx + swatchsize , palette_height], fill=color, width=outline_width,
                       outline=outline_color)
        hex_codes.append(rgb_to_hex(color[:3]))
        posx += swatchsize

    # Delete draw object
    del draw

    # pasting image and palette on the canvas
    box = (0, height, width, height + palette_height)
    background.paste(pal, box)

    return background, hex_codes
