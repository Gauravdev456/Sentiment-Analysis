import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# Load the CSV file into a Pandas DataFrame
csv_file_path = r"C:\Users\hp\Desktop\twitter\tweets_with_robertasentiment.csv"
df = pd.read_csv(csv_file_path)

# Check and handle data types
df['Comments'] = df['Comments'].astype(str)

# Handle NaN values
df = df.dropna(subset=['Comments'])

# Combine filtering conditions
max_pos_comments = df[df['pos'] > df[['neg', 'neu']].max(axis=1)]['Comments'].tolist()
max_neg_comments = df[df['neg'] > df[['pos', 'neu']].max(axis=1)]['Comments'].tolist()
max_neu_comments = df[df['neu'] > df[['pos', 'neg']].max(axis=1)]['Comments'].tolist()

# Adjust WordCloud parameters
wordcloud_params = {
    'width': 800,
    'height': 400,
    'background_color': "black",
    'max_words': 100
}

# Maximum positive sentiment
max_pos_wordcloud = WordCloud(**wordcloud_params).generate(' '.join(max_pos_comments))
plt.figure(figsize=(10, 5))
plt.imshow(max_pos_wordcloud, interpolation="bilinear")
plt.title('Positive ')
plt.axis("off")
plt.show()

# Maximum negative sentiment
max_neg_wordcloud = WordCloud(**wordcloud_params).generate(' '.join(max_neg_comments))
plt.figure(figsize=(10, 5))
plt.imshow(max_neg_wordcloud, interpolation="bilinear")
plt.title('Negative ')
plt.axis("off")
plt.show()

# Maximum neutral sentiment
max_neu_wordcloud = WordCloud(**wordcloud_params).generate(' '.join(max_neu_comments))
plt.figure(figsize=(10, 5))
plt.imshow(max_neu_wordcloud, interpolation="bilinear")
plt.title('Neutral ')
plt.axis("off")
plt.show()