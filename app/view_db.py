
# view_db.py
import sqlite3

def view_table(table_name):
    connection = sqlite3.connect('cybersecurity.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()

if __name__ == "__main__":
    table_name = input("Enter the table name to view: ")
    view_table(table_name)
