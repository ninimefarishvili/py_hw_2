class Librarian:
    def __init__(self, name, lastname, email, salary) -> None:
        self.name = name
        self.lastname = lastname
        self.email = email
        self.salary = salary


    def __str__(self) -> str:
        return f"librarian's name is {self.name}, lastname is {self.lastname}, email - {self.email} and salary is {self.salary}"

class User:
    def __init__(self, name, lastname, email) -> None:
        self.name = name
        self.lastname= lastname
        self.email = email

    def take_book(self, is_taken):
        if self.is_taken == False:
            return "you can borrow book"
            is_taken == True
        else:
            return "book is not available"

            
    def __str__(self) -> str:
        return f"User's name: {self.name}, lastname: {self.lastname}, email: {self.email}"

   


class Book:
    def __init__(self, title, ganre,is_taken = False ) -> None:
        self.title = title
        self.is_taken = is_taken
        self.ganre = ganre


    def __str__(self) -> str:
        return f"Book title: {self.title}, genre: {self.genre}"