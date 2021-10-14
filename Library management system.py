# LIBRARY MANAGEMENT SYSTEM
class Library:
    def __init__(self,list_of_books , library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lended_book=[]

    def Display_Book(self):
        for items in self.list_of_books:
            print(items)
        return f"These are the books we have "

    def Add_Book(self, new_book):
        self.list_of_books.append(new_book.capitalize())

    def lend_book(self,book):
        if book in self.list_of_books:
            self.lended_book.append(book)
            self.list_of_books.remove(book)
            print("Book lending permission apporved...")
        elif book in self.lended_book:
            print("Sorry the book is already been lended \n"
                  "Currently we only have these :- ")
            for items in self.list_of_books:
                print(items)
        else:
            print("Book's name Entered  is not available or name is wrong "
                  "and the available books are :- ")
            for items in self.list_of_books:
                print(items)


def system():
    try:
        value = True

        Omkars_Library = Library(["Game of Thrones", "Money Heist", "Sex Education", "Naruto", "Stranger Things"],
                                         "Omkars_Library")
        user_name = input("Enter your name : ")

        while value == True:
            print(f"\nWelcome {user_name} to Omkars_Library\n"
                          f"Enter (1) for Displaying the Books :"
                          f"\nEnter (2) for Donating the Books :"
                          f"\nEnter (3) for Lending the Books :"
                          f"\nEnter (4) for Returning the Books :"
                          f"\nEnter (5) for Exit --> ")
            user_input = int(input())

            if user_input == 1:
                print(Omkars_Library.Display_Book())

            elif user_input == 2:
                new_book = input("Enter name of the book you want to donate :- ")
                Omkars_Library.Add_Book(new_book.capitalize())
                print("Book has been successfully added. Thank you for your donation  ")

            elif user_input == 3:
                book = input("Enter name of the book you want to Lend :- ")
                Omkars_Library.lend_book(book.capitalize())

            elif user_input == 4:
                new_book = input("Enter name of the book you want to return :- ")
                Omkars_Library.Add_Book(new_book.capitalize())
                print("Book has been returned successfully! ")

            elif user_input == 5:
                value = False

            else:
                print("Invalid input please try again ")
                system()

    except Exception as e:
        print("Invalid Input !!")
        system()
system()