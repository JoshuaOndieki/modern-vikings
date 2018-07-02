from datetime import datetime


class Comment (object):
    messages = []

    def __init__(self, author, message):
        self.author = author
        self.timestamp = datetime.utcnow()
        self.message = message

    def create(self):
        Comment.messages.append (self)

    def delete(self):
        Comment.messages.remove(self)

    def edit(self, message):
        self.message = message
