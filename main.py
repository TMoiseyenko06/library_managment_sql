import managment as manage
import user_interface as UI

#Main class that runs the library
class Library(UI.UserInterface):
    def __init__(self, admin):
        self.__admin = admin
        self.__library = UI.UserInterface()
    #runs library and takes all of the options from the user
    def run_library(self):
        print(f"Welcome {self.__admin}")
        while True:
            operation = self.__library.main_menu()
            if operation == 1:
                operation = self.__library.book_menu()
                if operation == 1:
                    book_name = input(
                        "Please enter the name of the book you would like to add:"
                    )
                    book_author = input(
                        "Please enter the id of the author of this book:"
                    )
                    manage.add_book(book_name, book_author)
                elif operation == 2:
                    book_id = input(
                        "Please enter the id of the book you would like to borrow:"
                    )
                    user_id = input(
                        "Please enter the id of the user that would like to borrow the book:"
                    )
                    manage.borrow_book(book_id, user_id)
                elif operation == 3:
                    book_id = input(
                        "Please enter the id of the book you would like to return:"
                    )
                    user_id = input(
                        "Please enter the id of the user that would like to return the book:"
                    )
                    manage.return_book(book_id, user_id)
                elif operation == 4:
                    book_id = input(
                        "Please enter id of the book you would like to find:"
                    )
                    manage.search_for_book(book_id)
                else:
                    manage.display_all_books()
            elif operation == 2:
                operation = self.__library.user_menu()
                if operation == 1:
                    user_name = input(
                        "Please enter the name of the user you would like to add:"
                    )
                    manage.add_user(user_name)
                elif operation == 2:
                    user_id = input(
                        "What is the id of the user you would like to view?"
                    )
                    manage.view_user(user_id)
                else:
                    manage.display_all_users()
            elif operation == 3:
                operation = self.__library.author_menu()
                if operation == 1:
                    author_name = input(
                        "Please enter the name of the author you would like to add:"
                    )
                    author_bio = input(
                        "Please enter the bio of the author you would like to add:"
                    )
                    manage.add_author(author_name, author_bio)
                elif operation == 2:
                    author_id = input(
                        'Please enter the id of the author you would like to view:'
                    )
                    manage.view_author(author_id)
                else:
                    manage.display_all_authors()
            else:
                break

#activates the library
main = Library("Coding Temple")
main.run_library()
