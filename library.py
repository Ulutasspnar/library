class Library:
    def __init__(self):
        # Open the books.txt file in append and read mode. This will create the file if it doesn't exist.
        self.file = open('books.txt', 'a+')

    def __del__(self):
        # Close the books.txt file when the Library object is deleted.
        self.file.close()

    def list_books(self):
        self.file.seek(0)  # Move cursor to the start of the file
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        release_year = input("Enter the first release year: ")
        pages = input("Enter the number of pages: ")
        self.file.write(f"{title},{author},{release_year},{pages}\n")
        self.file.flush()  # Ensures that the written content is saved to the file

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        self.file.seek(0)
        self.file.truncate()  # Clear

        for line in lines:
            if not line.startswith(title_to_remove):
                self.file.write(line + '\n')
        self.file.flush()

# Create an instance of the Library class
lib = Library()

# Menu for interacting with the library system
while True:
    print("* MENU *")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
