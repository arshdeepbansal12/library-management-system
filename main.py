from add_books import add
from issue_book import issue
from show_books import show
from return_book import return_book

def library():
    while True:
        print("\n" + "#"*40)
        print("      📚 LIBRARY MANAGEMENT SYSTEM 📚")
        print("#"*40)
        print("1. Add a New Book")
        print("2. Show Catalog")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. Exit System")
        print("-" * 40)
        
        try:
            choice = int(input("Please enter your choice (1-5): "))
            
            if choice == 1:
                add()
            elif choice == 2:
                show()
            elif choice == 3:
                issue()
            elif choice == 4:
                return_book()
            elif choice == 5: 
                print("\nSaving data... Thank you for using the Library System.")
                break
            else:
                print("\nInvalid choice. Please select a valid number (1-5).")
        except ValueError:
            print("\nError: Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    library()