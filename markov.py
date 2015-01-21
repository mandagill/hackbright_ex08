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
    
    print master_list

#     chain_dict = {}
#     for word in corpus:
#         if (corpus[0],corpus[1]) not in chain_dict:
#             chain_dict = {(corpus[0], corpus[1]):[corpus[2]]}          
#         else:
#             chain_dict[(corpus[0], corpus[1])].append(corpus[2])
#         corpus.pop(0)
    
#     print corpus    
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
