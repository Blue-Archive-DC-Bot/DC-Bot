import json
import requests

SOURCE_URL = "https://schale.gg/data/en/raids.json"
BASE_IMAGE_URL = "https://schale.gg/images/raid/Boss_Portrait_{}_Lobby.png"


def main():
    response = requests.get(SOURCE_URL)

    if response is None:
        print("Unknown Error Occured")
        return

    data = response.json()
    raid_bosses = data["Raid"]
    bosses_data = []

    for data in raid_bosses:
        formatted_data = {
            "name": data["Name"],
            "faction": data["Faction"],
            "profile": data["Profile"],
        }

        image_url = BASE_IMAGE_URL.format(data["PathName"])
        response = requests.get(image_url)
        boss_image = response.content
        image_filename = f'data/boss image/{data["Name"]}.png'

        with open(image_filename, "wb") as f:
            f.write(boss_image)

        bosses_data.append(formatted_data)

    with open("data/boss.json", "w") as f:
        json.dump(bosses_data, f)


if __name__ == "__main__":
    main()
