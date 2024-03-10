import sqlite3

# Connect to the database (creates a new database if not already present)
conn = sqlite3.connect('titanicdb.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query to retrieve data and fetch data
cursor.execute("SELECT COUNT(*) FROM Titanic WHERE survived = 'died' AND sex = 'male'")

male_deceased = cursor.fetchall()

cursor.execute("SELECT COUNT(*) FROM Titanic WHERE survived = 'died' AND sex = 'female'")

female_deceased = cursor.fetchall()

# Close the cursor and the connection
cursor.close()
conn.close()

# Print data (for demonstration)
print("Male deceased", male_deceased[0][0])
print("Female deceased", female_deceased[0][0])

# Write data to t-mf-survivors.js for visualization
fhand = open('t-mf-survivors.js','w')
fhand.write("titanic = [ ['Gender and status', 'Number'],")
fhand.write(f"['Male deceased', {male_deceased[0][0]}],\n")
fhand.write(f"['Female deceased', {female_deceased[0][0]}]\n")
fhand.write("];\n")
fhand.close()

print("Output written to t-mf-survivors.js")
print("Open t-mf-survivors.htm to visualize the data")