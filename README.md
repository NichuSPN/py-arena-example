# Codebase Overview

This repository contains a Python application that demonstrates how to interact with different databases using the `arena` library. The application connects to PostgreSQL, SQLite, and MySQL databases, creating tables, inserting data, querying data, and cleaning up by dropping tables. 

**Note:** This code serves no purpose other than demonstrating the functionality of the `py-arena` package.

## Requirements

To run this application, ensure you have Python 3.x installed along with the necessary dependencies specified in the `requirements.txt` file. You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Database Connections

The application connects to three types of databases:

1. **PostgreSQL**
   - Modify the connection parameters in the `database-test.py` file to connect to your PostgreSQL instance.

2. **SQLite**
   - The SQLite database is created in the local directory as `py-arena-test.db`.

3. **MySQL**
   - Update the connection parameters in the `database-test.py` file to connect to your MySQL instance.

## Usage

### Running the Database Tests

To execute the database operations, run the following command:

```bash
python database-test.py
```

This script will:
- Create a table named `arena_test` in each database.
- Insert sample data into the table.
- Query the table for specific entries.
- Drop the table after the operations are complete.
- Close the database connections.

### API Tests

The `api-test.py` file demonstrates how to interact with various APIs. You can run it using:

```bash
python api-test.py
```

This script will:
- Fetch data from the Game of Thrones API.
- Interact with a RESTful API to perform various operations.