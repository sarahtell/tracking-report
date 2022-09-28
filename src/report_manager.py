from tabulate import tabulate


class ReportManager:
    def __init__(self, logs, date_time_start, date_time_end) -> None:
        self.logs = logs
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        self.date_time_parsed = []
        self.page_views = {}
        self.visits = {}


    def filter_rows_by_date_range(self):
        for date_time, url, user_id in self.logs:
            if self.date_time_start <= date_time <= self.date_time_end:
                self.date_time_parsed.append([date_time, url, user_id])
        return self.date_time_parsed


    def calculate_page_views(self, logs):
        for _, url, _ in logs:
            if url not in self.page_views.keys():
                self.page_views[url] = {"page views": 1}
            else:
                self.page_views[url]["page views"] += 1
        return self.page_views


    def calculate_unique_visits(self, logs):
        for _, url, user_id in logs:
            if url not in self.visits.keys():
                self.visits[url] = {"visitors": [user_id], "visits": 1}
            else:
                if user_id not in self.visits[url]["visitors"]:
                    self.visits[url]["visitors"].append(user_id)
                    self.visits[url]["visits"] += 1
        return self.visits


    def make_report(self):
        report_lists = []
        for url in self.page_views.keys():
            report_lists.append(
                [url, self.page_views[url]["page views"], self.visits[url]["visits"]]
            )

        table = tabulate(
            report_lists,
            headers=["url", "page views", "visitors"],
            tablefmt="youtrack",
            numalign="left",
        )

        print(table.replace("||", "|"))
