import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from src.constants import part_of_dict, empty_key


def create_pdf(image_folder, image_files, image_size, pdf_filename):
    # image settings and styles
    images_per_pdf = 4
    dpi = 72
    image_width = mm_to_pixels(image_size[0], dpi)
    image_height = mm_to_pixels(image_size[1], dpi)
    positions = [
        (23, A4[1] - 35 - image_height),  # top left
        (image_width + 23, A4[1] - 35 - image_height),  # top right
        (23, A4[1] - 35 - 2 * image_height),  # bottom left
        (image_width + 23, A4[1] - 35 - 2 * image_height),  # bottom right
    ]

    c = canvas.Canvas(pdf_filename, pagesize=A4)

    num_pages = 0
    for i in range(0, len(image_files), images_per_pdf):
        images_to_pack = [os.path.join(image_folder, image_files[j]) for j in
                          range(i, min(i + 4, len(image_files)))]
        draw_images_in_pdf(c, images_to_pack, image_width, image_height, positions)
        num_pages = num_pages + 1

    c.save()
    return num_pages


def draw_images_in_pdf(pdf_canvas, image_paths, image_width, image_height, positions):
    for i, (image_path, (x, y)) in enumerate(zip(image_paths, positions)):
        pdf_canvas.drawImage(image_path, x, y, width=image_width, height=image_height)
    pdf_canvas.showPage()


def pack_images_in_pdf(image_folder, output_folder, image_size, key):
    part_of = "COMMITTEES"
    if key in part_of_dict:
        part_of = part_of_dict[key]
    print("Packing name tags of " + part_of + " in PDF files...")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # print each 12 empty name tags for participants and committees
    if empty_key in key:
        image_files = [image_folder] * 12
    else:
        # get the list of image files in the folder
        image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # group images into lists to fit onto PDF pages
    pdf_filename = os.path.join(output_folder, f"{key}_name_tags.pdf")
    num_pages = create_pdf(image_folder, image_files, image_size, pdf_filename)

    return num_pages


def mm_to_pixels(mm, dpi):
    return mm * (dpi / 25.4)
