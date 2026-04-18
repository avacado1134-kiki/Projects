from utils import books
def show():
    if not books:
        print("Library is empty")

    else:
        for i,j in books.items():

            print(i,":",j["name"],"-",j["status"])