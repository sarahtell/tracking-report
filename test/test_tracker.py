from main import read_file
from tracker import Tracker
from datetime import datetime

LOGS = read_file("test/log.txt")
DATE_TIME_START = datetime(2019, 3, 1, 9, 0, 0)
DATE_TIME_END = datetime(2019, 3, 2, 11, 59, 59)
TRACKER = Tracker(LOGS, DATE_TIME_START, DATE_TIME_END)


FINAL_ROW = [
        datetime.strptime("2019-03-02 11:00:00", "%Y-%m-%d %H:%M:%S"),
        "/contact.html",
        "12348"
    ]


def test_calculate_page_views():
    page_views = TRACKER.calculate_page_views()
    assert page_views == {
        "/contact.html": {"page views": 5},
        "/home.html": {"page views": 3},
    }


def test_calculate_unique_visits():
    unique_visits = TRACKER.calculate_unique_visits()
    assert unique_visits == {
        "/contact.html": {
            "visitors": ["12345", "12346", "12347", "12348"],
            "visits": 4,
        },
        "/home.html": {"visitors": ["12347", "12348", "12349"], "visits": 3},
    }


def test_filter_rows_by_date_range():
    date_range = TRACKER.filter_rows_by_date_range()
    assert date_range[-1] == FINAL_ROW
