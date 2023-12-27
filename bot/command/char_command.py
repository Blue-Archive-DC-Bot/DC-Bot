from discord import File
import json


def handle_char_command(detail):
    with open("data/students.json") as f:
        students = json.load(f)

    for data in students:
        if data["student"].lower() != detail:
            continue
        variants = data["variants"]
        has_variants = len(variants) > 0
        message_content = f"""Name: {data['student']}
Rarity: {data['rarity']}*
Role: {data['role']}
Class: {data['class']}
Position: {data['position']}
ATK Type: {data['ATK type']}
DEF Type: {data['DEF type']}
Variants: {', '.join(variants) if has_variants else 'None'}
        """

        file = File(f"data/char image/{data['student']}.png")

        return message_content, [file]

    return "Char Not Found", []
