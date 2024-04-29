import csv
import pandas as pd

from src.constants import part_of_dict


def extract_participant_names(csv_file, key):
    """
    Read the given participants CSV file and extract the names
    """
    print("Reading CSV input file of " + part_of_dict[key] + "...")
    names = []
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            # check that the first column is empty
            if row[0].strip() == "" and len(row) >= 2:
                # extract the name from the second column
                name = row[1].strip()
                if name:
                    names.append(name)
    return names


def extract_committee_names(csv_file):
    """
    Read the given committee CSV file and extract the names
    """
    print("Reading COMMITTEES CSV input file...")
    sie_name_dict = {}
    last_sie = ""

    df = pd.read_csv(csv_file, skiprows=1)
    for index, row in df.iterrows():
        name = row["Nama lengkap"]
        sie = row["Sie/Jabatan"]
        if pd.isnull(sie):
            # if "Sie" is empty, take the last entry in the column
            sie = last_sie
        else:
            last_sie = sie

        # skip if name is empty or is the last row
        if pd.isnull(name) or "Total" in name:
            continue

        if sie in sie_name_dict:
            sie_name_dict[sie].append(name)
        else:
            sie_name_dict[sie] = [name]

    return sie_name_dict
