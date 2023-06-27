import re


class Library:

    def __init__(self):
        # boolList = {id:book, ...}
        self.bookList: dict = {}

    def register_book(self, id, book) -> None: 
        self.bookList[id] = book

    def lookupID(self, id: str) -> str: 
        if id in self.bookList: 
            return [str(self.bookList[id]), f"ID: {id}"]
        else:
            return ["No such book exists"]
    
    def lookupTitle(self, title: str) -> str:
        res = []
        for id, book in self.bookList.items():
            if book.title == title:
                res.append(str(book))
                res.append(f'ID: {id}')
        if res == []:
            return ["No such book exists"]
        return res if len(res) == 2 else [f"{len(res)//2} books match the title: {title}"]

    def lookupAuthor(self, author: str) -> str:
        res = []
        for id, book in self.bookList.items():
            if isinstance(book, TraditionalBook) and book.author == author:
                res.append(str(book))
                res.append(f'ID: {id}')
        if res == []:
            return ["No such book exists"]
        return res if len(res) == 2 else [f"{len(res)//2} books match the author: {author}"]


class Book:

    def __init__(self, title: str) -> None:
        self.title = title


class TraditionalBook(Book):

    def __init__(self, title: str, author: str) -> None:
        super().__init__(title)
        self.author = author

    @staticmethod
    def parse_def(book_representation):
        match_result = re.fullmatch('"(.*)" by (.*)', book_representation)
        if match_result is None:
            raise KeyError()
        title = match_result.group(1)
        author = match_result.group(2)
        return TraditionalBook(title, author)

    def __str__(self):
        return f'"{self.title}" by {self.author}'


class Magazine(Book):

    def __init__(self, title: str, issue_num: int) -> None:
        super().__init__(title)
        self.issue_num = issue_num
    
    @staticmethod
    def parse_def(book_representation):
        match_result = re.fullmatch('"(.*)" Issue (.*)', book_representation)
        if match_result is None:
            raise KeyError()
        title = match_result.group(1)
        issue_num = match_result.group(2)
        return Magazine(title, issue_num)

    def __str__(self):
        return f'"{self.title}" Issue {self.issue_num}'
    

def simulate_library(instructions: list[str]) -> list[str]:
    res = []
    library = Library()
    for instruction in instructions:

        command, subinstruction = instruction.split(" ", 1)
        if command == "register":
            book_type, id, book_representation = subinstruction.split(" ", 2)
            if id not in library.bookList:
                if book_type == "book":
                    book = TraditionalBook.parse_def(book_representation)
                elif book_type == "magazine":
                    book = Magazine.parse_def(book_representation)
                library.register_book(id, book)
            # else:
            #     print(f"id: {id} already in stock")
        elif command == "lookup":
            subcommand, rest = subinstruction.split(" ", 1)
            if subcommand == "id":
                res.extend(library.lookupID(rest))
            elif subcommand == "title":
                res.extend(library.lookupTitle(rest))
            elif subcommand == "author":
                res.extend(library.lookupAuthor(rest))

    return res


if __name__ == '__main__':
    instructions = [
        'register book B-001 "Macbeth" by W. Shakespeare',
        'register book B-002 "Hamlet" by W. Shakespeare',
        'register book B-003 "The Lord of the Rings" by J. R. R. Tolkien',
        'register magazine M-001 "New York Times" Issue 2',
        'lookup id B-002',
        'lookup title Macbeth',
        'lookup author W. Shakespeare',
        'lookup author J. R. R. Tolkien',
        'lookup title New York Times'
        ]

    res = simulate_library(instructions)
    for line in res:
        print(line)
