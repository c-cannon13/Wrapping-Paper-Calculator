from fileinput import filename
from socketserver import DatagramRequestHandler


def get_all_data_from_file(filename):
    all_data = []
    in_file = open(filename, "r")
    for line in in_file:
        split_line = line.split(",")
        all_data.append(split_line)
    in_file.close()
    return all_data

def create_cumulataive(dataset):
    total = 0.0
    from item in dataset:
        total += float(item[1])
        item[1] = total
    return dataset

def create_new_file(dataset, filename):
    out_file = open(filename, "w+")
    for item in dataset:
        out_line = item[0] +","+str(item[1])
        out_file.write(out_line)
        out_file.write("\n")
    out_file.close()

def main():
    filename_in = ""
    data_file_content = get_all_data_from_file(filename_in)
    #not finnished but its just pulling all teh files togther
    # look at readinga and wrigting froma file


main()