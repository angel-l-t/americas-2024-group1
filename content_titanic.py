import sqlite3

# Connect to the database
conn = sqlite3.connect('titanicdb.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query to retrieve data
cursor.execute("SELECT * FROM Titanic LIMIT 10")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Close the cursor and the connection
cursor.close()
conn.close()

# Print the fetched rows
for row in rows:
    print(row)
