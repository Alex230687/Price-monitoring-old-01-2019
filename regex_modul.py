import re


def number_transform(arg):
    """Преобразует строковую сумму с веб-страницы в целочисленный формат.
    Если регулярное выражение возвращает пустую строку, то функция возвращает 0"""
    if '+' in arg:
        subs = re.sub('\+(.*)', '', arg)
    else:
        subs = arg
    arg_to_str = re.sub('[^0-9\.,]', '', subs)
    str_to_num = re.sub('([\.,][0]*)', '', arg_to_str)
    if not str_to_num:
        return 0
    return int(str_to_num)


def isbn_to_barcode(isbn):
    barcode = re.sub('[-]*', '', isbn)
    if not barcode:
        return 0
    return barcode


