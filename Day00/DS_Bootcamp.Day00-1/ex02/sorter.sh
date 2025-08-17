#!/bin/sh

# Input and output file paths
INPUT_FILE="../ex01/hh.csv"   # Input CSV file from ex01
OUTPUT_FILE="./hh_sorted.csv" # Output sorted CSV file

# Check if the input file exists
if [ ! -f "$INPUT_FILE" ]; then
  echo "Error: Input file $INPUT_FILE not found!"
  exit 1
fi

# Extract header and sort data
{ head -n 1 "$INPUT_FILE"; tail -n +2 "$INPUT_FILE" | sort -t ',' -k2,2 -k1,1; } > "$OUTPUT_FILE"

echo "Sorting completed. Sorted file saved as $OUTPUT_FILE"
