import re

# Function to preprocess text (lowercase and remove punctuation)
def preprocess_text(text):
    # Convert all words to lowercase
    text = text.lower()

    # Remove all punctuation marks using regular expressions
    text = re.sub(r'[^\w\s]', '', text)

    return text

# Read the press release from the file
with open('Apple TV.txt', 'r') as file:
    press_release = file.read()

# Preprocess the press release
processed_release = preprocess_text(press_release)

# Tokenize the processed text into words
words = processed_release.split()

# Create a dictionary to store word length counts
word_length_counts = {}

# Count the number of times words of different lengths appear
for word in words:
    word_length = len(word)
    if word_length in word_length_counts:
        word_length_counts[word_length] += 1
    else:
        word_length_counts[word_length] = 1

# Print the word length statistics
for length, count in sorted(word_length_counts.items()):
    print(f"{length} {count}")