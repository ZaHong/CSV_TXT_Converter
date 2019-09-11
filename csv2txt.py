import csv
import sys

def convert(csv_file, txt_file):
    with open(txt_file, "w") as output_file:
        with open(csv_file, "r") as input_file:
            for row in csv.reader(input_file):
                output_file.write(" ".join(row)+'\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error! \nUsage: * from.csv to.txt")
    else:
        convert(sys.argv[1], sys.argv[2])
