class Author(object):
    def __init__(self,authorname,country):
        self.authorname=authorname
        self.country=country
    
class Books(object):
    def __init__(self,bookname,author,genre):
        self.bookname=bookname
        self.author=author
        self.genre=genre
