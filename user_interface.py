class UserInterface:
    def __init__(self):
        self.error = "That is not a valid option, please try again."

    def main_menu(self):
        while True:
            try:
                operation_option = int(
                    input(
                        """\t\t\t\tMain Menu:
                                1. Book Operations
                                2. User Operations
                                3. Author Operations
                                4. Quit"""
                    )
                )
            except:
                print(self.error)
            else:
                return operation_option

    def book_menu(self):
        while True:
            try:
                operation_option = int(
                    input(
                        """Book Options:
                                            1. Add a new book
                                            2. Borrow a book
                                            3. Return a book
                                            4. Search for a book
                                            5. Display all books"""
                    )
                )
            except:
                print(self.error)
            else:
                return operation_option

    def user_menu(self):
        while True:
            try:
                operation_option = int(
                    input(
                        """User Options:
                                             1. Add a new user
                                             2. View User details
                                             3.Display all users"""
                    )
                )
            except:
                print(self.error)
            else:
                return operation_option

    def author_menu(self):
        while True:
            try:
                operation_option = int(
                    input(
                        """Author Options:
                                             1. Add new author
                                             2. view author details
                                             3.display all authors"""
                    )
                )
            except:
                print(self.error)
            else:
                return operation_option
