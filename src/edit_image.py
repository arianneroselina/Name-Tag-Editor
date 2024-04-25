import os
from PIL import Image, ImageDraw, ImageFont


def write_names(design_path, output_path, basket_names):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    edited_images = []
    for basket_name in basket_names:
        output_name = write_name(design_path, output_path, basket_name)
        edited_images.append(output_name)
    return edited_images


def write_name(design_path, output_path, text):
    """
    Write a text to the image in the given path.
    """
    # open image
    image = Image.open(design_path)

    # max 20 chars per line
    max_chars_per_line = 18
    text_lines = split_text(text, max_chars_per_line)

    # define text style
    font_style = "fonts/coolvetica rg.otf"
    font_color = (50, 50, 50)
    font_size = 43
    font = ImageFont.truetype(font_style, font_size)

    draw = ImageDraw.Draw(image)

    # center vertical position
    y_pos = distribute_y_pos(325, 520, text_lines, font_size)

    for i, line in enumerate(text_lines):
        # center horizontal position
        x_pos = center_x_pos(draw, image, line, font)
        # add text to image
        draw.text((x_pos, y_pos[i]), line, fill=font_color, font=font)

    # save modified image
    _, output_ext = os.path.splitext(design_path)
    output_filename = "name_tag_" + text + output_ext

    image.save(os.path.join(output_path, output_filename))
    return output_filename


def center_x_pos(draw, image, text, font):
    """
    Calculate center x position for the text to start at with the given image and font.
    """
    _, _, text_width, text_height = draw.textbbox((0, 0), text, font=font)
    image_width, image_height = image.size
    return (image_width - text_width) // 2


def distribute_y_pos(y1, y2, text_lines, font_size):
    """
    Distribute y positions for a list of text lines, ensuring they are vertically centered between y1 and y2.
    """
    y_positions = []
    num_elements = len(text_lines)
    remaining_space = y2 - y1 - (num_elements * font_size)
    additional_space = remaining_space // 2

    current_y = y1 + additional_space + font_size // 2
    for _ in range(num_elements):
        y_positions.append(current_y)
        current_y += font_size

    return y_positions


def split_text(text, max_chars):
    """
    Split text into lines with a maximum number of characters without breaking words.
    """
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_chars:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines
