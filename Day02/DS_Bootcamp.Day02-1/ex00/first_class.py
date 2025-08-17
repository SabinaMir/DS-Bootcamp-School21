
class Must_read:
    
    filename="data.csv"

       
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
            print(f"Error: {self.filename} not found.")
    except Exception as e:
            print(f"An error occurred: {e}")
           
if __name__== "__main__":
    pass