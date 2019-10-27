from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag


def get_curr_balance():
    return 

def get_monthly_budget():
    return

def set_monthly_budget(new_budget):

def distribute():
    transaction_data = {}
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

def analyse_dst():
    distribution = distribute()
    # sort dictionary descending by value
    print("You have spent {} on {}, {} on {}, and {} on {}, {}, {}")

def advice():
    return

def get_offers():

def get_update():

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
    Transportation =  ["Uber", "Lyft"]
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
