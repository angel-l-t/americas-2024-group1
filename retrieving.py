import urllib.request, urllib.parse, urllib.error
import ssl
import sqlite3

conn = sqlite3.connect('titanicdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Titanic;


CREATE TABLE Titanic (
    id  INTEGER PRIMARY KEY,
    class TEXT ,
    survived TEXT,
    sex TEXT,
    age INTEGER
                  
);
''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")

if len(url) == 0 : url = "https://vincentarelbundock.github.io/Rdatasets/csv/vcdExtra/Titanicp.csv"

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

rows = data.split("\n")
# print (rows)
# rownames,pclass,survived,sex,age,sibsp,parch

#   0        1      2       3   4   5       6    
# exit()
new_row = rows[1:]
# print(new_row)
# exit()
for i in range(len(new_row)-1):
    pieces = new_row[i].split(',')

    pclass = pieces[1]
    survived = pieces[2]
    sex = pieces[3]
    age = 0 if len(pieces[4])==0 else round(int(float(pieces[4])))
    sibsp = pieces[5]
    parch = pieces[6]

    print(pclass, survived, sex, age)

    cur.execute('''INSERT OR REPLACE INTO Titanic
        (class, survived, sex, age) 
        VALUES ( ?, ?, ?, ?)''', 
        ( pclass, survived, sex, age ) )

    conn.commit()
