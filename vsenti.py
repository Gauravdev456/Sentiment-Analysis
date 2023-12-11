import nltk
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
plt.style.use('ggplot')
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)


sia = SentimentIntensityAnalyzer()


file_path = r'C:\Users\hp\Desktop\twitter\master.csv'

df = pd.read_csv(file_path, quoting=csv.QUOTE_MINIMAL, doublequote=True, escapechar='\\', encoding='unicode_escape')



def get_sentiment_score(text):
    if isinstance(text, str) and text.strip(): 
        
        score = sia.polarity_scores(text)
        sentiment_score = [score['neg'], score['neu'], score['pos']]
        return softmax(sentiment_score)
    else:
        return [0.0, 0.0, 0.0]

df[['neg', 'neu', 'pos']] = df['Comments'].apply(lambda text: pd.Series(get_sentiment_score(text)))


output_file_path = r'C:\Users\hp\Desktop\twitter\tweets_with_vadersentiment.csv'
df.to_csv(output_file_path, index=False)



# df['comp'].plot(kind='bar', color=['red', 'gray', 'green'], figsize=(8, 5))
# plt.title('Overall Compound Sentiment')
# plt.xlabel('Sample')
# plt.ylabel('Compound Score')
# plt.show()
# df['overall_sentiment'] = pd.cut(df['comp'], bins=[-1, -0.5, 0.5, 1], labels=['Negative', 'Neutral', 'Positive'])

# # Plotting
# df['overall_sentiment'].value_counts().plot(kind='bar', color=['red', 'gray', 'green'], figsize=(8, 5))
# plt.title('Overall Sentiment Distribution')
# plt.xlabel('Sentiment')
# plt.ylabel('Count')
# plt.show()
# df[['neg', 'pos', 'comp']].plot(kind='bar', stacked=True, colormap='viridis', figsize=(10, 6))
# plt.title('Sentiment Scores')
# plt.xlabel('Data Points')
# plt.ylabel('Score')
# plt.show()

# df['comp'].plot(kind='bar', color=['red' if x < 0 else 'green' for x in df['comp']], figsize=(10, 6))
# plt.title('Distribution of Compound Scores')
# plt.xlabel('Data Points')
# plt.ylabel('Compound Score')

# plt.show()
# filtered_df = df[df['comp'] != 0]

# # Plot for 'pos' and 'neg'
# filtered_df[['pos', 'neg']].plot(kind='bar', stacked=True, colormap='viridis', figsize=(10, 6))
# plt.title('Distribution of Positive and Negative Scores')
# plt.xlabel('Data Points')
# plt.ylabel('Score')

# plt.show()




# x = df['neg']
# y = df['neu']
# z = df['pos']

# # Create a 3D axes
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Scatter plot
# ax.scatter(x, y, z, c='r', marker='o')

# # Set labels
# ax.set_xlabel('Negative Score')
# ax.set_ylabel('Neutral Score')
# ax.set_zlabel('Positive Score')

# # Show the plot
# plt.show()

# positive_count = len(df[df['comp'] > 0])
# negative_count = len(df[df['comp'] < 0])

# # # Data for the pie chart
# labels = ['Positive', 'Negative']
# sizes = [positive_count, negative_count]
# colors = ['green', 'red']

# # # Plotting the pie chart
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
# plt.title('Sentiment Analysis Pie Chart')
# plt.show()

# def label_sentiment(compound):
#     if compound > 0:
#         return 'positive'
#     if compound < 0: 
#         return 'negative'


# df['Comments'] = df['comp'].apply(label_sentiment)

# plt.figure(figsize=(10, 6))
# sns.countplot(x='Comments', data=df, palette='viridis')
# plt.title('Sentiment Analysis Results')
# plt.xlabel('Sentiment')
# plt.ylabel('Count')
# plt.show()

# Print the DataFrame
# print(df[['text_column', 'compound', 'sentiment']])





# Calculate the mean sentiment scores for each sentiment category
mean_sentiment = df[['neg', 'neu', 'pos']].mean()


colors = ['orange', 'blue', 'green']

# Create a bar plot using Seaborn with custom colors
sns.barplot(x=mean_sentiment.index, y=mean_sentiment.values, palette=colors,width=0.5)

# Set plot labels and title
plt.xlabel('Sentiment')
plt.ylabel('Mean Score')
plt.title('Overall Sentiment Distribution')

# Show the plot
plt.show()

# Define labels and colors for the pie chart
# labels = ['Negative', 'Neutral', 'Positive']
# colors = ['red', 'gray', 'green']

# # Create a pie chart
# plt.pie(mean_sentiment, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# # Set plot title
# plt.title('Overall Sentiment Distribution')

# # Show the plot
# plt.show()