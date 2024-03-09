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
# print(data_list)

ageGroup ={}

# Iterate through the list 
for data in data_list:

    age = data[4]
    
    # Determine the age group and add it to the set
    if 0 <= age < 11:
        data.append('kids')
        ageGroup['kids'] = ageGroup.get('kids',0)+1
    elif 11 <= age < 20:
        data.append('teens')
        ageGroup['teens'] = ageGroup.get('teens',0)+1
    elif 20 <= age < 30:
        data.append('twenties')
        ageGroup['twenties'] = ageGroup.get('twenties',0)+1
    elif 30 <= age < 40:
        data.append('thirties')
        ageGroup['thirties'] = ageGroup.get('thirties',0)+1
    elif 40 <= age < 50:
        data.append('forties')
        ageGroup['forties'] = ageGroup.get('forties',0)+1
    elif 50 <= age < 60:
        data.append('fifties')
        ageGroup['fifties'] = ageGroup.get('fifties',0)+1
    elif 60 <= age < 70:
        data.append('sixties')
        ageGroup['sixties'] = ageGroup.get('sixties',0)+1
    elif 70 <= age < 80:
        data.append('seventies')
        ageGroup['seventies'] = ageGroup.get('seventies',0)+1
    elif 80 <= age < 90:
        data.append('eighties')
        ageGroup['eighties'] = ageGroup.get('eighties',0)+1
    elif 90 <= age < 100:
        data.append('nineties')
        ageGroup['nineties'] = ageGroup.get('nineties',0)+1
    elif age >= 100:
        data.append('centenarian')
        ageGroup['centenarian'] = ageGroup.get('centenarian',0)+1


print(ageGroup)


fhand = open('view/titanic.js','w')
fhand.write("titanic = [ ['age','Number of People']")

for key,value in ageGroup.items():
    fhand.write(",\n['"+key+"',"+ str(value))
    fhand.write("]");


fhand.write("\n];\n")
fhand.close()

print("Output written to titanic.js")
print("Open titanic.html to visualize the data")