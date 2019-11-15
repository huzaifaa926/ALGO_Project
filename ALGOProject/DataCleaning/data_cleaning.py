import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BENCHMARK_DIR = os.path.join(BASE_DIR, "benchmark")
CLEANED_DATA = os.path.join(BASE_DIR, "cleaned_data_benchmark")

def formatting_data(data_to_be_cleaned):
    no_of_nodes = data_to_be_cleaned[0][0]
    data_to_be_cleaned[0] = {"no_of_nodes": no_of_nodes}
    # formatting co-ordinates {n: [x, y]}
    for i in range(1, no_of_nodes+1):
        # saving variable for later use, i.e: for co-ordinates
        temp = data_to_be_cleaned[i]
        # temp[1:] = [x,y]
        data_to_be_cleaned[i] = {int(data_to_be_cleaned[i][0]): temp[1:]}

    # formatting edges data {edge: (edge, cost)}
    node_count = 0
    for i in range(no_of_nodes+1, len(data_to_be_cleaned)-1):
        # saving variable for later use, i.e: for edge, cost
        temp = data_to_be_cleaned[i]

        # IDK why i did that
        # data_to_be_cleaned[i] = {int(data_to_be_cleaned[i][0]) : temp[1:]}
        #####

        data_to_be_cleaned[i] = {node_count : temp[1:]}
        # length of each edge row
        length = len(temp)-1
        # converting edge, cost into tuple (edge, cost)
        for j in range(1, length, 2):
            tuple_temp = ()
            tuple_temp = list(tuple_temp)
            # casting edge to int 
            tuple_temp.insert(0, int(temp[j]))
            # cost is already in float no need to cast
            tuple_temp.insert(1, temp[j+1])
            tuple_temp = tuple(tuple_temp)
            # too complicated :p accessing dictionary in list and then list in that dictionary
            # appending the formatted tuples, after that I'll remove the unformatted data

            # IDK why i did that
            # data_to_be_cleaned[i][int(temp[0])].append(tuple_temp)
            ####

            data_to_be_cleaned[i][node_count].append(tuple_temp)

        # removing unformatted data
        for k in range(1, length+1):

            # IDK why i did that
            # data_to_be_cleaned[i][int(temp[0])].pop(0)
            ####

            data_to_be_cleaned[i][node_count].pop(0)

        node_count += 1

    # formatting: start_node
    data_to_be_cleaned[len(data_to_be_cleaned)-1] = {"starting_node": int(data_to_be_cleaned[len(data_to_be_cleaned)-1][0])}
    return data_to_be_cleaned

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

def clean_data(filename, is_write):
    file_path = os.path.join(BENCHMARK_DIR, filename)
    data_to_be_cleaned = []

    with open(file_path) as file:
        #Discarding first two lines
        file.readline()
        file.readline()
        temp = []
        # reading no of nodes
        temp.append(int(file.readline()))
        data_to_be_cleaned.append(temp)
        #Discarding line breaks
        file.readline()
        # reading co-ordinates
        for i in range(data_to_be_cleaned[0][0]):
            temp = []
            line = file.readline()
            for word in line.split():
                temp.append(float(word))
            data_to_be_cleaned.append(temp)
        #Discarding line breaks
        file.readline()
        # reading edges cost and other data
        for line in file.readlines():
            temp = []
            for word in line.split():
                temp.append(float(word))
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

    if(is_write):
        write_to_file(filename, data_to_be_cleaned)
    data_to_be_cleaned = formatting_data(data_to_be_cleaned)
    return data_to_be_cleaned
    