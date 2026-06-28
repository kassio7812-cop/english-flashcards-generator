from datetime import datetime


def timestamp():

    return datetime.now().strftime("%H:%M:%S")


def elapsed(seconds):

    return f"{seconds:.2f} s"