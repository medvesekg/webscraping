from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

total_viewers = 0

# Open the main page and parse HTML
url = "https://en.wikipedia.org/wiki/Game_of_Thrones"
response = urlopen(url).read()
soup = BeautifulSoup(response)

# Find the table that has links to season subpages
seasons_table = soup.findAll("table")[1]

for link in seasons_table.findAll("a"):
    if link.string.find("Season") != -1:    # Filter out the links that do not link to season subpages

        # Open the subpage for each season
        season_subpage = "https://en.wikipedia.org" + link["href"]
        response = urlopen(season_subpage).read()
        soup = BeautifulSoup(response)

        for episode in soup.findAll("tr", {"class" : "vevent"}):        # Get the row with viewer information for each episode
            viewers_table_cell = episode.findAll("td")[5]               # Get the table cell with viewer information
            episode_viewers = viewers_table_cell.contents[0].string     # Get only the number of viewers
            if episode_viewers is not None:                             # Filter out episodes which haven't aired yet
                print episode_viewers
                total_viewers += float(episode_viewers)                 # Add viewer number to the total




print "The total number of viewers who watched GoT episodes on the first day is", total_viewers, "million."