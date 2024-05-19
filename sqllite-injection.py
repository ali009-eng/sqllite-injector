import sqlite3

# Create a new SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

name = "ali "
email = "ali@example.com"
c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
print("Test case 1 (valid parameter): Success")


name = "Alice'; DROP TABLE users; --"
email = "alice@example.com"
try:
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
except sqlite3.OperationalError as e:
    print(f"Test case 2 (SQL injection attempt): {e}")
else:
    print("Test case 2 (SQL injection attempt): Failed to prevent injection")


name = "Bob"
email = "bob@example.com; DROP TABLE users; --"
try:
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
except sqlite3.OperationalError as e:
    print(f"Test case 3 (SQL injection with a parameter marker): {e}")
else:
    print("Test case 3 (SQL injection with a parameter marker): Failed to prevent injection")

conn.commit()
conn.close()