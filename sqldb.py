import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234srimay',
        database='giet'
    )

    if connection.is_connected():
        print("Successfully connected to MySQL database")

        cursor = connection.cursor()

        def run_query(title, query):
            print(f"\n--- {title} ---")
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("------")

        # Previous Queries
        run_query("All Data", "SELECT * FROM giet")
        run_query("Only Names", "SELECT name FROM giet")
        run_query("Name and Address", "SELECT name, address FROM giet")
        run_query("Roll and Salary", "SELECT roll, salary FROM giet")
        run_query("Name = aman", "SELECT * FROM giet WHERE name = 'aman'")

        run_query("Employees in Delhi", "SELECT * FROM giet WHERE address = 'delhi'")
        run_query("Male Employees", "SELECT * FROM giet WHERE gender = 'M'")
        run_query("Doctors", "SELECT * FROM giet WHERE desig = 'doctor'")
        run_query("Salary = 15000", "SELECT * FROM giet WHERE salary = 15000")
        run_query("Salary > 20000", "SELECT * FROM giet WHERE salary > 20000")
        run_query("Salary < 30000", "SELECT * FROM giet WHERE salary < 30000")
        run_query("Male with Salary > 20000", "SELECT * FROM giet WHERE gender = 'M' AND salary > 20000")
        run_query("Female OR in Raipur", "SELECT * FROM giet WHERE gender = 'F' OR address = 'raipur'")
        run_query("Name starts with 'a'", "SELECT * FROM giet WHERE name LIKE 'a%'")
        run_query("Name ends with 'h'", "SELECT * FROM giet WHERE name LIKE '%h'")
        run_query("Address contains 'pur'", "SELECT * FROM giet WHERE address LIKE '%pur%'")
        run_query("Sorted by Name (ASC)", "SELECT * FROM giet ORDER BY name ASC")
        run_query("Sorted by Salary (DESC)", "SELECT * FROM giet ORDER BY salary DESC")
        run_query("Total Employees", "SELECT COUNT(*) FROM giet")
        run_query("Total Male Employees", "SELECT COUNT(*) FROM giet WHERE gender = 'M'")

        cursor.close()
        connection.close()
        print("\nConnection closed")

except Error as e:
    print("Error:", e)