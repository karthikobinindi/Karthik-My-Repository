import mysql.connector

def mysql_operations():
    print("\n--- MySQL Operations ---")

    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",       # change if needed
            password="root123",   # change if needed
            database="employee"
        )

        cursor = conn.cursor()

        # 1️⃣ Fetch employees with salary > 50000
        cursor.execute("SELECT * FROM employees WHERE salary > 50000")
        employees = cursor.fetchall()

        print("Employees with salary > 50000:")
        for emp in employees:
            print(emp)

        # 2️⃣ Insert new employee
        insert_query = """
        INSERT INTO employees (name, department, salary)
        VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, ("Karthik", "IT", 60000))
        conn.commit()
        print("MySQL: Employee inserted")

        # 3️⃣ Update salary by 10% for employee id = 1
        update_query = """
        UPDATE employees
        SET salary = salary * 1.10
        WHERE id = %s
        """
        cursor.execute(update_query, (1,))
        conn.commit()
        print("MySQL: Salary updated")

        cursor.close()
        conn.close()

    except Exception as e:
        print("MySQL Error:", e)
