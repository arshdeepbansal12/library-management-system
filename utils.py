# Data storage using a dictionary
# Structure: 
# {
#   "BOOK_NAME": {
#       "status": "available" or "issued",
#       "student_name": str or None,
#       "issue_date": datetime object or None,
#       "allotted_days": int or 0
#   }
# }
books_db = {}