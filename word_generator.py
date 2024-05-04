"""
This program generates a list of words based on various criteria specified by the user.
The user will be prompted to enter the following information:

1. "Enter the letters you want to use: "
2. "Enter the priority letters: "
3. "Enter the minimum number of unique priority letters in each word: "
4. "Enter the minimum share of priority letters in each word (between 0 and 1): "
5. "Enter the number of words you want: "
6. "Do you want to shuffle the list? (y/n): "

Based on the user input, the program will generate a list of words that meet the following criteria:
- Use only the specified letters.
- Don't contain any uppercase letters or periods.
- Contain at least the specified minimum number of unique priority letters.
- Have at least the specified minimum share of characters as priority letters.

The user can choose whether to randomize the resulting list of words. The selected words are then printed along with the total number of words that meet the criteria.

Example:
(Prompt: user input)
Enter the letters you want to use: eniartos
Enter the priority letters: erta
Enter the minimum number of unique priority letters in each word: 3
Enter the minimum share of priority letters in each word (between 0 and 1): 0.5
Enter the number of words you want: 10
Do you want to shuffle the list? (y/n): y

Output:
Here are 10 words out of 579 meeting your criteria:
retirer otterer streeler tatter rester rainiest tetter iterate arsenite trierarch

In this example, the output includes words that contain at least 3 unique priority letters from the set {'e', 'r', 't', 'a'}, 
and at least 50% (0.5) of their characters are from this set of priority letters.
"""

import random
import nltk
from collections import Counter

# Download the necessary NLTK data
nltk.download('words')

def get_word_list(letters, priority_letters, min_priority_count, min_priority_share):
    # Load the dictionary of words from NLTK
    word_list = nltk.corpus.words.words()

    # Filter the word list based on the given criteria
    filtered_words = [
        word.lower() for word in word_list
        if set(word.lower()) <= set(letters)
        and not any(char.isupper() for char in word)
        and '.' not in word
        and len(set(word.lower()) & set(priority_letters)) >= min_priority_count
        and sum(Counter(word.lower())[char] for char in priority_letters) >= len(word.lower()) * min_priority_share
    ]

    # Return the filtered words and total count of words meeting the criteria
    return filtered_words, len(filtered_words)

# Prompt the user for input
letters = input("Enter the letters you want to use: ").lower()
priority_letters = input("Enter the priority letters: ").lower()
min_priority_count = int(input("Enter the minimum number of unique priority letters in each word: "))
min_priority_share = float(input("Enter the minimum share of priority letters in each word (between 0 and 1): "))
word_count = int(input("Enter the number of words you want: "))
shuffle_choice = input("Do you want to shuffle the list? (y/n): ").strip().lower()

# Get the word list and the total number of words meeting criteria
word_list, total_meeting_criteria = get_word_list(letters, priority_letters, min_priority_count, min_priority_share)

# Check if the user wants to shuffle the list
if shuffle_choice == 'y':
    random.shuffle(word_list)

# Get the desired number of words
word_list = word_list[:word_count]

# Output the results with the count of printed words and the total count of words meeting the criteria
print(f"Here are {len(word_list)} words out of {total_meeting_criteria} meeting your criteria:")
print(" ".join(word_list))