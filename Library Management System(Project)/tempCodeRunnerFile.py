from utils import books
from datetime import datetime

def return_book():
    book_name = input("Enter Book name: ").upper()

    for i in books.values():
        if i["name"] == book_name:

            if i["status"] == "issued":
                today = datetime.now()
                due_date = i["due_date"]

                if today > due_date:
                    delay_days = (today - due_date).days
                    fine = 0

                    for day in range(1, delay_days + 1):
                        week = (day - 1) // 7 + 1

                        fact = 1
                        for j in range(1, week + 1):
                            fact *= j

                        fine += 10 * fact

                    print("Fine imposed:", fine)
                else:
                    print("No Fine")
                i["status"] = "Available"
                i["issue_date"] = None
                i["due_date"] = None

                print("Book returned successfully!!!")
                return

            else:
                print("Book not issued")
                return

    print("Book not found!!!")