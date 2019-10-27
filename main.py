from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
import requests
from bs4 import BeautifulSoup

Groceries = ["Publix", "Krogers", "CVS", "GoPuff", "FreshMarket"]
Restaurant = ["UberEats", "Doordash", "Grubhub", "Subway", "HalalGuys", "Intermezzo", "TacoBell", "InsomniaCookies", "Starbucks"]
Home = ["HomeDepot", "Walmart", "Target"]
Entertainment = ["Netflix", "PrimeVideo", "Spotify"]
Education = ["BN", "Blick"]
Transportation =  ["Uber", "Lyft", "Bird", "Lime"]

def read_description(description):
    text = word_tokenize(description)
    tagged_tokens = pos_tag(text)
    noun_tokens = []
    for tup in tagged_tokens:
        if tup[1] == "NNP":
            noun_tokens.append(tup[0])
    return categorize(noun_tokens[0])


def categorize(token):
    global Groceries
    global Restaurant
    global Home
    global Entertainment
    global Education
    global Transportation
    category = ""
    if token in Groceries:
        category = "Grocery"
    elif token in Restaurant:
        category = "Restaurant"
    elif token in Home:
        category = "Home"
    elif token in Transportation:
        category = "Transportation"
    elif token in Entertainment:
        category = "Entertainment"
    elif token in Education:
        category = "Education"
    else:
        category = "Miscellaenous"
    return category

def scrape_unidays_for_groceries():
    global Groceries
    response = requests.get("https://www.myunidays.com/US/en-US/category/all-food_groceries")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    scrape = soup.find(class_="tile__group")
    output = scrape.get_text().split()
    word_l = []
    for word in output:
        if word in Groceries:
            word_l.append(word)
            break
    print(word_l[0])

def scrape_unidays_for_restaurants():
    global Restaurant
    response = requests.get("https://www.myunidays.com/US/en-US/category/all-food_in-store-and-delivery")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    scrape = soup.find(class_="tile__group")
    output = scrape.get_text().split()
    word_l = []
    for word in output:
        if word in Restaurant:
            word_l.append(word)
            break
    print(word_l[0])

scrape_unidays_for_groceries()
scrape_unidays_for_restaurants()