import os
class node:
    __node_number = 0
    __x_coordinate = 0
    __y_coordinate = 0
    # def __init__(self, )

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BENCHMARK_DIR = os.path.join(BASE_DIR, "benchmark")

def read_words(filename):
    with open(filename) as file:
        #Ignoring first line
        file.readline()
        for line in file:
            for word in line.split():
                yield word

def clean_data(filename):
    file_path = os.path.join(BENCHMARK_DIR, filename)
    words = read_words(file_path)
    data_to_be_clean = list(words)

    lower_limit = int(data_to_be_clean[0])*3 + 1
    upper_limit = len(data_to_be_clean) - 1

    for i in range(len(data_to_be_clean)):
        print(len(data_to_be_clean))
        data_to_be_clean.pop(i)
    # for i in range(lower_limit+2, upper_limit, 3):
    #     data_to_be_clean.pop(i)
    #     data_to_be_clean[i+1] = float(data_to_be_clean[i+1])/10000000
    #     data_to_be_clean.pop(i+2)
    #     upper_limit = len(data_to_be_clean)-1

    for a in data_to_be_clean:
        print(a)



if __name__ == "__main__":

    clean_data("input10.txt")
    