# File: data/generate_expenses.py
import random
import json
from datetime import datetime, timedelta
from expense import Expense

def generate_sample_expense():
    categories = ["Food", "Transportation", "Utilities", "Entertainment", "Healthcare"]
    payment_methods = ["Credit Card", "Cash", "Bank Transfer", "Mobile Payment"]
    
    return {
        "user_id": f"user_{random.randint(1, 50)}",
        "amount": round(random.uniform(5.0, 500.0), 2),
        "category": random.choice(categories),
        "description": random.choice(
            [None, "Monthly subscription", "Dinner with friends", "Grocery shopping"]
        ),
        "date": (datetime.utcnow() - timedelta(days=random.randint(0, 365))).isoformat(),
        "payment_method": random.choice(payment_methods),
        "recurring": random.choice([True, False]),
    }

# Generate 150 sample records
sample_expenses = [generate_sample_expense() for _ in range(150)]

# Save to a JSON file in the `data` folder
output_file = "data/sample_expenses.json"
with open(output_file, "w") as f:
    json.dump(sample_expenses, f, indent=4)

print(f"Generated 150 sample expenses and saved to {output_file}")