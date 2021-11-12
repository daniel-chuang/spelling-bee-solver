"""
SPELLING BEE

Words must include the center letter.

Words must contain at least four letters.

Letters can be used more than once.

Our word list does not include words that are offensive, obscure, hyphenated or proper nouns.

Four-letter words are worth one point each.

Longer words earn one point per letter. A six-letter word is worth six points.

Each puzzle includes at least one “pangram,” which uses every letter at least once. A pangram is worth an additional seven points.
"""

import streamlit as st

def find_words(optional_letters, mandatory_letter):

    # Getting words
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

    # The optional letter, which can be used in the word
    optional_letters = {letter for letter in optional_letters}

    # The mandatory letter, which must be in the word
    mandatory_letter_word = mandatory_letter
    mandatory_letter = {mandatory_letter}

    # Output list!
    null_letters = letters - optional_letters - mandatory_letter
    all_words_copy = all_words
    for null_letter in null_letters:
        all_words_copy -= dictionary[null_letter]

    all_words_copy = list(all_words_copy)


    output = []
    for word in all_words_copy:
        if len(word) > 4 and mandatory_letter_word in word:
            output.append(word)

    return(output)

# Main website frontend
st.write(
    """
    # NYT Spelling Bee Solver
    Solves the daily [New York Times Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee) challenge!
    """
)
optional_letters=st.text_input("What are the optionalional letters?")
mandatory_letter=st.text_input("What are the mandatory letters?")
output = find_words(optional_letters, mandatory_letter)

sorted_by=st.selectbox("Sort by", ["A-Z", "Z-A", "Length Down", "Length Up"])

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

with st.expander("How does it work?", expanded=True):
    st.write(
        r"""
        Using a [list of almost all of the words in the English language](http://www.mieliestronk.com/wordlist.html), the program creates 26 sets of words, each set representing all of the words that include one of the 26 letters anywhere in the word.

        In order to find the final list, the program makes a union between all the sets of the optional letters, then intersects that with the set of the mandatory letter. Remember, union is to *or* as intersect is to *and*.

        Another way to do it is by iterating through all of the combinations of the letters, but that is inefficient:
        
        The $O(n)$ of iteration is really high (and it needs to be performed up to the length of the longest english word), and the search into the set of all words is $O(1)$. This means it would take a REALLY long time.
        
        On the other hand, the $O(n)$ of sets operators is $O(|S_1| + |S_2|)$. This operation happens multiple times, but it's quite quick overall. The iteration through all of the final candidates to select words over length 4 is $O(n)$, but n is really small, so that is nearly negligable.
        """
    )
