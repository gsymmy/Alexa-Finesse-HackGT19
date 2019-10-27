# Finesse

Submitted to HackGT'19

* Best use of NCR's API
* Best Cloud Computing Application to improve FinTech Industry by Accenture

<p align="center">
  <img width="240" height="240" src="/logo.png">
</p>

## Demo
<a href="https://www.youtube.com/embed/KR08cri1SY0" target="_blank"><img src="/echo.png" 
alt="Amazon Echo" width="240" height="180" border="10" />Click on Image for Demo Video</a>


## Inspiration
Our idea for Finesse sprung from our experiences as students without a meal plan this semester–we used to eat out every day and had no way to track our expenditures and see how we’re managing our money. While some of us had heard of Mint before, we weren’t interested in a financial ‘assistant’ that tells us how much we’re spending and earning. Rather, we wanted an advisor we could talk to. Our desire to try out a FinTech hack along with a motivation to learn Alexa Skills development led to the creation of Finesse

## What it does
Finesse is every college student’s ideal financial advisor built upon Alexa devices. It allows students to connect their banking transactional data to learn about their monthly expenditures, highest and recurring expenses. You can also set your own budget limits to manage money better and be notified of when you are close to exceeding it. In general, Finesse acts as an advisor by offering various suggestions on how to reduce expenditures and save money. Finally, to help students improve financial literacy, it offers the option to define any financial term or see how a stock is performing to get students more interested in the financial bubble.

What the commands looks like?

* Alexa, Enter the Finesse app (Requires AT&T Authentication)
* What is my current balance? (NCR's API)
* Analyze my expenditure (NCR's API)
* Give me financial advice (NCR's API and NLP)
* Find me some student deals (BeautifulSoup Web Scraping)
* Tell me the meaning of "Savings Account" (Merriam-Webster API)
* Set my monthly budget
* How is Apple performing? (Blackrock API)
## How we built it
We built Finesse as a custom Alexa Skill using the Python SDK. Using NCR's Banking and Transactions API to get the a user's banking data, we used Python's extensive libraries such as one for NLP which uses topic-tagging to segregate NCR's transaction description into discrete categories. These categories then help us group the data and analyze it for generating useful inferences which are provided as skills in our Alexa VUI. The app has been made secure by using AT&T's SMS API to send the Alexa's owner a One-Time Password which is confirmed on the VUI to authenticate access. We also used BeautifulSoup to scrape UNiDAYS for getting student deals which are added as a recommendation functionality on the platform.

## Challenges we ran into
Integrating Firebase with Alexa Developer Console was challenging because the Alexa Skills Kit offers good coverage for AWS databases but not so much for Firebase RTDBs. Doing asynchronous fetches and pulls in the middle of a conversation was an interesting challenge that we struggled with for a long time.

## Accomplishments that we're proud of
Combining a lot of API’s to make a meaningful product where the whole is greater than the sum of its parts, and integrating Alexa Skills–something we’re new to–to frameworks like Firebase that we have used before

## What we learned
Using Python’s NLTK Library for topic-tagging and categorization of data, creating custom Alexa skills and maintaining a conversational Voice User Interface, persistent data storage from Alexa’s event responses. And a lot of financial terms!

## What's next for Finesse
We’re thinking of expanding our user base towards small businesses because they could find this app useful at POS for a slightly different use case: tracking their sales and seeing how different products are doing.

### Technologies Used
  * alexa-skills-kit
  * amazon-alexa
  * at&t-sms-api
  * beautiful-soup
  * blackrock-api
  * firebase
  * google-cloud
  * natural-language-processing
  * ncr-api
  * nltk
  * python
  * requests
  * topic-tagging
  * yahoo-finance-api
