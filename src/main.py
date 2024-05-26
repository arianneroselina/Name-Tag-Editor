import os
import shutil

from src.constants import pdf_key, cabor_keys, panitia_key, empty_participants_key, empty_committees_key, \
    bulu_tangkis_ganda_campuran_key
from src.create_pdf import pack_images_in_pdf
from src.edit_image import write_names
from src.read_csv import extract_participant_names, extract_committee_names

wd = os.getcwd()
design_path = os.path.join(wd, "designs")
output_path = os.path.join(wd, "outputs")
pdf_output_path = os.path.join(output_path, pdf_key)
img_size = [97, 136]


def participants(participants_design_path):
    print("Starting to edit participants' name tags...")

    participants_images = 0
    participants_pdf_pages = 0

    for key in cabor_keys:
        print("##################################################################")
        input_path = os.path.join(wd, f"inputs\\{key}.csv")
        img_output_path = os.path.join(output_path, key)
        participant_names = extract_participant_names(input_path, key)

        # TODO: remove this if bulu tangkis ganda campuran is full, currently there are two empty slots
        if key == bulu_tangkis_ganda_campuran_key:
            participant_names.extend(["", ""])

        # write names in images
        edited_images = write_names(participants_design_path, img_output_path, participant_names, key)
        print("Images edited: ", len(edited_images))
        participants_images = participants_images + len(edited_images)

        # put images in pdf
        num_pages = pack_images_in_pdf(img_output_path, pdf_output_path, img_size, key)
        print("Pages in PDF: ", num_pages)
        participants_pdf_pages = participants_pdf_pages + num_pages

    print("##################################################################")
    print("PARTICIPANTS Images edited: ", participants_images)
    print("PARTICIPANTS Pages in PDF: ", participants_pdf_pages)
    print()

    return participants_images, participants_pdf_pages


def committees(committees_design_path):
    print("Starting to edit committees' name tags...")
    print("##################################################################")

    committees_images = 0

    input_path = os.path.join(wd, f"inputs\\{panitia_key}.csv")
    img_output_path = os.path.join(output_path, panitia_key)

    committee_sie_and_names = extract_committee_names(input_path)

    for sie in committee_sie_and_names.keys():
        # write names in images
        edited_images = write_names(committees_design_path, img_output_path, committee_sie_and_names[sie], sie)
        print("Images edited: ", len(edited_images))
        committees_images = committees_images + len(edited_images)

    # put images in pdf
    committees_pdf_pages = pack_images_in_pdf(img_output_path, pdf_output_path, img_size, panitia_key)
    print("Pages in PDF: ", committees_pdf_pages)

    print("##################################################################")
    print("COMMITTEES Images edited: ", committees_images)
    print("COMMITTEES Pages in PDF: ", committees_pdf_pages)
    print()

    return committees_images, committees_pdf_pages


def empty(participants_design_path, committees_design_path):
    print("Adding empty name tags...")
    print("##################################################################")

    empty_images = 24

    empty_pdf_pages_1 = pack_images_in_pdf(participants_design_path, pdf_output_path, img_size, empty_participants_key)
    empty_pdf_pages_2 = pack_images_in_pdf(committees_design_path, pdf_output_path, img_size, empty_committees_key)
    empty_pdf_pages = empty_pdf_pages_1 + empty_pdf_pages_2
    print("Pages in PDF: ", empty_pdf_pages)

    print("##################################################################")
    print("EMPTY Images added: ", empty_images)
    print("EMPTY Pages in PDF: ", empty_pdf_pages)
    print()

    return empty_images, empty_pdf_pages


def main():
    print("Design path = " + design_path)
    print("Output path = " + output_path)
    print()

    print("Cleaning output directory..")
    # clean output directory
    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    # TODO: png is super slow! use jpeg for faster process
    participants_design_path = os.path.join(design_path, "participants_name_tag.png")
    committees_design_path = os.path.join(design_path, "committees_name_tag.png")

    # participants
    total_images, total_pdf_pages = participants(participants_design_path)

    # committees
    committees_images, committees_pdf_pages = committees(committees_design_path)
    total_images = total_images + committees_images
    total_pdf_pages = total_pdf_pages + committees_pdf_pages

    # empty
    empty_images, empty_pdf_pages = empty(participants_design_path, committees_design_path)
    total_images = total_images + empty_images
    total_pdf_pages = total_pdf_pages + empty_pdf_pages

    print("TOTAL Images edited: ", total_images)
    print("TOTAL Pages in PDF: ", total_pdf_pages)
    print("Finished.")


if __name__ == '__main__':
    main()
