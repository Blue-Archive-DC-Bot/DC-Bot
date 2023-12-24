from discord import File
import json


def clean_command_details(detail):
    return " ".join(detail.split())


def handle_char_command(detail):
    detail = clean_command_details(detail)
    with open("data/students.json") as f:
        students = json.load(f)

    for data in students:
        if data["student"].lower() != detail:
            continue
        message_content = f"""Name: {data['student']}
Rarity: {data['rarity']}*
Role: {data['role']}
Class: {data['class']}
Position: {data['position']}
ATK Type: {data['ATK type']}
DEF Type: {data['DEF type']}
        """

        file = File(f"data/char image/{data['student']}.png")

        return message_content, [file]

    return "Char Not Found", []


def get_response(content):
    """
    Returns message content, list of files to send
    """
    DEFAULT_RESPONSE = ("Invalid Command", [])

    content = content.lower()
    splitted = content.split(" ", 1)
    if len(splitted) < 2:
        return DEFAULT_RESPONSE

    command, detail = splitted

    match command:
        case "char":
            return handle_char_command(detail)
        case _:
            return DEFAULT_RESPONSE
