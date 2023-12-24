import requests
from bs4 import BeautifulSoup
import json

URL = "https://bluearchive.fandom.com/wiki/Category:Students"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)
content = soup.find("div", id="content")
content_table = content.find("table", class_="article-table")
table_body = content_table.tbody
rows = table_body.find_all("tr")[1:]

students_data = []
for row in rows:
    # cells from first to last are:
    # Student, Rarity, Role, Class, Position, Cover, Atk, Def
    cells = row.find_all("td")
    data = dict()

    # Parse get student name
    student_cell = cells[0]
    student_img_element = student_cell.find("img")
    data["student"] = student_img_element.get("alt")
    data["student"] = " ".join(data["student"].split(" ")[:-1])
    student_img_src = student_img_element.get("data-src")
    response = requests.get(student_img_src)

    with open(f"../data/char image/{data['student']}.png", "wb") as f:
        f.write(response.content)

    # Parse rarity
    rarity_cell = cells[1]
    data["rarity"] = len(rarity_cell.find_all("a"))

    # Parse Role
    role_cell = cells[2]
    data["role"] = role_cell.find("b").text

    # Parse Class
    class_cell = cells[3]
    data["class"] = class_cell.find("img").get("alt")

    # Parse Position
    position_cell = cells[4]
    data["position"] = position_cell.find("img").get("alt")
    data["position"] = data["position"].lower().capitalize()

    # Parse Cover
    cover_cell = cells[5]
    cover_img_alt = cover_cell.find("img").get("alt")
    data["cover"] = True if cover_img_alt == "Cover" else False

    # Parse Atk Type
    atk_cell = cells[6]
    data["ATK type"] = atk_cell.find("b").text

    # Parse Def Type
    def_cell = cells[7]
    data["DEF type"] = def_cell.find("b").text

    students_data.append(data)

for i in range(10):
    print(students_data[i])

with open("../data/students.json", "w") as f:
    json.dump(students_data, f)
