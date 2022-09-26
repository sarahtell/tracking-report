from main import read_file, parse_line
from datetime import datetime
import pytest


FIRST_ROW = [
        datetime.strptime("2019-03-01 09:00:00", "%Y-%m-%d %H:%M:%S"),
        "/contact.html",
        "12345"
    ]


def test_read_file():
    file_name = "log.txt"
    file_name_with_path = "test/" + file_name
    
    with pytest.raises(FileNotFoundError) as excinfo:
        read_file(file_name)

    file_content = read_file(file_name_with_path)

    assert "File does not exist!" in str(excinfo.value)
    assert file_content[0] == FIRST_ROW


def test_parse_line():
    line = "|2019-03-01 09:00:00UTC |/contact.html |12345 |"
    parsed_line = parse_line(line)
    assert parsed_line == FIRST_ROW
