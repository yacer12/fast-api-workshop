# File: data/generate_expenses.py
import random
import json
from datetime import datetime, timedelta
from pymongo import MongoClient
from uuid import uuid4

_MONGO_SERVER = "mongodb://localhost:27017/"
def generate_sample_expense(num_of_expenses=150):
    user_ids = ["Frodo", "Sam", "Gandalf", "Aragorn", "Legolas", "Gimli", "Boromir",
                 "Pippin", "Merry", "Saruman", "Sauron", "Galadriel", "Elrond", "Gollum", "Bilbo", 
                 "Thorin", "Bard", "Bard", "Thranduil", "Balin", "Dwalin"]
    
    categories = ["Food", "Transportation", "Utilities", "Entertainment", "Healthcare"]
    payment_methods = ["Credit Card", "Cash", "Bank Transfer", "Mobile Payment"]

    expenses = []
    for _ in range(num_of_expenses):
        expense =  {
            "expense_id": str(uuid4()),
            "user_id": random.choice(user_ids),
            "amount": round(random.uniform(5.0, 2500.0), 2),
            "category": random.choice(categories),
            "description": random.choice(
                [None, "Monthly subscription", "Dinner with friends", "Grocery shopping", 
                 "Medication", "Movie tickets", "Transportation fare"]
            ),
            "date": (datetime.utcnow() - timedelta(days=random.randint(0, 90))).isoformat(),
            "payment_method": random.choice(payment_methods),
            "recurring": random.choice([True, False]),
        }
        expenses.append(expense)

    # Save to a JSON file in the `data` folder
    output_file = "sample_expenses.json"
    with open(output_file, "w+") as f:
        json.dump(expenses, f, indent=4)

    print(f"Generated {num_of_expenses} sample expenses and saved to {output_file}")

def write_to_mongodb(data, db_name="expensesDB", collection_name="expenseDetails", chunk_size=100):
    """
    Writes bulk data to a MongoDB collection.

    Args:
        data (list): A list of dictionaries representing the data to insert.
        db_name (str): The name of the MongoDB database.
        collection_name (str): The name of the MongoDB collection.
        chunk_size (int): The number of documents to insert in each batch.
    """
    try:
        # Connect to MongoDB
        client = MongoClient(_MONGO_SERVER)
        db = client[db_name]
        collection = db[collection_name]
         # Check if the collection exists and remove it
        if collection_name in db.list_collection_names():
            collection.drop()
            print(f"Collection '{collection_name}' already exists. Dropped the collection.")
      # Insert data in chunks
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i + chunk_size]
            result = collection.insert_many(chunk)
            print(f"Inserted {len(result.inserted_ids)} records into MongoDB collection '{collection_name}' in  \
                  database '{db_name}' (chunk {i // chunk_size + 1}).")

        # Create indexes
        collection.create_index([("user_id", 1)])  # Ascending index for user_id
        collection.create_index([("expense_id", 1)])  # Ascending index for expense_id
        print(f"Created indexes on 'user_id' and 'expense_id' for collection '{collection_name}'.")
    except Exception as e:
        print(f"An error occurred while writing to MongoDB: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    num_of_expenses = 1000
    # Generate sample expenses
    generate_sample_expense(num_of_expenses=num_of_expenses)
    sample_expenses = [] 
    with open("sample_expenses.json") as json_file:
        sample_expenses = json.load(json_file)
    if sample_expenses:
        # Write the generated sample expenses to MongoDB, keeping the default database and collection names and using a chunk size of 100
        write_to_mongodb(sample_expenses, chunk_size=100)