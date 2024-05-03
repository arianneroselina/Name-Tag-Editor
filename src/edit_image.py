import os
from PIL import Image, ImageDraw, ImageFont

from src.constants import part_of_dict


def write_names(design_path, output_path, names, key):
    print("Writing names and part ofs of " + part_of_dict[key] + " to the design...")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    edited_images = []
    empty_text = 0
    for name in names:
        # TODO: remove this if bulu tangkis ganda campuran is full
        if name == "":
            name = f"empty_{empty_text}"
            empty_text = empty_text + 1
        output_name = write_name_and_part_of(design_path, output_path, name, key)
        edited_images.append(output_name)
    return edited_images


def write_name_and_part_of(design_path, output_path, text, key):
    """
    Write a text to the image in the given path.
    """
    # open image
    image = Image.open(design_path)
    draw = ImageDraw.Draw(image)

    # write name
    write_name(image, draw, text)
    write_part_of(image, draw, key)

    # draw border
    draw_border(image, draw)

    # save modified image
    _, output_ext = os.path.splitext(design_path)
    output_filename = "name_tag_" + text + output_ext

    image.save(os.path.join(output_path, output_filename))
    return output_filename


def write_name(image, draw, name):
    # TODO: remove this if bulu tangkis ganda campuran is full
    if "empty" in name:
        return

    text_lines = split_text(name)

    # define text style
    font_style = "fonts/coolvetica rg.otf"
    font_color = (50, 50, 50)
    font_size = 80
    font = ImageFont.truetype(font_style, font_size)

    # center vertical position
    y_pos = distribute_y_pos(750, 900, text_lines, font_size)

    for i, line in enumerate(text_lines):
        # center horizontal position
        x_pos = center_x_pos(image, draw, line, font)
        # add text to image
        draw.text((x_pos, y_pos[i]), line, fill=font_color, font=font)


def write_part_of(image, draw, key):
    part_of_text = part_of_dict[key]

    font_style = "fonts/coolvetica rg.otf"
    font_color = (50, 50, 50)
    font_size = 30
    font = ImageFont.truetype(font_style, font_size)

    line = "PART OF: " + part_of_text
    x_pos = center_x_pos(image, draw, line, font)
    y_pos = 1000
    draw.text((x_pos, y_pos), line, fill=font_color, font=font)


def draw_border(image, draw):
    width, height = image.size
    border_width = 1

    # top border
    draw.line([(0, 0), (width, 0)], fill="black", width=border_width)
    # bottom border
    draw.line([(0, height - border_width), (width, height - border_width)], fill="black", width=border_width)
    # left border
    draw.line([(0, 0), (0, height)], fill="black", width=border_width)
    # right border
    draw.line([(width - border_width, 0), (width - border_width, height)], fill="black", width=border_width)


def contains_many_m_or_w(word):
    count = 0
    for char in word:
        if char.upper() in ['M', 'W']:
            count += 1
            if count == 3:
                return True
    return False


def center_x_pos(image, draw, text, font):
    """
    Calculate center x position for the text to start at with the given image and font.
    """
    _, _, text_width, text_height = draw.textbbox((0, 0), text, font=font)
    image_width, image_height = image.size
    return ((image_width - text_width) // 2) + 5


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


def split_text(text):
    """
    Split text into lines with a maximum number of characters without breaking words.
    """
    # max 18 chars per line
    max_chars = 18
    lines = []
    current_line = ""
    line_count = 0

    words = text.split()

    for i, word in enumerate(words):
        # m and w take a lot of space
        if contains_many_m_or_w(word):
            max_chars = max_chars - 3

        # adjust max_chars for the second and third lines
        if line_count == 1:
            max_chars += 3
        elif line_count == 2:
            max_chars -= 3

        if len(current_line) + len(word) + 1 <= max_chars:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
            line_count += 1

    if current_line:
        lines.append(current_line)
    return lines
