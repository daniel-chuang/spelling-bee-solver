# Imports
import streamlit as st
import pandas as pd
import random

# Functions


def find_words(optional_letters, mandatory_letters):

    # Reading the file
    all_words_file = open("corncob_lowercase.txt", "r")

    # Adding all the words into a set
    all_words = set()
    for line in all_words_file:
        all_words.add(line.strip())

    # Creating a set of all letters
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

    # The optional letter, which can be used in the word
    optional_letters = {letter for letter in optional_letters}

    # The mandatory letter, which must be in the word
    mandatory_letters = {letter for letter in mandatory_letters}

    # Subtracts each unused letter set from the universal set of all words
    null_letters = letters - optional_letters - mandatory_letters
    for null_letter in null_letters:
        all_words -= dictionary[null_letter]

    # Makes sure that each word has both mandatory letters
    for mandatory_letter in mandatory_letters:
        all_words = all_words.intersection(dictionary[mandatory_letter])

    # Checks if the word is four letters or greater, then adds it to the outputs if it is!
    all_words = list(all_words)
    output = []
    for word in all_words:
        if len(word) > 3:
            output.append(word)

    return(output)


# Website frontend
st.set_page_config(page_title="NYT Bee Solver!", page_icon=None, layout="wide", initial_sidebar_state="auto")

# Title
st.write(
    """
    # NYT Spelling Bee Solver by [Daniel Chuang](https://github.com/daniel-chuang)
    Solves the daily [New York Times Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee) challenge!
    
    ## Screenshot of Game
    """
)

# Inserts a screenshot of the game!
st.image("spelling_bee_solver.png")

# Instructions for Game
st.sidebar.write("# FAQ")
with st.sidebar.expander("What is the New York Times Spelling Bee Game?", expanded=False):
    st.write(
        """
    [Link to Official Instructions](https://www.nytimes.com/2021/07/26/crosswords/spelling-bee-forum-introduction.html)

    - Words must include the center letter.

    - Words must contain at least four letters.

    - Letters can be used more than once.

    - Our word list does not include words that are offensive, obscure, hyphenated or proper nouns.

    - Four-letter words are worth one point each.

    - Longer words earn one point per letter. A six-letter word is worth six points.

    - Each puzzle includes at least one ???pangram,??? which uses every letter at least once. A pangram is worth an additional seven points."
    """
    )

# Instructions for Website Usage
with st.sidebar.expander("How do I use this website?", expanded=False):
    st.write(
        """
        Input all of the optional letters, then all of the mandatory letters, and an output will come out! 
        """
    )

# The input form for the optional and mandatory letters
letters = {
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    }

st.write("# Solver")
optional_letters = st.text_input("What are the optional letters?").lower()
mandatory_letters = st.text_input("What are the mandatory letters?").lower()
output = find_words(optional_letters, mandatory_letters)

# Allows the user to select different sorting methods for the list
with st.expander("Advanced Options", expanded=False):
    col1, col2 = st.columns(2)
    sorted_by = col1.selectbox(
        "Sort list by", ["A-Z", "Z-A", "Length Increasing", "Length Decreasing"])
    output_format = col2.selectbox(
        "Format data in", ["Text", "Dataframe", "List (For Copy Paste)"]
    )

# Sorts the output list
output = list(output)
if sorted_by == "A-Z":
    output = sorted(output)
elif sorted_by == "Z-A":
    output = sorted(output, reverse=True)
elif sorted_by == "Length Increasing":
    output = sorted(output, key=len)
elif sorted_by == "Length Decreasing":
    output = sorted(output, key=len, reverse=True)

# Displays the output!
st.write("# Results")
if output_format == "Text":
    st.write(str(output)[1:-2].replace("'", ""))
elif output_format == "Dataframe":
    output = pd.DataFrame(output)
    output.index = [""] * len(output)
    st.dataframe(output, width=None, height=99999999)
else:
    st.write(output)


# Explaination of the program for SWAG people
with st.sidebar.expander("How does it work?", expanded=False):
    st.write(
        r"""
        Using a [list of almost all of the words in the English language](http://www.mieliestronk.com/wordlist.html), the program creates 26 sets of words, each set representing all of the words that include one of the 26 letters anywhere in the word.

        In order to find the final list, the program removes all words that have letters outside of the entered letters. Then, it takes the intersection of the mandatory letters with the remaining list. Finally, it removes any results that are under 4 letters long!

        Another way to do it is by iterating through all of the combinations of the letters, but that is inefficient:
        
        The $O(n)$ of iteration is really high (and it needs to be performed up to the length of the longest english word), and the search into the set of all words is $O(1)$. This means it would take a REALLY long time.
        
        On the other hand, the $O(n)$ of sets operators is $O(|S_1| + |S_2|)$. This operation happens multiple times, but it's quite quick overall. The iteration through all of the final candidates to select words over length 4 is $O(n)$, but n is really small, so that is nearly negligable.
        """
    )

# Self-plug
with st.sidebar.expander("Where can I see more of your projects?", expanded=False):
    st.write(
        """
        Here's my personal website: [https://sites.google.com/view/daniel-chuang/home](https://sites.google.com/view/daniel-chuang/home)

        Here's my GitHub: [https://github.com/daniel-chuang](https://github.com/daniel-chuang)

        Here's the code for this project: [https://github.com/daniel-chuang/spelling-bee-solver](https://github.com/daniel-chuang/spelling-bee-solver)
        
        Thanks for using this website!
        """
    )