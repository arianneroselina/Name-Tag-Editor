# Name Tag and Certificate Generator

## 🏆 Overview

This program automatically creates:
   - Name tags for participants from different sports categories (cabor)
   - Name tags for committee members organized by division (sie)
   - Empty name tags as placeholders
   - Certificates for committee members

It takes names from CSV files and prints them onto your design templates, then organizes everything into ready-to-print PDFs.

## 📋 Before You Start

You'll need:
1. [Python 3](https://www.python.org/downloads/) installed
2. The template design files
3. Your participant/committees lists in CSV format

## 🚀 Usage

### For Name Tags

#### Step 1: Prepare your CSV files

1. **Input Files** - Put these in the `inputs/` directory following these formats:
   - **For participants** (5 required files, exact names):
      ```
      basket_putra.csv
      bulu_tangkis_ganda_campuran.csv
      bulu_tangkis_ganda_putra.csv
      futsal.csv
      voli.csv
      ```
      Example content:
      ```
      ,Name
      ,John Doe
      ,Jane Smith
      ,...
      ```
      - First column is empty (used as a marker)
      - Second column contains participant names 
      - One CSV file per sports category.
   
   - **For committees** (1 file)
      ```
      panitia.csv
      ```
      Example content:
      ```
      Sie/Jabatan,Nama lengkap,...
      Logistik,John Doe,...
      ,Jane Smith,...   # this will be considered "Logistik" as well, following the previous entry
      Acara,Robert Johnson,...
      ...
      ```
      - Must include "Sie/Jabatan" and "Nama lengkap" headers
      - Empty division cells inherit from previous row
      - Rows with "Total" in name field are skipped (last row)

2. **Design Templates** - Put these in the `designs/` directory:
   - `participants_name_tag.png` - template design for participant name tags 
   - `committees_name_tag.png` - template design for committee name tags

#### Step 2: Run the program

   ```bash
    python src/name_tags/main.py
   ```

#### Step 3: Get Your Outputs

Output will be generated in `outputs/name_tags/` (individual images and ready-to-print PDFs)

### For Certificates

#### Step 1: Prepare your CSV files

1. **Input Files** - Prepare your committee CSV file in the `inputs/` directory using the same committee format as above

2. **Design Templates** - Put this in the `designs/` directory:
   - `certificate.png` - template design for certificates

#### Step 2: Run the program

   ```bash
    python src/certificates/main.py
   ```

#### Step 3: Get Your Outputs

Output will be generated in `outputs/certificates/` (individual images)

## 🛠️ For Developers

### File Structure
   ```
   project/
   ├── designs/              # Contains design templates
   ├── inputs/               # Contains CSV files with names
   ├── outputs/              # Generated output files
   ├── src/                  # Source code
   │   ├── constants.py      # Configuration constants
   │   ├── create_pdf.py     # PDF generation logic
   │   ├── edit_image.py     # Image editing functionality
   │   └── read_csv.py       # CSV parsing functions
   └── main.py               # Main program entry point
   ```

### Customization Options

1. **Design Templates**
   - Replace the PNG files in the designs directory with your own templates 
   - Ensure the text positioning matches your design (adjust coordinates in the code)

2. **Text Customization** (in `edit_image.py`)
   - Font styles (add the otf file in the `fonts` directory)
   - Text colors 
   - Positioning (x, y coordinates)
   - Size adjustments

3. **CSV Format**
   - The tool expects specific CSV formats (see above)
   - Modify `read_csv.py` if your format differs

### Performance Notes

- The tool currently uses PNG format which can be slow for processing 
- Consider switching to JPEG for faster processing (see TODO in code)

## ❓ Troubleshooting

- **Missing Files**: Ensure all required CSV and design template files exist in the correct directories 
- **Permission Issues**: Make sure the program has write access to the output directories 
- **Text Positioning**: If text appears misaligned, adjust the coordinates in the relevant functions 
- **CSV Reading Issues**:
  - Verify file encoding is UTF-8
  - Check column headers exactly match expected values

## 📜 License
Free for organizational use. Contact author for commercial applications.