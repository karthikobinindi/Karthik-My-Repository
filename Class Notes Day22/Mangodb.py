from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create / switch database
db = client["mydatabase"]

# Create / switch collection
collection = db["students"]

# Insert data
collection.insert_one({
    "name": "Karthik",
    "age": 22,
    "course": "Python"
})

print("Collection created and data inserted")
