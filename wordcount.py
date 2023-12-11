import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

file_path = r'C:\Users\hp\Desktop\twitter\master.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Handle missing values in the 'Comments' column
df['Comments'] = df['Comments'].fillna('')  # Replace NaN with an empty string

# Tokenize the text and filter out stop words and punctuation
stop_words = set(stopwords.words('english'))
punctuation_set = set(punctuation)
df['tokens'] = df['Comments'].apply(lambda x: [word.lower() for word in word_tokenize(x) if word.lower() not in stop_words and word.lower() not in punctuation_set])

# Count the occurrences of each word
word_counts = Counter(word for words in df['tokens'] for word in words)

# Get the top 10 most repeated words
top_10_words = word_counts.most_common(10)

# Print or use the results as needed
print(top_10_words)
