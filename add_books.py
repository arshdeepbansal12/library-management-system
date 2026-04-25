from utils import books_db

def add():
    print("\n" + "="*40)
    print("             ADD A NEW BOOK")
    print("="*40)
    
    book_name = input("Enter the title of the book to add: ").strip().upper()
    
    if not book_name:
        print("Error: Book name cannot be empty.")
        return

    if book_name in books_db:
        print(f"Notice: '{book_name}' already exists in the catalog.")
    else:
        # Initialize the book's record in the dictionary
        books_db[book_name] = {
            'status': 'available',
            'student_name': None,
            'issue_date': None,
            'allotted_days': 0
        }
        print(f"Success: '{book_name}' has been added to the library.")