import os
import shutil
class node:
    __node_number = 0
    __x_coordinate = 0
    __y_coordinate = 0
    # def __init__(self, )

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BENCHMARK_DIR = os.path.join(BASE_DIR, "benchmark")
CLEANED_DATA = os.path.join(BASE_DIR, "cleaned_data_benchmark")

def write_to_file(filename, data_to_be_cleaned):
    # try:
    #     shutil.rmtree(CLEANED_DATA)
    # except OSError:
    #     print ("Deletion of the directory %s failed" % CLEANED_DATA)
    try:
        os.mkdir(CLEANED_DATA)
    except OSError:
        print ("Creation of the directory %s failed" % CLEANED_DATA)
    
    file_path = os.path.join(CLEANED_DATA, filename)
    file = open(file_path, "a")
    for words in data_to_be_cleaned:
        for i in range(len(words)):
            file.write(str(words[i]))
            if i!=len(words)-1:
                file.write(" ")
        file.write("\n")

def clean_data(filename):
    file_path = os.path.join(BENCHMARK_DIR, filename)
    data_to_be_cleaned = []

    with open(file_path) as file:
        #Discarding first two lines
        file.readline()
        file.readline()
        temp = []
        temp.append(int(file.readline()))
        data_to_be_cleaned.append(temp)
        #Discarding line breaks
        file.readline()
        for i in range(data_to_be_cleaned[0][0]):
            temp = []
            line = file.readline()
            for word in line.split():
                temp.append(word)
            data_to_be_cleaned.append(temp)
        #Discarding line breaks
        file.readline()
        for line in file.readlines():
            temp = []
            for word in line.split():
                temp.append(word)
            data_to_be_cleaned.append(temp)
        #Removing the line break from second last line
        data_to_be_cleaned.pop(-2)

    lower_bound = data_to_be_cleaned[0][0] + 1
    upper_bound = len(data_to_be_cleaned) - 1
    for i in range(lower_bound, upper_bound):
        list_len = len(data_to_be_cleaned[i]) - 1
        is_pop = True
        is_convert = True
        while list_len>1:
            if is_pop:
                data_to_be_cleaned[i].pop(list_len)
                is_pop = False
            else:
                if is_convert:
                    data_to_be_cleaned[i][list_len] = float(data_to_be_cleaned[i][list_len])/10000000
                    is_convert = False
                else:
                    is_convert = True
                is_pop = True
            list_len-=1

    write_to_file(filename, data_to_be_cleaned)
    # print(data_to_be_cleaned)

    
if __name__ == "__main__":

    clean_data("input10.txt")
    