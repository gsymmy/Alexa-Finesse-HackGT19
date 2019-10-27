import requests
import calendar
import datetime
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import json
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
import requests
import math
# from bs4 import BeautifulSoup

config = {
        "type": "service_account",
        "project_id": "hackgt-finesse",
        "private_key_id": "7968f779808ef68de54038f0035d1e070a6c3738",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCza0bEmWJn9D3i\nfK81tKkl2BVcF094EpF2akoK1gaIHvxNhGG+ljVBq4+z4Y1WqlJeEB19HnjauNOE\n1+mnzG/Yd9bowh3gP3MsV8LF0vh2ESqG30hiGqOlWXF9OLXbKZP9rjlTSGCiZz5W\nFVkLt2BuSCRyoDoh2yGKrnWShNUKsfAhRU+sceAuPZPXM2RTrhK/Vqiah4v3ApET\nQR/Rcbj93LbMbCA4zY5zxeyxx8TxCC6LfKl2b5GDFnL82QVS7DdOu9zCgDYTNtBR\nLt8Tbotom/I/eufDVfapMSB6eaNhz7ApvOVv91NcKdk9J7ZAGNSCN8dpV3iUbJ7g\nF508sQl5AgMBAAECggEAAse1Q4Oa7kBvGwzSjDL98fusrQ4haZtkDKEt/4f8dux/\n/VWBTDo4ngliAygKEB84goOeaVtpBP6bLHJKCRMWYpTMzDOB0gE5sCS1/Gm99tpi\nPc/E59xAz+WYaBfSXZCB3grukXdMJAgUg7H1/MP9JwhQJESOUgr6tJLqeHg9ctpz\nVSKRuJCgeyvcfJiHlMKKwD4Wrmb/WH9ftQt6lIyHLC+i3/v5gQ4CFS5YjM8qD3X9\naTeo2BwP7IeOpJhUyRw5suxCwfFZDsRapi0iUA7qcCo6uhZpeHU3aIc9RjKcW5cd\nBoDfh5Q5Q1es+I4J1fI+W7ey4JFtm4LAmFeM9uP8gQKBgQDl2om/oqEpsMMZtpRu\nuvwJw1/fm96vl9wwbFBYybzTDUurm5AlGAFsf8LRQClnuLUNkcdvDN7X0UnKjSnB\nNAZQcJ0ASBGaBQZsBlB8bzZ3Cto877Rj0gzVDtWi+yLrFbcPlPs5jEBbWJiG8LR7\nFkOUQBCqxIJOnBdO8w4UXi9P2QKBgQDH1A4oxcnlDVZDDlcRgXjOrdsS/HjGUJln\n+7kIkTIh4j7YnazXs6NikTW4NM9t05nfgVDhOtNlOGvv3brEMs+DgXyYHB9z0VS2\n2FjnsqgitxTMzWiYpZxbBLQGRgRFi2Dy3B/R12ykLS2qeRFyYCOTNOdO/sCzP/Z/\nrHb92t0ioQKBgQDBBUtl9XE3bGv6XNu7PSTIIhyRz/gqJvHObDbwyMDbzy97ddCP\nheA0N/nm9OWQZ4kLUx9SP1GnlOZNxUuKJmEjDd6aTOsTFyM0df0C8fWf9CoewAER\nTmReSu3WxuSk3AB1gluSERg+XWEA+IPnVWP8y+vzK8BtuSDNuMhbDFjYyQKBgQCF\nqPV/mCyfJPiaCbF7aBqiQ+/RF0bBf4/c2aa+cEAUIfzfbzf5X5LdjztbZxeH4o19\nzkWHIY3cmoy3+JvAOCxNTgNEyyrOkSoU00lEUV/dOJCVHJ/l2oBm8RJpT9PzoHLM\nfyhZd7qXZhCxgiGFW4DwKea+E/BY9WOvqnA9BHP9gQKBgQCnW77iv72fguh/x/T4\n3RG1tyi/zI91TpGNPfzbdr2Ct8+YANs0PFKYVWBAYrz1AAyT7p/oJ1+IzWLkf0RM\nvfFV8eIujaFVsStGqmNIaaSn1sfXjnxtIaUg04/VYH598DvCapqbjbtd5q7EnxxW\nwBHv74/DFnWO8dp7hG4j6CEZXA==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-7ljeu@hackgt-finesse.iam.gserviceaccount.com",
        "client_id": "102206742043320407900",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-7ljeu%40hackgt-finesse.iam.gserviceaccount.com"
    }
cred = credentials.Certificate(config)
default_app = firebase_admin.initialize_app(cred, options = {
    'databaseURL': "https://hackgt-finesse.firebaseio.com/"
    })
month_ref = db.reference('Monthly')
monthly_data = {}

def get_current_balance():
    headers = {
        'content-type': "application/json",
        'transactionid': "fdd1542a-bcfd-439b-a6a1-5a064023b0ce",
        'authorization': "Bearer HgPTB9f9qsMhtmkX4SfUEXkg5GjA"
        }
    r = requests.get("http://ncrqe-qe.apigee.net/digitalbanking/db-accounts/v1/accounts/rf5ao6Qclwsth9OfOvUb-EeV1m2BfmTzUEALGLQ3ehU?hostUserId=HACKATHONUSER105", headers=headers)
    data = r.json()
    return data['currentBalance']['amount']

def get_transaction_data():
    global monthly_data
    headers = {
        'content-type': "application/json",
        'transactionid': "fdd1542a-bcfd-439b-a6a1-5a064023b0ce",
        'authorization': "Bearer HgPTB9f9qsMhtmkX4SfUEXkg5GjA"
    }
    r = requests.get("http://ncrqe-qe.apigee.net/digitalbanking/db-transactions/v1/transactions?accountId=rf5ao6Qclwsth9OfOvUb-EeV1m2BfmTzUEALGLQ3ehU&hostUserId=HACKATHONUSER106", headers=headers)
    file = open('get_transaction.json', 'r')
    data = json.load(file)
    for i in range(len(data['transactions'])):
        splitted = data['transactions'][i]['transactionDate'].split('-')
        month_name = datetime.date(2019, int(splitted[1]), int(splitted[2])).strftime('%B')
        try:
            monthly_data[month_name][data['transactions'][i]['id']] = {
                'transaction-id': data['transactions'][i]['id'],
                'date': data['transactions'][i]['transactionDate'],
                'description': data['transactions'][i]['description'],
                'amount': data['transactions'][i]['amount']['amount'],
                'type': data['transactions'][i]['type'],
                'rec': data['transactions'][i]['memo']
            }
        except:
            monthly_data[month_name] = {}
            monthly_data[month_name][data['transactions'][i]['id']] = {
                'transaction-id': data['transactions'][i]['id'],
                'date': data['transactions'][i]['transactionDate'],
                'description': data['transactions'][i]['description'],
                'amount': data['transactions'][i]['amount']['amount'],
                'type': data['transactions'][i]['type'],
                'rec': data['transactions'][i]['memo']
            }
    month_ref.update(monthly_data)

    return monthly_data
get_transaction_data()
def set_budget(budget, month):
    month_ref.child(month).update({
        'monthly_budget' : budget
        })

def get_budget(month):
    return month_ref.child(month).get()

def distribute():
    transaction_data = get_transaction_data()
    total_spent = 0.0
    distribution = {}
    month_dict = {}
    for month in transaction_data:
        for t_id in transaction_data[month]:
            category = read_description(transaction_data[month][t_id]['description'])
            total_spent += transaction_data[month][t_id]['amount']
            if category in distribution.keys():
                distribution[category] += transaction_data[month][t_id]['amount']
            else:
                distribution[category] = transaction_data[month][t_id]['amount']
        for key in distribution.keys():
            distribution[key] = math.ceil((distribution[key] / total_spent) * 100)
        month_dict[month] = distribution

    return distribution

# def get_update(month):
#     curr = get_current_balance()
#     limit = get_budget(month)
#     if limit <= curr:
#         return "Too bad! You're already past the limit" #plays sad song
#     elif limit - curr <= 100:
#         return "You're almost there! Start saving and you'll be fine"
#     elif limit - curr > 100:
#         return "Amazing, you're a pro budgeter!"


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

# def get_offer_from_unidays():
#    response = requests.get("https://www.myunidays.com/US/en-US/category/all-tech_laptops-and-tablets")
#    html = response.text
#    soup = BeautifulSoup(html, "html.parser")
#   tweet = soup.find(class_="tile tile-onebyone")
#   get_list = tweet.get_text().split()
#   toReturn = get_text[0] + "has an offer. You can get " + get_list[1] + get_list[2] + get_list[3]
distribute()
