from utils import books
from datetime import datetime,timedelta

def issue():
    book_name=input("Enter Book name:").upper()
    for i in books.values():
        if i["name"] == book_name:
            if i["status"]=="Available":
                i["status"]="issued"
                issue_date=datetime.now()
                due_date=issue_date+timedelta(days=7)
                i["issue_date"]=issue_date.strftime("%Y-%m-%d")
                i["due_date"]=due_date.strftime("%Y-%m-%d")
                print("Book issued successfully!!!🤗")
                print(f"Issue Date:{i['issue_date']}")
                print(f"Due Date:{i['due_date']}")
                
                
            else:
                print("Book already issued!!!")
            return
    else:
        print("Book not available")