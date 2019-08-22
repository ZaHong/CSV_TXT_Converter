import pandas as pd
import sys

def convert(txt_file, csv_file):
    df = pd.read_fwf(txt_file)
    df.to_csv(csv_file, index = False, header = None)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error! \nUsage: * from.txt to.csv")
    else:
        convert(sys.argv[1], sys.argv[2])