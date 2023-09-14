from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read text from a file
with open('word_count.txt', 'r') as file:
    text = file.read()

# Create a WordCloud object with custom dimensions
wordcloud = WordCloud(width=1584, height=396).generate(text)

# Display the word cloud (you can also save it to an image file)
plt.figure(figsize=(15.84, 3.96))  # Adjust the figure size to match the dimensions
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
