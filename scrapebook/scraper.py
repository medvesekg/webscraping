from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = 'https://scrapebook22.appspot.com'
response = urlopen(url).read()

soup = BeautifulSoup(response)

first_names = []
last_names = []
cities = []
ages = []
emails = []

for row in soup.findAll("tr"):
    for i, data in enumerate(row.findAll("td")):
        if i == 0:
            first_names.append(data.string)
            print data.string
        elif i == 1:
            last_names.append(data.string)
            print data.string
        elif i == 2:
            ages.append(data.string)
            print data.string
        elif i == 3:
            cities.append(data.string)
            print data.string



for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = url + link["href"]


        person_details = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_details)
        person_email = person_soup.find("span", attrs={"class": "email"}).string
        emails.append(person_email)
        print person_email


with open("data.csv", "w") as out_file:
    out_file.write("First name;Last name;City;Age;Email\n")
    for i in range(0, len(first_names)):
        out_file.write(first_names[i] + ";" + last_names[i] + ";" + cities[i] + ";" + ages[i] + ";" + emails[i] + "\n")

print "Done"