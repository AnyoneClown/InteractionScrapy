import csv
import json
import re
import time
from dataclasses import fields
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag

from scraping.models import Person
from scraping.spreadsheet import upload_to_spreadsheet

HOME_URL = "https://interaction24.ixda.org/"


def parse_person(soup: Tag) -> Person:
    """
    Parse a person and return a Person object.
    """
    name = soup.select_one("h3").text.strip()
    role = soup.find("div", class_="margin-bottom margin-small").find_all("div")[1].text.strip()
    img = urljoin(HOME_URL, soup.select_one("img").get("src").replace("../", ""))
    linkedin = None
    twitter = None
    other = None

    for link in soup.select_one("div.speakers-list_social-list").find_all("a"):
        url = link.get("href")
        if re.search("linkedin.com", url):
            linkedin = url
        elif re.search("twitter.com", url):
            twitter = url
        elif url != "index.html#":
            other = url

    return Person(
        name=name,
        role=role,
        img=img,
        linkedin=linkedin,
        twitter=twitter,
        other_link=other,
    )


def parse_team() -> [Person]:
    """
    Parse the page and return a list of Person objects.
    """
    response = requests.get(HOME_URL)
    soup = BeautifulSoup(response.content, "html.parser")

    speakers = soup.select("div.speakers-list_list.is-4-columns.w-dyn-items div.speakers-list_item.w-dyn-item")

    return [parse_person(speaker) for speaker in speakers]


def write_data_to_csv(people: [Person], filename: str = "team.csv"):
    """
    Write the data to a CSV file.
    """
    with open(filename, "w", newline="") as csvfile:
        fieldnames = [field.name for field in fields(Person)]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for person in people:
            writer.writerow(person.__dict__)


def write_data_to_json(people: [Person], filename: str = "team.json"):
    with open(filename, "w") as jsonfile:
        json.dump([person.__dict__ for person in people], jsonfile)


if __name__ == "__main__":
    start_time = time.perf_counter()

    people = parse_team()
    write_data_to_csv(people)
    write_data_to_json(people)
    upload_to_spreadsheet(people, "credentials.json", "Interaction24 Team")

    end_time = time.perf_counter()
    print("Elapsed:", end_time - start_time)
