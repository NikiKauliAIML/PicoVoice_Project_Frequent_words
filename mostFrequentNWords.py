import collections
import nltk
from nltk.corpus import stopwords
import streamlit as st

# Download the stopword and punkt
nltk.download("punkt")

def find_frequent_words(path, n, remove_stopword):
  """Finds the n most frequent words in the TensorFlow Shakespeare dataset.

  Args:
    path: Path to the Shakespeare dataset file.
    n: Number of most frequent words to find.
    remove_stopword: Remove the stopwords like is, are, an, a, etc... from the dataset

  output:
    A list of the n most frequent words.
  """

  # Load and read the dataset
  data = open(path, 'rb').read().decode(encoding='utf-8')

  # Preprocess text data
  text = data.lower()
  text = data.replace('\n', ' ')

  # remove stopword from dataset using NLP preprocesing method
  if remove_stopword:
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    all_words = [word for word in words if word.isalnum() and word not in stop_words]

  else:
    all_words = text.split()

  # count number of n frequnet word usinf counter method
  freq_word_count = collections.Counter(all_words)

  # Get the fequent words
  freq_words = freq_word_count.most_common(n)
  return [words for words, count in freq_words]

# Main function to give the input using streamlit and calculate most frequent words

def main():
  # Title of page
  st.title("Frequent Word Count")

  # Take the input using stremlit input method
  freq_word = st.number_input("Enter the number of n frequnet word: ", min_value=1)
  enable_stopword = st.checkbox("Remove Stopwords in dataset")

  # Select the run button to run code
  if st.button("Run"):
    # Input dataset
    path_to_file = 'shakespeare.txt'

    # call the function
    frequent_words = find_frequent_words(path_to_file, freq_word, enable_stopword)

    # Display the output in list with words and count of words
    print(frequent_words)
    st.write("Most Frequnet Words: " )
    st.write(frequent_words)


if __name__ == "__main__":
  main()