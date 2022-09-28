from parser import parse_line, set_time_format
from datetime import datetime


FIRST_ROW = [
    datetime.strptime("2019-03-01 09:00:00", "%Y-%m-%d %H:%M:%S"),
    "/contact.html",
    "12345",
]


def test_set_time_format():
    date_string_utc = "2017-06-13 17:59:00UTC"
    date_utc_time_format = set_time_format(date_string_utc)

    date_string = "2019-02-14 18:59:00"
    date_time_format = set_time_format(date_string, format="%Y-%m-%d %H:%M:%S")

    assert date_utc_time_format == datetime(2017, 6, 13, 17, 59, 0)
    assert date_time_format == datetime(2019, 2, 14, 18, 59, 0)


def test_parse_line():
    line = "|2019-03-01 09:00:00UTC |/contact.html |12345 |"
    parsed_line = parse_line(line)
    assert parsed_line == FIRST_ROW
