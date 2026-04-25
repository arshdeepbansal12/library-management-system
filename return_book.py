from utils import books_db
from datetime import datetime
import math

def calculate_fine(late_days):
    """Calculates progressive fine based on weeks late."""
    fine = 0
    remaining_days = late_days
    week = 1
    
    while remaining_days > 0:
        # Process fine week by week
        days_in_current_week = min(remaining_days, 7)
        
        # Factorial logic: wk 1=10, wk 2=20, wk 3=60, wk 4=240, etc.
        daily_rate = 10 * math.factorial(week) 
        
        fine += days_in_current_week * daily_rate
        remaining_days -= days_in_current_week
        week += 1
        
    return fine

def return_book():
    print("\n" + "="*40)
    print("              RETURN A BOOK")
    print("="*40)
    
    book_name = input("Enter the title of the book to return: ").strip().upper()
    
    if book_name not in books_db:
        print("Error: This book does not belong to our library catalog.")
        return
    
    if books_db[book_name]['status'] == 'available':
        print(f"Notice: '{book_name}' is already currently in the library.")
        return

    # Retrieve issue details
    issue_date = books_db[book_name]['issue_date']
    allotted_days = books_db[book_name]['allotted_days']
    student_name = books_db[book_name]['student_name']
    
    # Calculate days kept
    return_date = datetime.now()
    days_kept = (return_date - issue_date).days
    
    print(f"\n--- Return Details for '{book_name}' ---")
    print(f"Issued To      : {student_name}")
    print(f"Days Allotted  : {allotted_days}")
    print(f"Actual Days Kept: {days_kept}")

    late_days = days_kept - allotted_days
    
    if late_days > 0:
        fine_amount = calculate_fine(late_days)
        print(f"\nStatus: LATE by {late_days} days.")
        print(f"Fine Applied: ₹{fine_amount}")
    else:
        print("\nStatus: ON TIME. No fine applied.")

    # Reset book status back to available
    books_db[book_name] = {
        'status': 'available',
        'student_name': None,
        'issue_date': None,
        'allotted_days': 0
    }
    print(f"\nSuccess: '{book_name}' has been successfully returned.")