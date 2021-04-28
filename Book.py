

class Book:
    def __init__(self, book_id, author_id, title):
        self.book_id =  book_id
        self.author_id =  author_id
        self.title =  title


    @property
    def information(self):
        return self.title
    @property
    def get_author(self):
        return self.author_id

