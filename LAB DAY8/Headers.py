import requests
import json

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Custom headers
headers = {
    "User-Agent": "Python-Requests-App",
    "Accept": "application/json"
}

try:
    # Send GET request
    response = requests.get(url, headers=headers, timeout=5)

    # Raise exception for HTTP errors (4xx / 5xx)
    response.raise_for_status()

    # Parse JSON response
    users = response.json()

    # Extract specific fields
    extracted_data = []
    for user in users:
        extracted_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"]
        })

    # Save extracted data to JSON file
    with open("users_data.json", "w") as file:
        json.dump(extracted_data, file, indent=4)

    print("Data successfully saved to users_data.json")

except requests.exceptions.HTTPError as http_err:
    print("HTTP error occurred:", http_err)

except requests.exceptions.ConnectionError:
    print("Error connecting to the server")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.RequestException as err:
    print("An error occurred:", err)
