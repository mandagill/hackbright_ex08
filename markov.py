#!/usr/bin/env python
import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    corpus_as_string = corpus.read().split()
    chain_dict = {}
    
    for i in range(len(corpus_as_string)-2):
        if (corpus_as_string[i],corpus_as_string[i + 1]) not in chain_dict:
            chain_dict[(corpus_as_string[i], corpus_as_string[i +1])] = [corpus_as_string[i +2]]          
        else:
            chain_dict[(corpus_as_string[i], corpus_as_string[i + 1])].append(corpus_as_string[i + 2])
 
    return chain_dict  

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    while True:
        first_key = random.choice(chains.keys())
        #first_key is a tuple; first_value is a list of possible continuations
        word1, word2 = first_key
        if word1[0].isupper():
            break

    words_to_be_chained = [word1, word2]
    punctuation = ['.', '?', '!']

    while True:
        search_tuple = (words_to_be_chained[-2], words_to_be_chained[-1])
        if search_tuple in chains:
            possible_next_words = chains[search_tuple]
            definite_next_word = random.choice(possible_next_words)
            words_to_be_chained.append(definite_next_word)
            if definite_next_word[-1] in punctuation:
                break
        else:    
            break

    final_chained_string = " ".join(words_to_be_chained)

    return final_chained_string

def main():

    # Initially, we didn't slice the arguments on the line below and it would pass the script as text as a function parameter. Interesting snafu.
    args = sys.argv[1:]
    master_dictionary = {}

    for i in range(len(args)):
        input_text_raw = open(args[i])
        dictionary_of_words = make_chains(input_text_raw)
        master_dictionary = dict(master_dictionary.items() + dictionary_of_words.items())

    random_text = make_text(master_dictionary)
    print random_text

if __name__ == "__main__":
    main()
