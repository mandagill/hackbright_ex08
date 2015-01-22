#!/usr/bin/env python
import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    master_list = []
    for line in corpus:
        line = line.strip()
        line = line.split()
        if line != []:
            for word in line:
                master_list.append(word)

    chain_dict = {}
    
    counter = 0
    for word in master_list[:-2]:
        if (master_list[counter],master_list[counter + 1]) not in chain_dict:
            chain_dict[(master_list[counter], master_list[counter +1])] = [master_list[counter +2]]          
        else:
            chain_dict[(master_list[counter], master_list[counter + 1])].append(master_list[counter + 2])
        counter += 1
 
    # print chain_dict 
    return chain_dict  

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    first_key, first_value = random.choice(chains.items())
    #first_key is a tuple; first_value is a list of possible continuations
    word1, word2 = first_key
    new_list = [word1, word2]

    word3 = random.choice(first_value)
    new_list.append(word3)

    while True:
        search_tuple = (new_list[-2], new_list[-1])
        if search_tuple in chains:
            value = chains[search_tuple]
            word3 = random.choice(value)
            new_list.append(word3)
        else:    
            break

    new_string = " ".join(new_list)

    return new_string

def main():
    args = sys.argv
    input_text_raw = open(args[1])

    dictionary_of_values = make_chains(input_text_raw)
    random_text = make_text(dictionary_of_values)
    print random_text

if __name__ == "__main__":
    main()
