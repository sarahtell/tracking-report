from datetime import datetime


def set_time_format(date_string, format="%Y-%m-%d %H:%M:%S%Z"):
    return datetime.strptime(date_string, format)


def strip_and_replace_in_line(line):
    return [x.replace("\n", "").strip() for x in line]


def remove_spaces_in_line(line):
    return [x for x in line if x]


def parse_line(line):
    splitted_line = line.split("|")
    stripped_line_replaced = strip_and_replace_in_line(splitted_line)
    date_string, url, user_id = remove_spaces_in_line(stripped_line_replaced)
    return [set_time_format(date_string), url, user_id]
