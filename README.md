# Task & Expense Categorizer Microservice

---

## 1. Overview

This microservice is part of a larger **TODO + Budgeting Application**.

It is responsible for:

- Categorizing expenditures automatically based on description keywords  
- Organizing tasks by category  
- Filtering tasks and expenses by a specified category  
- Returning structured JSON data to the requesting program  

This microservice communicates via a **REST API** and is independently testable.

---

## 2. What This Microservice Does

This microservice:

- Accepts tasks and/or expenses as JSON input  
- Automatically categorizes expenses (e.g., Food, Rent, Transportation, Entertainment)  
- Groups tasks and expenses by category  
- Optionally filters results by a specific category  
- Returns organized data in structured JSON format  

This service does **not** depend on other microservices and runs independently.

---

## 3. How to Run the Microservice

### 3.1 Requirements

- Python 3.x  
- Flask  

### 3.2 Install Dependencies

```bash
pip install -r requirements.txt
```

### 3.3 Start the Server

```bash
python app.py
```

### 3.4 Server Address

The microservice runs on:

```
http://127.0.0.1:5003
```

---

## 4. Communication Contract

⚠️ **Once defined, this contract must not change.**  
All teammates must follow this exact format when calling the microservice.

---

## 5. How to Programmatically REQUEST Data

### 5.1 Endpoint

```
POST /organize
```

### 5.2 Full URL

```
http://127.0.0.1:5003/organize
```

### 5.3 Request Headers

```
Content-Type: application/json
```

### 5.4 Request Body Format (JSON)

```json
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
```

### 5.5 Request Parameters

| Parameter        | Type        | Required | Description |
|------------------|------------|----------|-------------|
| tasks            | JSON array | No       | List of task objects |
| expenses         | JSON array | No       | List of expense objects |
| filter_category  | string     | No       | Filters results by this category |

---

### 5.6 Example Request (Python)

```python
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
```

---

## 6. How to Programmatically RECEIVE Data

The microservice returns a JSON response.

### 6.1 Response Format

```json
{
  "status": "success",
  "categorized_data": {
    "CategoryName": {
      "tasks": [...],
      "expenses": [...]
    }
  }
}
```

### 6.2 Response Fields

| Field             | Type        | Description |
|------------------|------------|-------------|
| status           | string     | "success" if request processed correctly |
| categorized_data | JSON object | Grouped tasks and expenses by category |

---

### 6.3 Example Response

```json
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
```

---

## 7. Expense Categorization Rules

The microservice uses keyword-based categorization:

| Keyword  | Category        |
|----------|----------------|
| walmart  | Food           |
| gas      | Transportation |
| rent     | Rent           |
| netflix  | Entertainment  |
| other    | Other          |

These rules can be expanded if needed.

---

## 8. UML Sequence Diagram

### 8.1 Interaction Diagram

```
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
```

### 8.2 Step-by-Step Flow

1. The test program sends an HTTP POST request to `/organize`.  
2. The microservice receives and parses JSON input.  
3. Tasks are grouped by category.  
4. Expenses are categorized using keyword rules.  
5. Optional filtering is applied.  
6. The microservice returns structured JSON.  
7. The test program receives and prints the response.

---

## 9. Test Program

A small test program (`test_program.py`) demonstrates:

- Programmatic request to the microservice  
- JSON data being sent  
- JSON response being received  

Run:

```bash
python test_program.py
```

This confirms the microservice functions independently.

---

## 10. Microservice Independence

This microservice:

- Runs on its own port (5003)  
- Does not import code from other microservices  
- Communicates strictly via HTTP  
- Can be tested independently  

---

## 11. Video Demonstration Structure

The video will show:

1. Scrolling through this README  
2. Running the microservice  
3. Running the test program  
4. Programmatic request being made  
5. JSON response being returned  
6. UML sequence explanation  

Total video duration will not exceed **10 minutes** across all microservices.

---

## 12. Team Contributions

### Faith Nambasa

- Implemented Task & Expense Categorizer microservice  
- Developed Flask API  
- Defined communication contract  
- Created test program  
- Designed UML sequence diagram  
- Wrote README documentation  

### Geetanjali Adhikari

- Assisted in defining categorization rules  
- Reviewed API structure and request/response format  
- Collaborated on testing and validation  

---

## 13. Notes

This communication contract must remain consistent so that other microservices in the system can reliably interact with this service.
