import os
import sys

class Research:
    def __init__(self,filename):
        self.filename = filename
    def file_reader(self):
        with open (self.filename,"r") as file:
            lines = file.readlines()   
        if len(lines)<2:
            raise ValueError("The file must have a header and at least one line of data.")         
        header = lines[0].strip().split(",")   
        if len(header)!=2:
             raise ValueError("The header must contain exactly two columns delimited by a comma.")
        for line  in lines[1:]:
            values = line.strip().split(",")
            if len(values) != 2 or not all(value in {"0", "1"} for value in values):
                raise ValueError("Data lines must contain exactly two values, each being '0' or '1', delimited by a comma.")
        return "".join(lines)     
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 first_constructor.py <path_to_file>")
        sys.exit(1)
    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)   
    try:
        research = Research(file_path)
        print(research.file_reader())
    except Exception as e:
        print(e)
        sys.exit(1)
if __name__== "__main__":
    main()            