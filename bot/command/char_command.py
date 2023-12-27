from discord import File
import json


def get_matching_student(query):
    """
    Return student where query is a prefix of the students name.
    If there are multiple, return the student with shortest name.
    Otherwise returns None.
    """
    with open("data/students.json") as f:
        students = json.load(f)

    matched = []

    for stu in students:
        if stu["student"].lower().startswith(query):
            matched.append(stu)

    if len(matched) == 0:
        return None

    return min(matched, key=lambda s: len(s["student"]))


def handle_char_command(detail):
    student = get_matching_student(query=detail)

    if student is None:
        return "Char Not Found", []

    variants = student["variants"]
    has_variants = len(variants) > 0
    message_content = f"""Name: {student['student']}
Rarity: {student['rarity']}*
Role: {student['role']}
Class: {student['class']}
Position: {student['position']}
ATK Type: {student['ATK type']}
DEF Type: {student['DEF type']}
Variants: {', '.join(variants) if has_variants else 'None'}
    """

    file = File(f"data/char image/{student['student']}.png")

    return message_content, [file]
