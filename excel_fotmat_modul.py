def price_cell_format(workbook, rrc, price):
    """условное форматирование цены"""
    user_format = workbook.add_format()
    user_format.set_font_name('Tahoma')
    user_format.set_font_size(8)
    user_format.set_align('vcenter')
    user_format.set_bottom()
    user_format.set_top()
    user_format.set_left()
    user_format.set_right()
    user_format.set_num_format('_-* # ##0_р_._-;-* # ##0_р_._-;_-* "-"??_р_._-;_-@_-')
    if price == 0:
        user_format.set_font_color('#000000')
        user_format.set_bg_color('#ffffff')
    elif price == rrc:
        user_format.set_font_color('#00b050')
        user_format.set_bg_color('#e2efda')
    elif price < rrc:
        user_format.set_font_color('#ff0000')
        user_format.set_bg_color('#fce4d6')
    elif price > rrc:
        user_format.set_font_color('#806000')
        user_format.set_bg_color('#fff2cc')
    return user_format


def second_price_cell_format(workbook, rrc, price, max_sql_price):
    """условное форматирование цены"""
    user_format = workbook.add_format()
    user_format.set_font_name('Tahoma')
    user_format.set_font_size(8)
    user_format.set_align('vcenter')
    user_format.set_bottom()
    user_format.set_top()
    user_format.set_left()
    user_format.set_right()
    user_format.set_num_format('_-* # ##0_р_._-;-* # ##0_р_._-;_-* "-"??_р_._-;_-@_-')
    if price == 0:
        user_format.set_font_color('#000000')
        user_format.set_bg_color('#ffffff')
    elif price == max_sql_price:
        user_format.set_font_color('#806000')
        user_format.set_bg_color('#fff2cc')
    elif price >= rrc:
        user_format.set_font_color('#00b050')
        user_format.set_bg_color('#e2efda')
    elif price < rrc:
        user_format.set_font_color('#ff0000')
        user_format.set_bg_color('#fce4d6')
    return user_format


def text_row_format(workbook, worksheet=None):
    """условное форматирование текста"""
    user_format = workbook.add_format()
    user_format.set_font_name('Tahoma')
    user_format.set_font_size(8)
    user_format.set_align('vcenter')
    user_format.set_align('left')
    user_format.set_border()
    user_format.set_font_color('#000000')
    user_format.set_bg_color('#ffffff')
    user_format.set_indent(1)
    return user_format


def text_left_top_format(workbook, worksheet=None):
    user_format = workbook.add_format()
    user_format.set_bg_color('#c0c0c0')
    user_format.set_bold()
    user_format.set_font_name('Tahoma')
    user_format.set_font_size(8)
    user_format.set_align('center')
    user_format.set_align('vcenter')
    user_format.set_border()
    return user_format


def text_right_top_format(workbook, worksheet=None):
    user_format = workbook.add_format()
    user_format.set_bold()
    user_format.set_font_name('Tahoma')
    user_format.set_font_size(8)
    user_format.set_align('center')
    user_format.set_align('vcenter')
    user_format.set_border()
    user_format.set_rotation(90)
    return user_format
