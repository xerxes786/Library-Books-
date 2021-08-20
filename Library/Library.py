class Library:
    def __init__(self, list, user):
        self.booklist = list
        self.name = user
        self.lendlist = {}

    def DisplayBooks(self):
        print(f"Welcome to the {XerXes.name} Library. These are the following books that we have.")
        for books in self.booklist:
            print(books)

    def LendBooks(self, user, book):
        if book not in self.lendlist.keys():
            self.lendlist.update({book:user})
            print("Database has been updated!")

        else:
            print(f"this book is already being used by {self.lendlist[book]}")

    def AddBook(self, book):
        self.booklist.append(book)
        print("Book has been added!")

    def ReturnBook(self, book):
        self.lendlist.pop(book)
        print(f"{self.user} has returned the book.")

if __name__ == '__main__':
    XerXes = Library(['Harry Potter', 'Treasure Island', 'Naruto', 'Game Of Thrones'], "BookNation")

    while(True):
        print(f"Welcome to the {XerXes.name} Library. Select your choice to continue" )
        print("1. Display Books")
        print("2. Lend Books")
        print("3. Add Books")
        print("4. Return Books")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            XerXes.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            XerXes.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            XerXes.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            XerXes.returnBook(book)

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue


    




