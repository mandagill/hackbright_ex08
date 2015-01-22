#!/usr/bin/env python
import sys
import random

def make_chains(corpus, n_gram_size):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    corpus_as_string = corpus.read().split()
    chain_dict = {}

    
    c = corpus_as_string
    n = n_gram_size

    for i in range(len(c)-n):
        if (tuple(c[i:i + n])) not in chain_dict:
            chain_dict[(tuple(c[i:i + n]))] = [c[i + n]]          
        else:
            chain_dict[(tuple(c[i:i + n]))].append(c[i + n])
  
    return chain_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # This is so that each new string within the newly generated text
    # begins with a capital letter and so is grammatically correct.
    while True:

        first_key = random.choice(chains.keys())
        if first_key[0][0].isupper():
            break

    words_to_be_chained = []

    for each_word in first_key:
        words_to_be_chained.append(each_word)

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

    file_paths = sys.argv[1:]
    master_dictionary = {}
    n_gram_size = int(raw_input("How long should the n-gram be? "))

    for i in range(len(file_paths)):
        input_text_raw = open(file_paths[i])
        dictionary_of_words = make_chains(input_text_raw, n_gram_size)
        print dictionary_of_words
        # master_dictionary = dict(master_dictionary.items() + dictionary_of_words.items())

    # random_text = make_text(master_dictionary)
    # print random_text

if __name__ == "__main__":
    main()
