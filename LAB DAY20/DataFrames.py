import pandas as pd

# Create the DataFrame
data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)

# 1. Filter all employees from the IT department
it_employees = df[df["Department"] == "IT"]

# 2. Find the average salary per department
avg_salary_per_dept = df.groupby("Department")["Salary"].mean()

# 3. Add a new column Salary_Adjusted (10% increase)
df["Salary_Adjusted"] = df["Salary"] * 1.10

# Print results
print("IT Department Employees:")
print(it_employees)

print("\nAverage Salary per Department:")
print(avg_salary_per_dept)

print("\nFinal DataFrame with Salary_Adjusted:")
print(df)
