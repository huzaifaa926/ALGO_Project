from .data_cleaning import clean_data

def cleaned_data(index, is_write=False):
    files_to_be_read = ["input10.txt", "input20.txt", "input30.txt",
                        "input40.txt", "input50.txt", "input60.txt",
                        "input70.txt", "input80.txt", "input90.txt",
                        "input100.txt",
                        ]
    returned_data = clean_data(filename=files_to_be_read[index], is_write=is_write)
    return returned_data