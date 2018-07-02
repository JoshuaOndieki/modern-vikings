from datetime import datetime


class Comment (object):
    messages = []

    def __init__(self, author, message, parent):
        self.author = author
        self.parent = parent
        self.timestamp = datetime.utcnow()
        self.message = message

    def create(self):
        Comment.messages.append (self)

    def delete(self):
        Comment.messages.remove(self)

    def edit(self, message):
        self.message = message

    @staticmethod
    def get_comment_by_id(comment_id):
        for msg in Comment.messages:
            if msg['comment_id'] == comment_id:
                return msg
        return None
