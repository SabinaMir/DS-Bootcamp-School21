def convert_csv_to_tsv(input_file, output_file):

    with open(input_file,"r", encoding="utf-8") as csv_file:
        lines = csv_file.readlines()
    tsv_lines = []
    for line in lines:
        tsv_line = line.strip().replace(",","\t")
        tsv_lines.append(tsv_line)
    with open(output_file,"w", encoding="utf-8") as tsv_file:
      for tsv_line in tsv_lines:
        tsv_file.write(tsv_line + "\n")
if __name__ =="__main__":
    input_file = "ds.csv"
    output_file = "ds.tsv"

    convert_csv_to_tsv(input_file, output_file)
    print(f"Файл {output_file} успешно создан")