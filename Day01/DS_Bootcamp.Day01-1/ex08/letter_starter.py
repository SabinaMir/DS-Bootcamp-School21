import sys

def generate_letter(email, employee_file="employees.tsv"):
    try:
        with open(employee_file, "r") as file:
            # Skip header
            next(file)
            for line in file:
                name, surname, employee_email = line.strip().split("\t")
                if employee_email == email:
                    print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
                    return
        print(f"No employee found with the email: {email}")
    except FileNotFoundError:
        print(f"Error: File {employee_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script2.py <email>")
        sys.exit(1)

    email = sys.argv[1]
    generate_letter(email)
