import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")

if len(url) == 0 : url = "https://vincentarelbundock.github.io/Rdatasets/csv/vcdExtra/Titanicp.csv"

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

i = 0
rows = data.split("\n")

for row in rows :
    print(row)

    if i == 50 :
        break
    i += 1