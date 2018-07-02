"""
    FUNCTIONS
"""
from models.comment import Comment
from models.user import User

class Functions(object):
    logged_in_user = ""


    def create_comment(self, parent, comment1):
        for message in Comment.messages:
            if message['author'] == Functions.logged_in_user:
                comment1.parent = parent
                Comment.messages.append(comment1)

    def delete_comment(self, comment_id):
        pass



