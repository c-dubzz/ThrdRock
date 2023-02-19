import requests
import sqlite3
from bs4 import BeautifulSoup


def get_headlines(url):
    # Extract the text from headlines on a given url
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    headlines = content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    headlines_text = [headline.get_text().strip()
                      for headline in headlines]
    return headlines_text


# Connect to the database and create new headlines table
conn = sqlite3.connect('headlines.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS headlines (title TEXT)')

# Define the URL of the webpage to scrape and get headlines from it
url = 'https://www.nationalgeographic.com/pages/topic/latest-stories'
headlines = get_headlines(url)

url = 'https://www.nytimes.com/spotlight/learning-stem'
headlines = get_headlines(url)

url = 'https://www.sciencedaily.com/news/'
headlines = get_headlines(url)

url = 'https://www.theguardian.com/us/environment'
headlines = get_headlines(url)

url = 'https://www.theguardian.com/us/technology'
headlines = get_headlines(url)

url = 'https://www.theguardian.com/science'
headlines = get_headlines(url)

# Insert each headline into database
for headlines in headlines:
    c.execute('''INSERT INTO headlines (headline) VALUES (?)''', (headlines,))

# Commit changes and close connection
conn.commit()
conn.close()
