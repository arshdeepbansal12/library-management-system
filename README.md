# 📚 Python Library Management System

A robust, terminal-based Library Management System built with Python. This project provides a clean interactive command-line interface for managing library catalog data, tracking book issuances, and dynamically calculating progressive late fees.

## ✨ Features

* **Centralized Data Management:** Utilizes a dictionary-based data structure to efficiently track book status, borrower details, and issuance timelines.
* **Real-time Tracking:** Integrates Python's `datetime` module to log exact issuance and return dates.
* **Dynamic Fine Calculation:** Implements a progressive, factorial-based fine system for overdue books (calculates fees week-by-week).
* **Modular Architecture:** Code is separated into logical, single-responsibility modules for easy maintenance and readability.
* **Input Validation:** Includes robust error handling to prevent application crashes from invalid user inputs.
* **Clean Console UI:** Features formatted tabular outputs and clear separation of terminal menus for a better user experience.

## 📂 Project Structure

* `main.py` - The entry point of the application. Handles the main menu loop and user routing.
* `utils.py` - Acts as the central database, storing the `books_db` dictionary for state management.
* `add_books.py` - Logic for adding new books to the library catalog.
* `issue_book.py` - Handles assigning books to students, logging the date, and setting the allotted return timeframe.
* `return_book.py` - Manages the return process, checks actual days kept against allotted days, and calculates fines if overdue.
* `show_books.py` - Renders a clean, formatted table of all books and their current availability status.

## 🚀 How to Run

**Prerequisites:** Ensure you have Python 3.x installed on your system.

1. Clone this repository or download the project files.
2. Open your terminal or command prompt.
3. Navigate to the project directory:
   ```bash
   cd path/to/library-management
Run the main application file:
python main.py

💸 Fine Policy
To encourage timely returns, this system enforces a progressive late fee policy. Fines multiply based on the number of weeks a book is overdue:

1st Week Late: ₹10 per day

2nd Week Late: ₹20 per day (₹10 * 2)

3rd Week Late: ₹60 per day (₹10 * 2 * 3)

The multiplier continues to increase factorially for subsequent weeks.

🛠️ Built With
Python 3 - Core programming language

datetime module - For timestamping and duration calculations

math module - For factorial fine computations
