import json
from urllib.request import urlopen

from bs4 import BeautifulSoup

MAL_USERNAME = "abhineeth"
INFO_FILE = "info.json"


def scrape_top_ten():
    base = f"https://myanimelist.net/profile/{MAL_USERNAME}"

    soup = BeautifulSoup(urlopen(base), "html.parser")
    anime_names = []
    for row in soup.select("#anime_favorites li.btn-fav"):
        title = row.select_one("a .title")
        if title:
            anime_names.append(title.get_text(strip=True))

    return anime_names


def main():
    print("Scraping MyAnimeList...")
    anime_names = scrape_top_ten()

    with open(INFO_FILE, "w", encoding="utf-8") as file:
        json.dump({"anime": anime_names}, file, ensure_ascii=False, indent=2)
        file.write("\n")

    print("Anime names updated in info.json.")


if __name__ == "__main__":
    main()
