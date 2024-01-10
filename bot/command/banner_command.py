import json
from datetime import datetime
from .command import Command


class BannerCommand(Command):
    @staticmethod
    def handle_command(_):
        banners = BannerCommand.load_banner_data()
        banners = BannerCommand.filter_past_banner(banners)
        output_string = BannerCommand.format_output(banners)

        return output_string, []

    @staticmethod
    def load_banner_data():
        BANNER_FILE = "data/banners.json"

        with open(BANNER_FILE) as f:
            banners = json.load(f)
            for b in banners:
                b["date"] = datetime.strptime(b["date"], "%Y-%b-%d")

        return banners

    @staticmethod
    def filter_past_banner(banners):
        current_time = datetime.now()
        past_banners = [b for b in banners if b["date"] <= current_time][:-1]
        current_banners = banners[len(past_banners) :]

        return current_banners

    @staticmethod
    def students_to_string(students):
        student_strings = []
        for s in students:
            string = f"{s['name']} ({', '.join(s['remarks'])})"
            student_strings.append(string)

        return ", ".join(student_strings)

    @staticmethod
    def format_output(banners):
        # limit output to 3 banners only
        banners = banners[:3]
        banner_strings = []

        for b in banners:
            start_date = b["date"].strftime("%d-%b-%Y")
            students = b["students"]
            banner_string = (
                f"Start Date: {start_date}\n"
                f"students: {BannerCommand.students_to_string(students)}\n"
            )
            banner_strings.append(banner_string)

        return "\n".join(banner_strings)
