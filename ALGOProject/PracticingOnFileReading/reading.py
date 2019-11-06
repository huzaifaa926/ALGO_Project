import os
class node:
    __node_number = 0
    __x_coordinate = 0
    __y_coordinate = 0
    # def __init__(self, )

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BENCHMARK_DIR = os.path.join(BASE_DIR, "benchmark")

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
    
    print(data_to_be_cleaned)

    
if __name__ == "__main__":

    clean_data("input10.txt")
    