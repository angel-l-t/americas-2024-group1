import sqlite3

# Connect to the database (creates a new database if not already present)
conn = sqlite3.connect('titanicdb.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query to retrieve data
cursor.execute("SELECT * FROM Titanic")
# Fetch data and parse into a list of tuples
rows = cursor.fetchall()

# Close the cursor and the connection
cursor.close()
conn.close()

# Convert the fetched data into a list of lists
data_list = []
for row in rows:
    data_list.append(list(row))

# Print the list (for demonstration)
print(data_list)


fhand = open('titanic.js','w')
fhand.write("titanic = [ ['age'")
# for org in orgs:
#     fhand.write(",'"+org+"'")
# fhand.write("]")

# for year in years:
#     fhand.write(",\n['"+year+"'")
#     for org in orgs:
#         key = (year, org)
#         val = counts.get(key,0)
#         fhand.write(","+str(val))
#     fhand.write("]");

fhand.write("\n];\n")
fhand.close()

print("Output written to titanic.js")
print("Open titanic.html to visualize the data")