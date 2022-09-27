from datetime import datetime
from tracker import Tracker
import argparse


def set_time_format(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S%Z")


def strip_and_replace_in_line(line):
    return [x.replace("\n", "").strip() for x in line]


def remove_spaces_in_line(line):
    return [x for x in line if x]


def parse_line(line):
    splitted_line = line.split("|")
    stripped_line_replaced = strip_and_replace_in_line(splitted_line)
    date_string, url, user_id = remove_spaces_in_line(stripped_line_replaced)
    return [set_time_format(date_string), url, user_id]


def read_file(file_name):
    try:
        with open(file_name) as f:
            # i != 0 since we don't want to include the top row of log.txt.
            return [parse_line(line) for i, line in enumerate(f) if i != 0]
    except FileNotFoundError:
        print("File does not exist!")
        exit()


def get_user_input():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--startdate",
        required=True,
        help="input the start date of the time range on format YYYY-MM-DD HH:MM:SS",
    )
    parser.add_argument(
        "--enddate",
        required=True,
        help="input the end date of the time range on format YYYY-MM-DD HH:MM:SS",
    )
    parser.add_argument(
        "--filepath",
        required=True,
        help="input the path to the file containing the tracking data",
    )

    args = parser.parse_args()

    return args.startdate, args.enddate, args.filepath


def main():

    startdate, enddate, filepath = get_user_input()

    logs = read_file(filepath)

    tracker = Tracker(
        logs,
        date_time_start=set_time_format(startdate),
        date_time_end=set_time_format(enddate),
    )

    date_time_parsed_log = tracker.filter_rows_by_date_range()

    tracker.calculate_page_views(date_time_parsed_log)

    tracker.calculate_unique_visits(date_time_parsed_log)

    tracker.make_report()


if __name__ == "__main__":
    main()
