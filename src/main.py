import os

from src.create_pdf import pack_images_in_pdf
from src.edit_image import write_names
from src.read_csv import extract_names

basket_putra_key = "basket_putra"
bulu_tangkis_ganda_putra_key = "bulu_tangkis_ganda_putra"
bulu_tangkis_ganda_campuran_key = "bulu_tangkis_ganda_campuran"
futsal_key = "futsal"
voli_key = "voli"

pdf_key = "pdfs"


def main():
    wd = os.getcwd()
    design_path = os.path.join(wd, "designs/name_tag.jpeg")
    output_path = os.path.join(wd, "outputs")

    # basket putra
    basket_input_path = os.path.join(wd, f"inputs/{basket_putra_key}.csv")
    basket_img_output_path = os.path.join(output_path, basket_putra_key)
    basket_pdf_output_path = os.path.join(output_path, basket_putra_key, pdf_key)
    basket_names = extract_names(basket_input_path)

    # write names in images
    edited_images = write_names(design_path, basket_img_output_path, basket_names)
    print("Images edited: ", len(edited_images))

    # put images in pdf
    img_size = [95, 140]
    packed_pdfs = pack_images_in_pdf(basket_img_output_path, basket_pdf_output_path, img_size, basket_putra_key)
    print("PDFs created: ", len(packed_pdfs))


if __name__ == '__main__':
    main()
