from utils import books

def add():
    book_id=int(input("Enter the id of the book:"))
    book_name = input("Enter the Book name to add: ").upper()
    books[book_id]={"name":book_name,"status":"Available"}
    print(f"Book Added: {book_id}-->{book_name}📖")
    