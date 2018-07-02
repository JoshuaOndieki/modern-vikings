"""
    APP ui
"""

from termcolor import colored


def success(text):
    """Returns a green colored text
    """
    return(colored(text, 'green', attrs=['bold']))


def magenta(text):
    """Returns a magenta colored text
    """
    return(colored(text, 'magenta', attrs=['blink', 'bold']))


def error(text):
    """Returns a red colored text
    """
    return(colored(text, 'red', attrs=['bold']))
