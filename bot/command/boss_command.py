from .command import Command
from discord import File
import json


class BossCommand(Command):
    @staticmethod
    def handle_command(detail):
        if detail is None:
            return "Invalid Command Format", []

        boss = BossCommand.get_matching_boss(query=detail)

        if boss is None:
            return "Boss Not Found", []

        message_content = BossCommand.format_boss_info(boss)
        boss_image_file = File(f"data/boss image/{boss['name']}.png")

        return message_content, [boss_image_file]

    @staticmethod
    def get_matching_boss(query):
        with open("data/boss.json") as f:
            bosses = json.load(f)

        matched = []

        for boss in bosses:
            if boss["name"].lower().startswith(query):
                matched.append(boss)

        if len(matched) == 0:
            return None

        return min(matched, key=lambda b: len(b["name"]))

    @staticmethod
    def format_boss_info(boss):
        return (
            f"Name: {boss['name']}\n"
            f"Faction: {boss['faction']}\n"
            f"Profile:\n"
            f"{boss['profile']}"
        )
