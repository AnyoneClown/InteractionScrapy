import re
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag

from scraping.models import Person

HOME_URL = "https://interaction24.ixda.org/"


def parse_person(soup: Tag) -> Person:
    """
    Parse a person and return a Person object.
    """
    name = soup.select_one("h3").text.strip()
    role = soup.find("div", class_="margin-bottom margin-small").find_all("div")[1].text.strip()
    img = urljoin(HOME_URL, soup.select_one("img").get("src").replace("../", ""))
    linkedin = ""
    twitter = ""
    oestrategy = ""
    for link in soup.select_one("div.speakers-list_social-list").find_all("a"):
        url = link.get("href")
        if re.search("linkedin.com", url):
            linkedin = url
        elif re.search("twitter.com", url):
            twitter = url
        elif re.search("oestrategy.com", url):
            oestrategy = url

        return Person(
            name=name,
            role=role,
            img=img,
            linkedin=linkedin,
            twitter=twitter,
            oestrategy=oestrategy,
        )


def parse_team() -> [Person]:
    """
    Parse the page and return a list of Person objects.
    """
    response = requests.get(HOME_URL)
    soup = BeautifulSoup(response.content, "html.parser")

    speakers = soup.select("div.speakers-list_list.is-4-columns.w-dyn-items div.speakers-list_item.w-dyn-item")

    return [parse_person(speaker) for speaker in speakers]


if __name__ == "__main__":
    start_time = time.perf_counter()
    parse_team()
    end_time = time.perf_counter()
    print("Elapsed:", end_time - start_time)
