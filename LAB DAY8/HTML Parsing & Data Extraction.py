import requests
from bs4 import BeautifulSoup
import json

# URL to fetch HTML
url = "https://www.python.org"

try:
    # 1. Fetch webpage
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    # 2. Parse HTML using BeautifulSoup with lxml
    soup = BeautifulSoup(response.text, "lxml")

    # 3. Extract page title
    page_title = soup.title.string if soup.title else "No Title Found"

    # Extract all hyperlinks
    links = []
    for a_tag in soup.find_all("a", href=True):
        links.append(a_tag["href"])

    # Extract specific list data (Upcoming Python Events)
    events = []
    events_section = soup.find("div", class_="medium-widget event-widget")

    if events_section:
        for li in events_section.find_all("li"):
            events.append(li.get_text(strip=True))

    # 4. Convert extracted data to JSON format
    extracted_data = {
        "title": page_title,
        "total_links": len(links),
        "links": links[:10],  # limiting for readability
        "events": events
    }

    # 5. Save JSON data to file
    with open("scraped_data.json", "w", encoding="utf-8") as file:
        json.dump(extracted_data, file, indent=4)

    print("HTML data successfully extracted and saved.")

except requests.exceptions.RequestException as e:
    print("Error fetching the webpage:", e)
