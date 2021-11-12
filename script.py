"""
VERY ROUGH DRAFT FOR THE IDEA BEFORE A FRONTEND IS MADE

SPELLING BEE

Words must include the center letter.

Words must contain at least four letters.

Letters can be used more than once.

Our word list does not include words that are offensive, obscure, hyphenated or proper nouns.

Four-letter words are worth one point each.

Longer words earn one point per letter. A six-letter word is worth six points.

Each puzzle includes at least one “pangram,” which uses every letter at least once. A pangram is worth an additional seven points.
"""

import copy

# Importing the file
all_words_file = open("corncob_lowercase.txt", "r")

all_words = set()
for line in all_words_file:
  all_words.add(line.strip())

letters = {
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
}

# Creating a dictionary composed of sets with each word
dictionary = {}
for letter in letters:
    dictionary[letter] = set()

# Adding words to those sets
for word in all_words:
    for letter in letters:
        if letter in word:
            dictionary[letter].add(word)

# The outer letter, which can be used in the word
outer_letters = input("What are the outer letters?")
outer_letters = {letter for letter in outer_letters}

# The inner letter, which must be in the word
inner_letter = input("What is the inner letter of the day?")
inner_letter_word = inner_letter
inner_letter = {inner_letter}

# Output list!
null_letters = letters - outer_letters - inner_letter
all_words_copy = all_words
for null_letter in null_letters:
    all_words_copy -= dictionary[null_letter]

all_words_copy = list(all_words_copy)


output = []
for word in all_words_copy:
    if len(word) > 4 and inner_letter_word in word:
        output.append(word)

print(output)