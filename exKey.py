import nltk
import nltk.data
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


#extracts keywords from a given text
def extract_keywords(text):
    # Organize the text into words and remove stop words
    print('A')
    words = word_tokenize(text)
    print('B')
    add_stops = [',', '.', '[', ']', '(', ')'] 
    stop_words = set(stopwords.words('english'))
    stop_words.update(add_stops)
    filtered_words = [word for word in words if word.lower() not in stop_words]

    print("list of stop words is: ")
    print(stop_words)
    
    # Calculate the frequency of each word
    print('C')
    freq_dist = nltk.FreqDist(filtered_words)
    
    # Return the 10 most common words
    print('D')
    return freq_dist.most_common(10)