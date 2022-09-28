import argparse
from parser import parse_line, set_time_format


def get_user_input():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--startdate",
        required=True,
        help='input the start date (UTC) of the time range on format "YYYY-MM-DD HH:MM:SS"',
    )
    parser.add_argument(
        "--enddate",
        required=True,
        help='input the end date (UTC) of the time range on format "YYYY-MM-DD HH:MM:SS"',
    )
    parser.add_argument(
        "--filepath",
        required=True,
        help="input the path to the file containing the tracking data",
    )

    args = parser.parse_args()

    return args.startdate, args.enddate, args.filepath


def validate_date_input(startdate, enddate):

    try:
        date_time_start = set_time_format(startdate, "%Y-%m-%d %H:%M:%S")
        date_time_end = set_time_format(enddate, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print('"Date should have the correct format: "YYYY-MM-DD HH:MM:SS"')
        exit()

    if date_time_end < date_time_start:
        print("End date cannot be earlier than start date!")
        exit()

    return date_time_start, date_time_end



def read_file(file_name):
    try:
        with open(file_name) as f:
            # i != 0 since we don't want to include the top row of log.txt.
            return [parse_line(line) for i, line in enumerate(f) if i != 0]
    except FileNotFoundError:
        print("File does not exist!")
        exit()
