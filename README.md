Task & Expense Categorizer Microservice
Overview

This microservice is part of a larger TODO + Budgeting Application.

It is responsible for:

Categorizing expenditures automatically based on description keywords

Organizing tasks by category

Filtering tasks and expenses by a specified category

Returning structured JSON data to the requesting program

This microservice communicates via a REST API and is independently testable.

What This Microservice Does

This microservice:

Accepts tasks and/or expenses as JSON input

Automatically categorizes expenses (e.g., Food, Rent, Transportation, Entertainment)

Groups tasks and expenses by category

Optionally filters results by a specific category

Returns organized data in structured JSON format

This service does not depend on other microservices and runs independently.

How to Run the Microservice
Requirements

Python 3.x

Flask

Install dependencies:

pip install -r requirements.txt

Start the server:

python app.py

The microservice runs on:

http://127.0.0.1:5003
Communication Contract

⚠️ Once defined, this contract must not change.

All teammates must follow this exact format when calling the microservice.

How to Programmatically REQUEST Data
Endpoint
POST /organize
Full URL
http://127.0.0.1:5003/organize
Request Headers
Content-Type: application/json
Request Body Format (JSON)
{
  "tasks": [
    {
      "title": "string",
      "category": "string"
    }
  ],
  "expenses": [
    {
      "description": "string",
      "amount": 0
    }
  ],
  "filter_category": "string (optional)"
}

Request Parameters
Parameter	Type	Required	Description
tasks	JSON array	No	List of task objects
expenses	JSON array	No	List of expense objects
filter_category	string	No	If provided, results are filtered by this category
Example Request (Python)
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
How to Programmatically RECEIVE Data

The microservice returns a JSON response.

Response Format
{
  "status": "success",
  "categorized_data": {
    "CategoryName": {
      "tasks": [...],
      "expenses": [...]
    }
  }
}
Response Fields
Field	Type	Description
status	string	"success" if request processed
categorized_data	JSON object	Grouped tasks and expenses by category
Example Response
{
  "status": "success",
  "categorized_data": {
    "Personal": {
      "tasks": [
        {"title": "Buy groceries", "category": "Personal"}
      ],
      "expenses": [
        {"description": "Walmart", "amount": 75, "category": "Food"}
      ]
    }
  }
}
Expense Categorization Rules

The microservice uses keyword-based categorization:

Keyword	Category
walmart	Food
gas	Transportation
rent	Rent
netflix	Entertainment
other	Other

These rules can be expanded if needed.

UML Sequence Diagram

Below is the sequence of interactions between a test program and the microservice:

Test Program              Task Categorizer Microservice
     |                               |
     | POST /organize (JSON)         |
     |------------------------------->|
     |                               |
     |   Process tasks               |
     |   Categorize expenses         |
     |   Group data                  |
     |                               |
     |<-------------------------------|
     |   Return JSON response        |
     |                               |
Step-by-Step Flow

The test program sends an HTTP POST request to /organize.

The microservice receives and parses JSON data.

Tasks are grouped by category.

Expenses are categorized using keyword rules.

Optional filtering is applied.

The microservice returns structured JSON.

The test program receives and prints the response.

Test Program

A small test program (test_program.py) is included to demonstrate:

How to call the microservice

How to send JSON data

How to receive and print the response

Run:

python test_program.py

This demonstrates independent functionality as required by the assignment.

Microservice Independence

This microservice:

Runs on its own port (5003)

Does not import code from other microservices

Communicates strictly via HTTP

Can be tested independently

Video Demonstration Requirements

The video will show:

The README (scroll slowly)

Running the microservice

Running the test program

Programmatic request being made

Programmatic JSON response being returned

UML sequence diagram explanation

Total video time will not exceed 10 minutes across all microservices.

Team Contributions

Faith Nambasa:

Implemented Task & Expense Categorizer microservice

Wrote Flask API

Defined communication contract

Wrote README documentation

Geetanjali Adhikari:

Assisted with defining categorization rules

Reviewed API structure and request/response contract

Created test program

Designed UML sequence diagram

Collaborated on microservice planning and testing

Notes

This communication contract must remain consistent so that other microservices in the system can reliably interact with this service.