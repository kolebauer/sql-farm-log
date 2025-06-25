# Overview

This project is a command-line Farm Log Tracker designed to help farmers and agricultural operators record and manage daily fieldwork activities in a structured and organized way. It integrates with a relational SQL database to store log entries that include the field name, date, activity performed, and additional notes.

I created this project to strengthen my understanding of how backend software interacts with a SQL database. It reinforces key software engineering skills such as structured data storage, CRUD (Create, Read, Update, Delete) operations, input validation, and modular design within a real-world use case relevant to my background.

The system is fully CLI-driven. Users can:
- Add new log entries
- View all logs
- Search logs by field name, activity type, or date range
- Update or delete existing entries


[Software Demo Video](Don't Forget to Add Me)


# Relational Database

This program uses an SQLite database (`farm_logs.db`) as the backend. SQLite was chosen for its simplicity and file-based architecture, which makes it ideal for lightweight, local applications like this one.

The database contains a single table called `farm_logs` with the following structure:

| Column     | Type    | Description                               |
|------------|---------|-------------------------------------------|
| id         | INTEGER | Primary key (autoincremented)             |
| field_name | TEXT    | Name of the field                         |
| date       | TEXT    | Date of the activity (format: YYYY-MM-DD) |
| activity   | TEXT    | Description of the activity performed     |
| notes      | TEXT    | Additional details or context (optional)  |


# Development Environment

- Language: Python 3.11
- Database: SQLite using Python's built-in sqlite3 library
- Editor: Visual Studio Code
- Platform: Windows 11


# Useful Websites

- [SQLite Python Tutorial – SQLitetutorial.net](https://www.sqlitetutorial.net/sqlite-python/)
- [Python SQLite3 Docs](https://docs.python.org/3.11/library/sqlite3.html)
- [Python String Formatting and Common Operations](https://docs.python.org/3.11/library/string.html)


# Future Work

- Merge this CLI project into a forked or copied version of my energy dashboard to begin pivoting toward a full-featured farm management dashboard.
- Design the system to be modular and customizable, allowing users to enable or disable features based on their specific operation (e.g., crop farming, dairy, ranching, or mixed-use).
- Add crop tracking with lifecycle phases, input usage, and seasonal planning.
- Integrate yield analysis based on historical logs and environmental conditions.
- Develop livestock tracking for herd size, health records, and pasture rotation.
- Incorporate expense tracking tied to specific fields, crops, or animals for better financial insights.

