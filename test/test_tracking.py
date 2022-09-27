from main import read_file, parse_line
from datetime import datetime
import pytest


FIRST_ROW = [
    datetime.strptime("2019-03-01 09:00:00", "%Y-%m-%d %H:%M:%S"),
    "/contact.html",
    "12345",
]


def test_read_file(capsys):
    file_that_does_not_exist = "random_file.txt"
    file_that_exists = "test/log.txt"

    with pytest.raises(SystemExit):
        read_file(file_that_does_not_exist)

    out = capsys.readouterr()

    file_content = read_file(file_that_exists)

    assert "File does not exist!" == out.out
    assert file_content[0] == FIRST_ROW


def test_parse_line():
    line = "|2019-03-01 09:00:00UTC |/contact.html |12345 |"
    parsed_line = parse_line(line)
    assert parsed_line == FIRST_ROW
