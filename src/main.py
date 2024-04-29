import os
import shutil

from src.constants import pdf_key, cabor_keys, panitia_key, organisator_key, part_of_dict
from src.create_pdf import pack_images_in_pdf
from src.edit_image import write_names
from src.read_csv import extract_participant_names, extract_committee_names


def main():
    wd = os.getcwd()
    design_path = os.path.join(wd, "designs")
    output_path = os.path.join(wd, "outputs")

    # clean output directory
    shutil.rmtree(output_path)

    img_size = [95, 140]

    print("Design path = " + design_path)
    print("Output path = " + output_path)
    print()

    # participants
    participants_design_path = os.path.join(design_path, "participants_name_tag.jpeg")
    print("Starting to edit participants' name tags...")

    for key in cabor_keys:
        print("##################################################################")
        input_path = os.path.join(wd, f"inputs\\{key}.csv")
        img_output_path = os.path.join(output_path, key)
        pdf_output_path = os.path.join(output_path, key, pdf_key)
        participant_names = extract_participant_names(input_path, key)

        # write names in images
        edited_images = write_names(participants_design_path, img_output_path, participant_names, key)
        print("Images edited: ", len(edited_images))

        # put images in pdf
        packed_pdfs = pack_images_in_pdf(img_output_path, pdf_output_path, img_size, key)
        print("PDFs created: ", len(packed_pdfs))

    print("##################################################################")
    print()

    # committees
    committees_design_path = os.path.join(design_path, "committees_name_tag.jpeg")
    print("Starting to edit committees' name tags...")

    print("##################################################################")
    key = panitia_key
    input_path = os.path.join(wd, f"inputs\\{key}.csv")
    img_output_path = os.path.join(output_path, key)
    pdf_output_path = os.path.join(output_path, key, pdf_key)
    committee_sie_and_names = extract_committee_names(input_path)

    for sie in committee_sie_and_names.keys():
        # write names in images
        edited_images = write_names(committees_design_path, img_output_path, committee_sie_and_names[sie], sie)
        print("Images edited: ", len(edited_images))

    # put images in pdf
    packed_pdfs = pack_images_in_pdf(img_output_path, pdf_output_path, img_size, key)
    print("PDFs created: ", len(packed_pdfs))

    print("##################################################################")
    print("Finished.")


if __name__ == '__main__':
    main()
