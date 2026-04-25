from utils import books_db

def show():
    print("\n" + "="*50)
    print("                 LIBRARY CATALOG")
    print("="*50)
    
    if not books_db:
        print("No books are currently stored in the system.")
        return

    print(f"{'BOOK TITLE':<30} | {'STATUS'}")
    print("-" * 50)
    
    for book, details in books_db.items():
        if details['status'] == 'issued':
            student = details['student_name']
            print(f"{book:<30} | ISSUED TO {student}")
        else:
            print(f"{book:<30} | AVAILABLE")
            
    print("=" * 50)