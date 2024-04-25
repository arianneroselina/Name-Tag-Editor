import csv


def extract_names(csv_file):
    """
    Read the given CSV file and extract the names
    """
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
