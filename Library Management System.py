books=[]
def add_book(book):
    if book not in books:
        books.append(book)
    else:
        print(f"{book} is already Exit")
def issue_book(book):
    if book in books:
        books.remove(book)
    else:
        print(f"{book} is not available")
def return_book(book):
    if book not in books:
        books.append(book)
    else:
        print(f"{book} not there")
def display_book(books):
    for items in books:
        print(items)
    
while True:
    print("1. add book")
    print("2. issue book")
    print("3. return book")
    print("4. display all books")
    print("5. exits")
    choice=int(input("enter your choice(1-5)"))
    if choice==1:
        book=input("enter book:")
        add_book(book)
    elif choice==2:
        book=input("enter book:")
        issue_book(book)
    elif choice==3:
        book=input("enter book:")
        return_book(book)
    elif choice==4:
        
        display_book(book)
    elif choice==5:
        print("bye bye")
        break 
    else:
        print("invalid choice please try again!")