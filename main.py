from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
# import requests
# from bs4 import BeautifulSoup
from data import get_transaction_data
from data import get_current_balance
from data import get_budget

def distribute():
    transaction_data = get_transaction_data()
    total_spent = 100
    distribution = {}
    for transaction in transaction_data:
        category = read_description(description)
        if category in distribution.keys():
            distribution[category] += transaction[amount]
        else:
            distribution[category] = transaction[amount]

    for key in distribution.keys():
        distribution[key] = (distribution[key] / total_spent) * 100

    return distribution

# def analyse_dst():
#     distribution = distribute()
#     # sort dictionary descending by value
#     print("You have spent {} on {}, {} on {}, and {} on {}, {}, {}")

# def advice():
#     distribution = distribute()
#     # if the top distribution is >50% then say "You're spending too much on this"
#     #Get the top two distributions
#     #if they match the same parent category - advice on reduing each a bit
#     # else say - your finance look sorted

def get_update():
    curr = get_current_balance()
    limit = get_budget(month)
    if limit <= curr:
        return "Too bad! You're already past the limit" #plays sad song
    elif limit - curr <= 100:
        return "You're almost there! Start saving and you'll be fine"
    elif limit - curr > 100:
        return "Amazing, you're a pro budgeter!"

# def get_offer_from_unidays():
#     response = requests.get("https://www.myunidays.com/US/en-US/category/all-tech_laptops-and-tablets")
#     html = response.text
#     soup = BeautifulSoup(html, "html.parser")
#     tweet = soup.find(class_="tile tile-onebyone")
#     get_list = tweet.get_text().split()
#     toReturn = get_text[0] + "has an offer. You can get " + get_list[1] + get_list[2] + get_list[3]



def read_description(description):
    text = word_tokenize(description)
    tagged_tokens = pos_tag(text)
    noun_tokens = []
    for tup in tagged_tokens:
        if tup[1] == "NNP":
            noun_tokens.append(tup[0])
    return categorize(noun_tokens[0])


def categorize(token):
    Groceries = ["Publix", "Krogers", "CVS", "GoPuff", "FreshMarket"]
    Restaurant = ["UberEats", "Doordash", "Grubhub", "Subway", "HalalGuys", "Intermezzo", "TacoBell", "InsomniaCookies", "Starbucks"]
    Home = ["HomeDepot", "Walmart", "Target"]
    Entertainment = ["Netflix", "PrimeVideo", "Spotify"]
    Education = ["BN", "Blick"]
    Transportation =  ["Uber", "Lyft", "Bird", "Lime"]
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
