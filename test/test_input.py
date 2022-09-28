from input import read_file, validate_date_input
from datetime import datetime
import pytest


FIRST_ROW = [
    datetime.strptime("2019-03-01 09:00:00", "%Y-%m-%d %H:%M:%S"),
    "/contact.html",
    "12345",
]


def test_validate_date_input(capsys):
    nonvalid_startdate = "2019-03-01 09:00:90"
    nonvalid_enddate = "2019-23-01 09:00:00"

    with pytest.raises(SystemExit):
        validate_date_input(nonvalid_startdate, nonvalid_enddate)
    
    out = capsys.readouterr()

    assert 'Date should have the correct format: "YYYY-MM-DD HH:MM:SS"' in out.out


def test_read_file(capsys):
    file_that_does_not_exist = "random_file.txt"
    file_that_exists = "test/log.txt"

    with pytest.raises(SystemExit):
        read_file(file_that_does_not_exist)

    out = capsys.readouterr()

    file_content = read_file(file_that_exists)

    assert "File does not exist!" in out.out
    assert file_content[0] == FIRST_ROW
