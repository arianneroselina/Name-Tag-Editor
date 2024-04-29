import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from src.constants import part_of_dict


def create_pdf(image_paths, pdf_filename, image_width, image_height, positions):
    c = canvas.Canvas(pdf_filename, pagesize=A4)

    for i, (image_path, (x, y)) in enumerate(zip(image_paths, positions)):
        c.drawImage(image_path, x, y, width=image_width, height=image_height)

    c.save()


def pack_images_in_pdf(image_folder, output_folder, image_size, key):
    part_of = "COMMITTEES"
    if key in part_of_dict:
        part_of = part_of_dict[key]
    print("Packing name tags of " + part_of + " in PDF files...")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # convert dimensions to pixels
    dpi = 72
    image_width = mm_to_pixels(image_size[0], dpi)
    image_height = mm_to_pixels(image_size[1], dpi)

    positions = [
        (30, A4[1] - 25 - image_height),  # top left
        (5 + image_width + 25, A4[1] - 25 - image_height),  # top right
        (30, A4[1] - 50 - image_height + 25 - image_height),  # bottom left
        (5 + image_width + 25, A4[1] - 50 - image_height + 25 - image_height),  # bottom right
    ]

    # get the list of image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # group images into lists to fit onto PDF pages
    packed_pdfs = []
    images_per_pdf = 4
    for i in range(0, len(image_files), images_per_pdf):
        images_to_pack = [os.path.join(image_folder, image_files[j]) for j in
                          range(i, min(i + 4, len(image_files)))]
        pdf_filename = os.path.join(output_folder, f"{key}_name_tags_{len(packed_pdfs) + 1}.pdf")
        create_pdf(images_to_pack, pdf_filename, image_width, image_height, positions)
        packed_pdfs.append(pdf_filename)

    return packed_pdfs


def mm_to_pixels(mm, dpi):
    return mm * (dpi / 25.4)
