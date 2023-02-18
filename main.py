import requests
from bs4 import BeautifulSoup


def get_headlines(url):
    # Make a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the headline tags (h1, h2, h3, h4, h5, h6)
    headlines = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    # Extract the text content of each headline and store it in a list
    headlines_text = [headline.get_text().strip()
                      for headline in headlines]

    return headlines_text


url = 'https://www.nationalgeographic.com/pages/topic/latest-stories'
headlines = get_headlines(url)
# print(headlines)

url = 'https://www.nytimes.com/spotlight/learning-stem'
headlines = get_headlines(url)
# print(headlines)

url = 'https://www.sciencedaily.com/news/'
headlines = get_headlines(url)
# print(headlines)

url = 'https://www.theguardian.com/us/environment'
headlines = get_headlines(url)
# print(headlines)

url = 'https://www.theguardian.com/us/technology'
headlines = get_headlines(url)
# print(headlines)

url = 'https://www.theguardian.com/science'
headlines = get_headlines(url)
# print(headlines)
