import sys
import os

class Research:
    def __init__(self, filename):
        self.filename = filename

    def file_reader(self, has_header=True):
        with open(self.filename, "r") as file:
            lines = file.readlines()

        if len(lines) < 2 and has_header:
            raise ValueError("The file must have a header and at least one line of data.")

        if has_header:
            lines = lines[1:]

        data = []
        for line in lines:
            values = line.strip().split(",")
            if len(values) != 2 or not all(value in {"0", "1"} for value in values):
                raise ValueError("Data lines must contain exactly two values, each being '0' or '1', delimited by a comma.")
            data.append([int(value) for value in values])

        return data

    class Calculations:
        @staticmethod
        def counts(data):
            heads = sum(row[0] for row in data)
            tails = sum(row[1] for row in data)
            return heads, tails

        @staticmethod
        def fractions(heads, tails):
            total = heads + tails
            head_fraction = (heads / total) * 100
            tail_fraction = (tails / total) * 100
            return round(head_fraction, 2), round(tail_fraction, 2)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)

    try:
        research = Research(file_path)
        data = research.file_reader(has_header=True)
        print("Data:", data)

        calculations = Research.Calculations()
        heads, tails = calculations.counts(data)
        print("Counts:", heads, tails)

        head_fraction, tail_fraction = calculations.fractions(heads, tails)
        print("Fractions:", head_fraction, tail_fraction)

    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
