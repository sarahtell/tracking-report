from datetime import datetime
from tracker import Tracker

def strip_and_replace_in_line(line):
    return [x.replace("\n", "").strip() for x in line]


def remove_spaces_in_line(line):
    return [x for x in line if x]


def parse_line(line):
    splitted_line = line.split("|")
    stripped_line_replaced = strip_and_replace_in_line(splitted_line)
    date_string, url, user_id = remove_spaces_in_line(stripped_line_replaced)
    return [datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S%Z"), url, user_id]


def read_file(file_name):
    try:
        with open(file_name) as f:
            # i != 0 since we don't want to include the top row of log.txt.
            return [parse_line(line) for i, line in enumerate(f) if i != 0]
    except FileNotFoundError as e:
        e.strerror = "File does not exist!"
        raise e


def main():
    logs = read_file("log.txt")  # => [[],[],...,[]]

    tracker = Tracker(logs)

    tracker.filter_rows_by_date_range()

    tracker.calculate_page_views()

    tracker.calculate_unique_visits()


if __name__ == "__main__":
    main()
