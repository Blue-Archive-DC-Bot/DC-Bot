import json


def is_potentially_related(name1, name2):
    if name1 == name2:
        return True

    name_length1 = len(name1.split(" "))
    name_length2 = len(name2.split(" "))

    return name_length1 != name_length2


def is_variant(name, stu):
    if not is_potentially_related(name, stu["student"]):
        return False
    return stu["student"].startswith(name)


def main():
    students_data_file = "data/students.json"
    with open(students_data_file) as f:
        students = json.load(f)

    original_student_names = []

    for stu in students:
        stu["variants"] = []

    for stu in students:
        name = stu["student"]
        other_students = [s for s in students if s != stu]
        is_original = any(is_variant(name, s) for s in other_students)
        if is_original:
            original_student_names.append(name)

    # group students by their original names
    groups = dict()
    for name in original_student_names:
        related_students = [s for s in students if is_variant(name, s)]
        groups[name] = related_students

    # add variants data
    for name in groups:
        for stu in groups[name]:
            variants = [s["student"] for s in groups[name] if s != stu]
            stu["variants"] = variants

    with open(students_data_file, "w") as f:
        json.dump(students, f)


if __name__ == "__main__":
    main()
