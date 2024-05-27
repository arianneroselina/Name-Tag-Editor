import os
import shutil

from src.constants import pdf_key, panitia_eng_key
from src.edit_image import DesignWriter, DesignType
from src.read_csv import extract_committee_names

wd = os.getcwd()
design_path = os.path.join(wd, "designs")
output_path = os.path.join(wd, "outputs/certificates")
pdf_output_path = os.path.join(output_path, pdf_key)


def certificates(certificate_design_path):
    print("Starting to edit committees' certificates...")
    print("##################################################################")

    certificate_images = 0

    input_path = os.path.join(wd, f"inputs\\{panitia_eng_key}.csv")
    img_output_path = os.path.join(output_path, panitia_eng_key)

    committee_sie_and_names = extract_committee_names(input_path)

    for sie in committee_sie_and_names.keys():
        # write names in images
        writer = DesignWriter(certificate_design_path, img_output_path, committee_sie_and_names[sie], sie,
                              font_color_name=(0, 0, 0), font_size_name=500, y_pos_name=[4100, 4300],
                              font_color_part_of=(0, 0, 0), font_size_part_of=370, y_pos_part_of=5500)
        edited_images = writer.write_to_design(design_type=DesignType.CERTIFICATE)
        print("Images edited: ", len(edited_images))
        certificate_images = certificate_images + len(edited_images)

    print("##################################################################")
    print("Certificates edited: ", certificate_images)
    print()


def main():
    print("Design path = " + design_path)
    print("Output path = " + output_path)
    print()

    print("Cleaning output directory..")
    # clean output directory
    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    certificate_design_path = os.path.join(design_path, "certificate.png")
    certificates(certificate_design_path)
    print("Finished.")


if __name__ == '__main__':
    main()
