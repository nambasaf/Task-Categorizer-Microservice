import requests

url = "http://127.0.0.1:5003/organize"

payload = {
    "tasks": [
        {"title": "Study CS361", "category": "Work"},
        {"title": "Buy groceries", "category": "Personal"}
    ],
    "expenses": [
        {"description": "Walmart", "amount": 75},
        {"description": "Gas", "amount": 40}
    ],
    "filter_category": "Personal"
}

response = requests.post(url, json=payload)

print(response.json())