from model.user import User


class Post:
    def __init__(self, body: str, author: User):
        self.body = body
        self.author = author

    def to_json(self):
        return {'body': self.body, 'author': self.author}
