import datetime


def days(date):
    current_day = datetime.date.today()
    delta = current_day - date
    days_in_sale = delta.days
    return days_in_sale
