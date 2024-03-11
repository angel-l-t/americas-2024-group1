import sqlite3

# Connect to the database
conn = sqlite3.connect('titanicdb.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Execute SQL queries to retrieve data
cursor.execute("SELECT COUNT(*) FROM Titanic WHERE sex = 'male'")
total_male = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM Titanic WHERE sex = 'female'")
total_female = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM Titanic WHERE survived = 'survived' AND sex = 'male'")
male_survived = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM Titanic WHERE survived = 'survived' AND sex = 'female'")
female_survived = cursor.fetchone()[0]

# Calculate survival rates as percentages
male_survival_rate = (male_survived / total_male) * 100
female_survival_rate = (female_survived / total_female) * 100

# Close the cursor and the connection
cursor.close()
conn.close()

# Print the calculated survival rates
print("Male survival rate:", male_survival_rate)
print("Female survival rate:", female_survival_rate)

# Write data to survived_avg.js for visualization
with open('survived_avg.js', 'w') as fhand:
    fhand.write("titanic = [ ['Gender', 'Survival Rate'],\n")
    fhand.write(f"['Male', {male_survival_rate}],\n")
    fhand.write(f"['Female', {female_survival_rate}]\n")
    fhand.write("];\n")

print("Output written to survived_avg.js")
