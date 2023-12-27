import json


def get_first_name(name):
    return name.split(" ")[0]


def main():
    students_data_file = "data/students.json"
    with open(students_data_file) as f:
        students = json.load(f)

    # reset variant data
    for stu in students:
        stu["variants"] = []

    # group students by their first names
    groups = dict()
    for stu in students:
        first_name = get_first_name(stu["student"])

        if first_name not in groups:
            groups[first_name] = []
        groups[first_name].append(stu)

    # add variants data
    for group in groups.values():
        for stu in group:
            variants = [s["student"] for s in group if s != stu]
            stu["variants"] = variants

    with open(students_data_file, "w") as f:
        json.dump(students, f)


if __name__ == "__main__":
    main()
