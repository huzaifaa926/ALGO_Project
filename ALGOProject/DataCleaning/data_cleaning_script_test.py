from data_cleaning import clean_data

def cleaned_data():
    files_to_be_read = ["input10.txt", "input20.txt", "input30.txt",
                        "input40.txt", "input50.txt", "input60.txt",
                        "input70.txt", "input80.txt", "input90.txt",
                        "input100.txt",
                        ]
    temp = clean_data(filename=files_to_be_read[0], is_write=False)
    return temp