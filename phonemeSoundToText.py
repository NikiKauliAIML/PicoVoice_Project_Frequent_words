"""
Problem Statement:
phoneme is a sound unit (similar to a character for text). We have an extensive pronunciation
dictionary (think millions of words). Below is a snippet:
ABACUS AE B AH K AH S
BOOK B UH K
THEIR DH EH R
THERE DH EH R
TOMATO T AH M AA T OW
TOMATO T AH M EY T OW
Given a sequence of phonemes as input (e.g. ["DH", "EH", "R", "DH", "EH", "R"]), find all the combinations of the words that
can produce this sequence (e.g. [["THEIR", "THEIR"], ["THEIR", "THERE"], ["THERE", "THEIR"], ["THERE", "THERE"]]). You can
preprocess the dictionary into a different data structure if needed.

Overview:

        - phonemes : Phonemes is sequence of words
        - pronunciation_dict: Dictonary of words with phonemes 
        
        Find the combinations of words from phonemes       

Args: 
        -   input_phonemes : List or sequence of shape (Phonemes[]) containing the phonemes

        -   phonemes_dict : dict of shape containing kay value pair - (word(Key) - phoenems(Value))
        

"""
# Here I used the defaultdict library for inputs

# import the defaultdict
from collections import defaultdict

class Tree:
    def __init__(self):
        self.child = defaultdict(Tree)
        self.words = []

# Build a tree for given dictonary words
def construct_tree(words_dict):
    root = Tree()
    for word, phonemes in words_dict.items():
        element = root
        for p in phonemes:
            element = element.child[p]
        element.words.append(word)
    return root 
            
# Find the word combination of phoneme in given list
def find_word_combos_with_pronunciation(phonemes_seq, input_phonemes):
    def combination(i, current_words, output):
        if i == len(input_phonemes):
            output.append(current_words.copy())
            return
        
        element = phonemes_seq

        for phoneme in input_phonemes[i]:
            if phoneme not in element.child:
                return
            element = element.child[phoneme]

        for word in element.words:
            combination(i + 1, current_words + [word], output)

    output = []
    combination(0, [], output)
    return output

def add_word_to_dict(word, phonemes):
    phonemes_dict[word] = phonemes



# pronunciation Dictonary of worlds
phonemes_dict = {
    "ABACUS": ["AE", "B", "AH", "K", "AH", "S"],
    "BOOK": ["B", "UH", "K"],
    "TOMATO": ["T", "AH", "M", "EY", "T", "OW"],
    "THEIR": ["DH", "EH", "R"],
    "THERE": ["DH", "EH", "R"],
    "TOMATO": ["T", "AH", "M", "AA", "T", "OW"],
    "ANALOGUE": ["AE", "N", "AH", "L", "AO", "G"],
    "ADVANTAGE": ["AE", "D", "V", "AE", "N", "T", "IH", "JH"],
    "AIDE": ["EY", "D"],
    "AID":["EY", "D"],
    "GUIDANCE":["G", "AY", "D", "AH", "N", "S"],
    "WITHOUT": ["W", "IH", "TH", "AW", "T"],
    "PROJECT": ["P", "R", "AA", "JH", "EH", "K", "T"]
}

words_dict = construct_tree(phonemes_dict)
input_phonemes = [["P", "R", "AA", "JH", "EH", "K", "T"]]


combinations = find_word_combos_with_pronunciation(words_dict, input_phonemes)
print(combinations)



# def main():
#     st.title("Phoneme Dictionary")

#     st.write("Existing Phoneme Dictionary:")
#     st.json(phonemes_dict)

#     # word = st.text_input("Enter a word:")
#     phonemes1 = st.text_input("Enter phonemes (separated by commas):")

#     if st.button("Output"):
#         st.write(phonemes_dict.values())
#         for phonemes1 in phonemes_dict.values():
           
#             st.write(combinations)
#         else:
#             st.write("Not")



#     # if st.button("Add Word"):
#     #     if word and phonemes:
#     #         phonemes_list = phonemes.split(",")
#     #         add_word_to_dict(word, phonemes_list)
#     #         st.success("Word added successfully!")
#     #     else:
#     #         st.warning("Please enter both word and phonemes.")

#     # st.write("Updated Phoneme Dictionary:")
#     # st.json(phonemes_dict)

# if __name__ == "__main__":
#     main()
    
