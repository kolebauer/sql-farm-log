import sqlite3 

# Connect to (or create) the SQLite database
conn = sqlite3.connect("farm_logs.db")
cursor = conn.cursor()

# Create the main table for storing farm logs
cursor.execute("""
CREATE TABLE IF NOT EXISTS farm_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    field_name TEXT NOT NULL,
    date TEXT NOT NULL,
    activity TEXT NOT NULL,
    notes TEXT
)
""")
conn.commit()

# Function to add a new farm log to the database
def add_log():
    print("\nAdd New Farm Log")
    field = input("Enter field name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    activity = input("Enter activity (e.g., Planting, Spraying): ")
    notes = input("Enter notes: ")

    cursor.execute("""
        INSERT INTO farm_logs (field_name, date, activity, notes)
        VALUES (?, ?, ?, ?)
    """, (field, date, activity, notes))
    conn.commit()
    print("Log entry added.")

# Function to view all existing logs
def view_logs():
    print("\nAll Farm Logs:")
    cursor.execute("SELECT * FROM farm_logs")
    rows = cursor.fetchall()

    if not rows:
        print("No logs found.")
        return

    for row in rows:
        print(f"ID: {row[0]} | Field: {row[1]} | Date: {row[2]} | Activity: {row[3]} | Notes: {row[4]}")

# Function to update the activity and/or notes of an existing log
def update_log():
    id = input("Enter the ID of the log you want to update: ")
    new_activity = input("Enter new activity (leave blank to keep current): ")
    new_notes = input("Enter new notes (leave blank to keep current): ")

    if new_activity:
        cursor.execute("UPDATE farm_logs SET activity = ? WHERE id = ?", (new_activity, id))
    if new_notes:
        cursor.execute("UPDATE farm_logs SET notes = ? WHERE id = ?", (new_notes, id))

    conn.commit()
    print("Log updated.")

# Function to delete a log by its ID
def delete_log():
    id = input("Enter the ID of the log to delete: ")
    confirm = input(f"Are you sure you want to delete log ID {id}? (y/n): ")
    if confirm.lower() == "y":
        cursor.execute("DELETE FROM farm_logs WHERE id = ?", (id,))
        conn.commit()
        print("Log deleted.")
    else:
        print("Delete canceled.")

# Function to view logs filtered by a specific field name
def view_by_field():
    field = input("Enter field name to search: ")
    cursor.execute("SELECT * FROM farm_logs WHERE field_name = ?", (field,))
    rows = cursor.fetchall()

    if not rows:
        print("No logs found for that field.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Field: {row[1]} | Date: {row[2]} | Activity: {row[3]} | Notes: {row[4]}")

# Function to view logs filtered by a specific activity
def view_by_activity():
    activity = input("Enter activity to search (e.g., Harvest): ")
    cursor.execute("SELECT * FROM farm_logs WHERE activity = ?", (activity,))
    rows = cursor.fetchall()

    if not rows:
        print("No logs found for that activity.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Field: {row[1]} | Date: {row[2]} | Activity: {row[3]} | Notes: {row[4]}")

# Function to view logs between two dates
def logs_by_date_range():
    start = input("Start date (YYYY-MM-DD): ")
    end = input("End date (YYYY-MM-DD): ")
    cursor.execute("SELECT * FROM farm_logs WHERE date BETWEEN ? AND ?", (start, end))
    rows = cursor.fetchall()

    if not rows:
        print("No logs found in this date range.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Field: {row[1]} | Date: {row[2]} | Activity: {row[3]} | Notes: {row[4]}")

# # Function to show a count of logs by activity type (**Update later with addition of equipment maintenance logging, crop storage, head counts for livestock, etc.)
# def activity_summary():
#     cursor.execute("SELECT activity, COUNT(*) FROM farm_logs GROUP BY activity")
#     rows = cursor.fetchall()

#     print("\nActivity Summary:")
#     for row in rows:
#         print(f"{row[0]}: {row[1]} entries")

# Menu loop for user interaction
def menu():
    while True:
        print("\nFarm Log Menu")
        print("1. Add new log")
        print("2. View all logs")
        print("3. Update a log")
        print("4. Delete a log")
        print("5. View logs by field name")
        print("6. View logs by activity type")
        print("7. View logs by date range")
        # print("8. Activity summary (count by type)")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_log()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            update_log()
        elif choice == "4":
            delete_log()
        elif choice == "5":
            view_by_field()
        elif choice == "6":
            view_by_activity()
        elif choice == "7":
            logs_by_date_range()
        # elif choice == "8":
        #     activity_summary()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
    conn.close()