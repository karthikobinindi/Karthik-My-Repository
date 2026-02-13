from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

db = client["company_db"]
collection = db["employees"]

# ---------------------------------------------------
# 1️⃣ Insert a new employee document
# ---------------------------------------------------
employee = {
    "name": "Karthik",
    "department": "IT",
    "salary": 100000
}

collection.insert_one(employee)
print("Employee inserted")

# ---------------------------------------------------
# 2️⃣ Find all employees in IT department
# ---------------------------------------------------
print("Employees in IT department:")
for emp in collection.find({"department": "IT"}):
    print(emp)

# ---------------------------------------------------
# 3️⃣ Update salary of employee by name
# (example: name = 'Anita')
# ---------------------------------------------------
collection.update_one(
    {"name": "Anita"},
    {"$set": {"salary": 75000}}
)

print("Salary updated")

client.close()
