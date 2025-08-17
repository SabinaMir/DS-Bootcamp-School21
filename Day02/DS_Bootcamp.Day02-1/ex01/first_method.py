
class Research:
    filename="data.csv"

    def file_reader(self): 
           
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"Error: {self.filename} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
def main():
    research = Research()
    print(research.file_reader())            
if __name__== "__main__":
    main()