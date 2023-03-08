import requests
import sqlite3
from bs4 import BeautifulSoup
import time
import datetime
import random
#from flask import Flask, render_template             STILL NEED TO FIX

# extracts headline text from given url
def get_headlines(url):
    # send GET request to url
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    content = BeautifulSoup(response.text, 'html.parser')

    headlines = content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    headlines_text = ""

    # Extract the text content of each headline and adds it to string a
    for headline in headlines:
        x = headline.get_text().strip()
        # x = headlines.get_text().strip()                   MAYBE??????
        headlines_text = headlines_text + " \n" + x
        
    return headlines_text

# create the table (if table DNE) for data entry
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS headlinesTable (textColumn TEXT, date TEXT)')

def enter_data(urlText, randNum):
    t = time.time()
    date = str(datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S'))
    params = (urlText, date)
    c.execute("INSERT INTO headlinesTable (textColumn, date) VALUES (?, ?)", (params))
    conn.commit()

# Connect to the database
conn = sqlite3.connect('headlines.db')
c = conn.cursor()

# Define the URL to scrape
url1 = 'https://www.nationalgeographic.com/pages/topic/latest-stories'
url2 = 'https://www.nytimes.com/spotlight/learning-stem'
url3 = 'https://www.sciencedaily.com/news/'
url4 = 'https://www.theguardian.com/us/environment'
url5 = 'https://www.theguardian.com/us/technology'
url6 = 'https://www.theguardian.com/science'


create_table()

# Loop through array of urls, adding each to database
urls = [url1, url2, url3, url4, url5, url6]
for item in (urls):
    txt = get_headlines(item)
    x = 1
    enter_data(txt, x)
    x = x + 1

c.close()
conn.close()
