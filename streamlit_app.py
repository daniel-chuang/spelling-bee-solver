# Imports
import streamlit as st

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
    all_words = all_words
    for null_letter in null_letters:
        all_words -= dictionary[null_letter]

    # Adds all of the words that fit the requirements into the output list
    all_words = list(all_words)
    output = []
    for word in all_words:
        if len(word) > 3: # Checks if the word is four letters or greater
            output.append(word)
            for mandatory_letter in mandatory_letters: # checks if both mandatory letters are inside
                if mandatory_letter not in word:
                    output.remove(word)
                    break



    return(output)


# Website frontend
st.write(
    """
    # NYT Spelling Bee Solver
    Solves the daily [New York Times Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee) challenge!
    """
)

# Inserts a screenshot of the game!
st.image("spelling_bee_solver.png")

# Instructions for Game
with st.expander("What is the New York Times Spelling Bee Game?", expanded=False):
    st.write(
        """
    [Link to Official Instructions](https://www.nytimes.com/2021/07/26/crosswords/spelling-bee-forum-introduction.html)

    - Words must include the center letter.

    - Words must contain at least four letters.

    - Letters can be used more than once.

    - Our word list does not include words that are offensive, obscure, hyphenated or proper nouns.

    - Four-letter words are worth one point each.

    - Longer words earn one point per letter. A six-letter word is worth six points.

    - Each puzzle includes at least one “pangram,” which uses every letter at least once. A pangram is worth an additional seven points."
    """
    )

# Instructions for Website Usage
with st.expander("How do I use this website?", expanded=False):
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
sorted_by = st.selectbox(
    "Sort list by", ["A-Z", "Z-A", "Length Down", "Length Up"])

# Sorts the output list
output = list(output)
if sorted_by == "A-Z":
    output = sorted(output)
elif sorted_by == "Z-A":
    output = sorted(output, reverse=True)
elif sorted_by == "Length Down":
    output = sorted(output, key=len)
elif sorted_by == "Length Up":
    output = sorted(output, key=len, reverse=True)
st.write(output)


# Explaination of the program for SWAG people
st.write("# For the curious")
with st.expander("How does it work?", expanded=False):
    st.write(
        r"""
        Using a [list of almost all of the words in the English language](http://www.mieliestronk.com/wordlist.html), the program creates 26 sets of words, each set representing all of the words that include one of the 26 letters anywhere in the word.

        In order to find the final list, the program makes a union between all the sets of the optional letters, then intersects that with the set of the mandatory letter. Remember, union is to *or* as intersect is to *and*.

        Another way to do it is by iterating through all of the combinations of the letters, but that is inefficient:
        
        The $O(n)$ of iteration is really high (and it needs to be performed up to the length of the longest english word), and the search into the set of all words is $O(1)$. This means it would take a REALLY long time.
        
        On the other hand, the $O(n)$ of sets operators is $O(|S_1| + |S_2|)$. This operation happens multiple times, but it's quite quick overall. The iteration through all of the final candidates to select words over length 4 is $O(n)$, but n is really small, so that is nearly negligable.
        """
    )

# Self-plug
with st.expander("Where can I see more of your projects?", expanded=True):
    st.write(
        """
        Here's my personal website: [https://sites.google.com/view/daniel-chuang/home](https://sites.google.com/view/daniel-chuang/home)

        Here's my GitHub: [https://github.com/daniel-chuang](https://github.com/daniel-chuang)

        Here's the code for this project: [https://github.com/daniel-chuang/spelling-bee-solver](https://github.com/daniel-chuang/spelling-bee-solver)
        
        Thanks for using this website!
        """
    )