from dataclasses import fields
from typing import NoReturn

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from scraping.models import Person


def upload_to_spreadsheet(data: [Person], json_file_path: str, spreadsheet_name: str) -> NoReturn:
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(json_file_path, scope)
    client = gspread.authorize(creds)

    sheet = client.open(spreadsheet_name).sheet1
    headers = [field.name.capitalize() for field in fields(Person)]

    sheet.append_row(headers)
    for person in data:
        person_list = [person.name, person.role, person.img, person.linkedin, person.twitter, person.other_link]
        sheet.append_row(person_list)
