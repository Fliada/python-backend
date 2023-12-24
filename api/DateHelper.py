from datetime import datetime


def format_date(curr: datetime):
    return curr.strftime("%Y-%m-%d %H:%M:%S")
