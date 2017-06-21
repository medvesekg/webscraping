from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import random

full_quotes = []


def get_full_quotes(subpage = ""):

    # Open page and parse HTML
    url = "http://quotes.yourdictionary.com/theme/marriage/" + subpage
    response = urlopen(url).read()
    soup = BeautifulSoup(response)

    # First find all quote blocks
    for quote_block in soup.findAll("div", {"class" : "QuotesAndNotes"}):

        # Get the quote itself, this is easy
        quote = quote_block.find("p", {"class" : "quoteContent"}).string

        # Get the author, this is trickier
        author = ""
        author_block = quote_block.find("small")   # First find the <small> tags
        if author_block.string is not None:         # If there is some information directly under the small tags, extract it
            author += author_block.string.strip() + ", "
        author_block = author_block.findChildren()    # Then also get all the child tags of small and extract any additional infomration
        for author_information in author_block:
            if author_information.string is not None:
                author += author_information.string.strip() + ", "  # Build the full author string


        full_quotes.append(quote.lstrip() + " - " + author.rstrip(", "))  # Add the quote itself and the author to the same string. Strip the any empty spaces to make it look nicer.



# Call the function on the main pages and also on all of the subpages
get_full_quotes()

for subpage in range (2,5):
    get_full_quotes(str(subpage) + "/")


def get_random_quotes(howMany):
    for i in range(0,howMany):
         random_number = random.randint(0,len(full_quotes))
         print full_quotes[random_number]

# Get 5 random quotes
get_random_quotes(5)







