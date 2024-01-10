from discord import File
from .command import Command
import json


class CharCommand(Command):
    @staticmethod
    def handle_command(detail):
        if detail is None:
            return "Invalid Command Format", []

        student = CharCommand.get_matching_student(query=detail)

        if student is None:
            return "Char Not Found", []

        message_content = CharCommand.format_student_info(student)

        file = File(f"data/char image/{student['student']}.png")

        return message_content, [file]

    @staticmethod
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

    @staticmethod
    def format_student_info(student):
        if student["variants"]:
            variant_details = ", ".join(student["variants"])
        else:
            variant_details = "None"
        return (
            f"Name: {student['student']}\n"
            f"Rarity: {student['rarity']}*\n"
            f"Role: {student['role']}\n"
            f"Class: {student['class']}\n"
            f"Position: {student['position']}\n"
            f"ATK Type: {student['ATK type']}\n"
            f"DEF Type: {student['DEF type']}\n"
            f"Variants: {variant_details}\n"
        )
