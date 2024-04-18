# InteractionScrapy

## Overview
This project is a web scraping tool designed to extract data from the Interaction24 website. The data is then written to a CSV file, a JSON file, and uploaded to a Google Spreadsheet.

## Tools Used
- BeautifulSoup: A Python library used for web scraping purposes to pull the data out of HTML.
- gspread: A Python client library for Google's spreadsheet API.
- oauth2client: A library for OAuth 2.0 in Python to make authenticated requests to the Google Sheets API.
- requests: A simple HTTP library for Python, built for human beings.

## How it Works
1. The script first sends a GET request to the Interaction24 website.
2. It then parses the HTML content of the site using BeautifulSoup.
3. The data of each person is extracted and stored in a `Person` object.
4. These `Person` objects are then written to a CSV file and a JSON file.
5. Finally, the data is uploaded to a Google Spreadsheet using the `gspread` library and Google Sheets API.

## Recommendation for Use
It is recommended to use `poetry` to manage the dependencies of this project, but it is not necessary. The `requirements.txt` file contains all the dependencies needed to run the project.

## Setup
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/AnyoneClown/InteractionScrapy.git
    ```
2. **Install Dependencies:**
    ```bash
    poetry install --no-root
   # or use pip, if you can't use poetry
    pip install -r requirements.txt
    ```
   
3. **Open folder`scraping` and add your service account key file, rename it to `credentials.json`.**

4. **Replace `Interaction24 Team` in the upload_to_spreadsheet function with the name of your Google Spreadsheet.**

5. **Run the Script:**
    ```bash
    python scraping/scrapy.py
    ```
This will start the scraping process and the data will be written to team.csv, team.json, and the specified Google Spreadsheet.

## Note
Please ensure that the Google Spreadsheet is shared with the `client_email` found in your service account JSON key file, and that the service account has the necessary permissions to access and modify the spreadsheet.

## Images
![GoogleSheet File](images/googlesheet.png)
![CSV File](images/csv.png)