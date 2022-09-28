from input import read_file
from report_manager import ReportManager
from datetime import datetime


LOGS = read_file("test/log.txt")
DATE_TIME_START = datetime(2019, 3, 1, 9, 30, 0)
DATE_TIME_END = datetime(2019, 3, 2, 11, 59, 59)
REPORT_MANAGER = ReportManager(LOGS, DATE_TIME_START, DATE_TIME_END)


FIRST_ROW = [
    datetime.strptime("2019-03-01 10:00:00UTC", "%Y-%m-%d %H:%M:%S%Z"),
    "/contact.html",
    "12345",
]


FINAL_ROW = [
    datetime.strptime("2019-03-02 11:00:00UTC", "%Y-%m-%d %H:%M:%S%Z"),
    "/contact.html",
    "12348",
]


def test_filter_rows_by_date_range():
    REPORT_MANAGER.filter_rows_by_date_range()
    assert REPORT_MANAGER.filtered_logs[0] == FIRST_ROW
    assert REPORT_MANAGER.filtered_logs[-1] == FINAL_ROW


def test_calculate_page_views():
    REPORT_MANAGER.calculate_page_views()
    assert REPORT_MANAGER.page_views == {
        "/contact.html": {"page views": 3},
        "/home.html": {"page views": 1},
    }


def test_calculate_unique_visits():
    REPORT_MANAGER.calculate_unique_visits()
    assert REPORT_MANAGER.visits == {
        "/contact.html": {
            "visitors": ["12345", "12347", "12348"],
            "visits": 3,
        },
        "/home.html": {"visitors": ["12347"], "visits": 1},
    }
