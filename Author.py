

class Author:
    def __init__(self, author_id, firstname, lastname):
        self.author_id =  author_id
        self.firstname =  firstname
        self.lastaname =  lastname

    def __str__(self):
        return self.firstname

    def __repr__(self):
        return self.firstname

    @property
    def information(self):
        return self.firstname
    @property
    def get_author(self):
        return self.author_id

