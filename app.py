"""
Welcome THREAD!
Type help for assistance.
Or type help followed by the command you need help on.
    Usage:
        help
"""

from docopt import docopt, DocoptExit
from functions import Functions
from ui import success, error, magenta
import cmd
import os


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    print(__doc__)


class APP(cmd.Cmd):
    """Application instance class.
    """
    prompt = magenta("THREAD $$$ ")

    @docopt_cmd
    def do_create_user(self, arg):
        """Usage: create_user <usertype> <username> <password>"""
        print(app_instance.create_user(arg['<usertype'], arg['<username'], arg['<password>']))

    @docopt_cmd
    def do_login(self, arg):
        """Usage: login <username> <password>"""
        print(app_instance.login(arg['<username'], arg['<password>']))

    @docopt_cmd
    def do_logout(self, arg):
        """Usage: logout """
        pass

    @docopt_cmd
    def do_add_comment(self, arg):
        """Usage: add_comment <parent> <comment>"""
        print(app_instance.create_comment(arg['<parent'], arg['<comment']))

    @docopt_cmd
    def do_edit_comment(self, arg):
        """Usage: edit_comment <comment_id> <comment>"""
        print(app_instance.edit_comment(arg['<comment_id'], arg['<comment']))

    @docopt_cmd
    def do_delete_comment(self, arg):
        """Usage: delete_comment <comment_id>"""
        pass

    @docopt_cmd
    def do_get_comments(self, arg):
        """Usage: get_comment <comment_id>"""
        pass

    @docopt_cmd
    def do_quit(self, arg):
        """Usage: quit"""
        print ("THREAD has quit!")
        exit()


if __name__ == "__main__":
    try:
        app_instance = Functions()
        os.system('cls' if os.name == 'nt' else 'clear')
        intro()
        APP().cmdloop()
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('THREAD has quit!')
