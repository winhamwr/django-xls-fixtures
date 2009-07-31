from fixture import DataSet, style

class ValidNoRelationsData(DataSet):
    class one:
        char = "one"
        num = 1
    class two:
        char = "two"
        num = 2

class InvalidNoRelationsData(DataSet):
    class one:
        char = "one"
        invalid = 'test'
    class two:
        char = "two"
        some_other = 2

class AuthorData(DataSet):
    class frank_herbert:
        first_name = "Frank"
        last_name = "Herbert"
    class guido:
        first_name = "Guido"
        last_name = "Van rossum"
        
class BookData(DataSet):
    class dune:
        title = "Dune"
        author = AuthorData.frank_herbert
    
    class python:
        title = 'Python'
        author = AuthorData.guido
        
class ReviewerData(DataSet):
        class ben:
            name = 'ben'
            reviewed = [BookData.dune, BookData.python]

