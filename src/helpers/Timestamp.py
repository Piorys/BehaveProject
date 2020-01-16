from datetime import datetime


def now():
    """
    Returns current time
    :return:
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')+' '
