import sys
import os
from random import randint

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
    def __init__(self, data):
        self.data = data

    def counts(self):
        heads = sum(row[0] for row in self.data)
        tails = sum(row[1] for row in self.data)
        return heads, tails

    def fractions(self):
        heads, tails = self.counts()
        total = heads + tails
        head_fraction = (heads / total) * 100
        tail_fraction = (tails / total) * 100
        return round(head_fraction, 2), round(tail_fraction, 2)

class Analytics(Calculations):
    def predict_random(self, num_predictions):
        predictions = []
        for _ in range(num_predictions):
            if randint(0, 1) == 0:
                predictions.append([1, 0])
            else:
                predictions.append([0, 1])
        return predictions

    def predict_last(self):
        return self.data[-1] if self.data else None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 first_child.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)

    try:
        research = Research(file_path)
        data = research.file_reader(has_header=True)
        print("Data:", data)

        calculations = Analytics(data)
        heads, tails = calculations.counts()
        print("Counts:", heads, tails)

        head_fraction, tail_fraction = calculations.fractions()
        print("Fractions:", head_fraction, tail_fraction)

        random_predictions = calculations.predict_random(3)
        print("Random Predictions:", random_predictions)

        last_prediction = calculations.predict_last()
        print("Last Prediction:", last_prediction)

    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
