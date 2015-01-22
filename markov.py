#!/usr/bin/env python
import sys

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
    
    print chain_dict    
#     return corpus

# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""
#     return "Here's some random text."

def main():
    args = sys.argv
    # Change this to read input_text from a file
    input_text = (args[1])
    opened = open(input_text)
    make_chains(opened)

    # chain_dict = make_chains(input_text)
    # random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()
