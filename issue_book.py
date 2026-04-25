from utils import books_db
from datetime import datetime

def issue():
    print("\n" + "="*40)
    print("               ISSUE A BOOK")
    print("="*40)
    
    book_name = input("Enter the title of the book to issue: ").strip().upper()
    
    if book_name not in books_db:
        print("Error: Book is not available in the library catalog.")
        return
    
    if books_db[book_name]['status'] == 'issued':
        student = books_db[book_name]['student_name']
        print(f"Notice: '{book_name}' is currently issued to {student}.")
        return

    student_name = input("Enter the student's name: ").strip().title()
    
    try:
        allotted_days = int(input("Enter the allotted days for issuance: "))
        if allotted_days <= 0:
            print("Error: Days must be greater than 0.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        return

    # Update dictionary with issue details
    books_db[book_name]['status'] = 'issued'
    books_db[book_name]['student_name'] = student_name
    books_db[book_name]['issue_date'] = datetime.now()
    books_db[book_name]['allotted_days'] = allotted_days

    print("\n" + "-"*40)
    print("             ISSUE SUCCESSFUL")
    print("-"*40)
    print(f"Book Assigned : {book_name}")
    print(f"Student Name  : {student_name}")
    print(f"Duration      : {allotted_days} days")
    
    # Notice for fine policy
    print("\n*** FINE POLICY NOTICE ***")
    print("Please return the book within the allotted time to avoid fines.")
    print("Late fines apply progressively:")
    print("  - 1st week late: ₹10/day")
    print("  - 2nd week late: ₹20/day  (10*2)")
    print("  - 3rd week late: ₹60/day  (10*2*3)")
    print("  - Continues multiplying per week.")