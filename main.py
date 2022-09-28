from input import get_user_input, read_file, validate_date_input
from report_manager import ReportManager


def main():

    startdate, enddate, filepath = get_user_input()

    date_time_start, date_time_end = validate_date_input(startdate, enddate)

    logs = read_file(filepath)

    report_manager = ReportManager(
        logs,
        date_time_start,
        date_time_end,
    )

    report_manager.filter_rows_by_date_range()

    report_manager.calculate_page_views()

    report_manager.calculate_unique_visits()

    report_manager.make_report()


if __name__ == "__main__":
    main()
