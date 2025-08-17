import sys

def process_emails(input_file, output_file="employees.tsv"):
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            # Write the header to the output file
            outfile.write("Name\tSurname\tE-mail\n")
            
            for line in infile:
                email = line.strip()
                if email:
                    try:
                        # Split the email to get the name and surname
                        local_part, domain = email.split("@")
                        name, surname = local_part.split(".")
                        # Capitalize the name and surname
                        name = name.capitalize()
                        surname = surname.capitalize()
                        # Write to the TSV file
                        outfile.write(f"{name}\t{surname}\t{email}\n")
                    except ValueError:
                        print(f"Invalid email format: {email}")
        print(f"Employee data saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script1.py <path_to_email_file>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    process_emails(input_file_path)
