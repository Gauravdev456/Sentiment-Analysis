
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
# Load the CSV files into Pandas DataFrames
file1 = r"C:\Users\hp\Desktop\twitter\tweets_with_robertasentiment.csv"
file2 = r"C:\Users\hp\Desktop\twitter\tweets_with_vadersentiment.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Select only numeric columns (assuming "neg," "neu," and "pos" are numeric)
numeric_columns1 = df1[['neg', 'neu', 'pos']]
numeric_columns2 = df2[['neg', 'neu', 'pos']]

mean_values1 = numeric_columns1.mean()
mean_values2 = numeric_columns2.mean()
combined_df = pd.concat([numeric_columns1, numeric_columns2], ignore_index=True)

# Calculate the mean values for all sentiment categories across both files
mean_values = combined_df.mean()

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a bar graph with adjusted x-coordinates for the second set of bars
categories = np.arange(len(mean_values1))
bar_width = 0.20
space=0.03

plt.bar(categories, mean_values1, width=bar_width,label='Roberta')
plt.bar(categories + bar_width+space, mean_values2, width=bar_width, label='Vader')
plt.bar(categories + 2 * (bar_width+space), mean_values, width=bar_width, label='Combined')

# Add labels and title
plt.xlabel('Sentiment Category')
plt.ylabel('Mean Value')
plt.title('Overall Sentiment Distribution')
tick_labels = list(mean_values1.index)
tick_labels[0] = 'Negative'
tick_labels[1] = 'Neutral'
tick_labels[2] = 'Positive'
plt.xticks(categories + 1.5 * (bar_width + space), tick_labels)
desired_ticks = 10
plt.ylim(0, 0.55)
plt.yticks(np.linspace(0, 0.55, 12))
plt.legend()

# Show the plot
plt.show()