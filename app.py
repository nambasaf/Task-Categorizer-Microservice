from flask import Flask, request, jsonify

app = Flask(__name__)

# Supported expense categories
EXPENSE_CATEGORIES = {
    "walmart": "Food",
    "gas": "Transportation",
    "rent": "Rent",
    "netflix": "Entertainment"
}

def categorize_expense(description):
    description_lower = description.lower()
    for keyword, category in EXPENSE_CATEGORIES.items():
        if keyword in description_lower:
            return category
    return "Other"

@app.route("/organize", methods=["POST"])
def organize():
    data = request.get_json()

    tasks = data.get("tasks", [])
    expenses = data.get("expenses", [])
    filter_category = data.get("filter_category")

    categorized_data = {}

    # Process tasks
    for task in tasks:
        category = task.get("category", "Uncategorized")
        categorized_data.setdefault(category, {"tasks": [], "expenses": []})
        categorized_data[category]["tasks"].append(task)

    # Process expenses
    for expense in expenses:
        description = expense.get("description", "")
        category = categorize_expense(description)
        categorized_data.setdefault(category, {"tasks": [], "expenses": []})
        expense["category"] = category
        categorized_data[category]["expenses"].append(expense)

    # Apply filter if requested
    if filter_category:
        filtered = categorized_data.get(filter_category, {"tasks": [], "expenses": []})
        return jsonify({
            "status": "success",
            "categorized_data": {filter_category: filtered}
        })

    return jsonify({
        "status": "success",
        "categorized_data": categorized_data
    })


if __name__ == "__main__":
    app.run(port=5003, debug=True)