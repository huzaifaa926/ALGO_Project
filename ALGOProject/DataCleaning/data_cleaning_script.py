from data_cleaning import clean_data

if __name__ == "__main__":
    files_to_be_read = ["input10.txt", "input20.txt", "input30.txt",
                        "input40.txt", "input50.txt", "input60.txt",
                        "input70.txt", "input80.txt", "input90.txt",
                        "input100.txt",
                        ]
    for file_to_be_read in files_to_be_read:
        temp = clean_data(filename=file_to_be_read, is_write=False)
        break
    print(temp)
    for i in temp:
        print(i)