#!/usr/bin/env python

import sys
import random


def make_chains():
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    corpus = open("Palinator.txt")
    corpus_dict = {}
    read_file = corpus.read()
    split_file = read_file.split()

    for i in range(len(split_file) -2):
        if (split_file[i], split_file[i + 1]) in corpus_dict: 
            value = corpus_dict[(split_file[i], split_file[i+1])] # = [words[i+1]]
            value.append(split_file[i +2])
            corpus_dict[(split_file[i], split_file[i + 1])] = value
        else: 
            #make new key, value entry in dict
            corpus_dict[(split_file[i], split_file[i +1])] = [split_file[i+2]]

    return corpus_dict

def make_text(chains):
# #     """Takes a dictionary of markov chains and returns random text
# #     based off an original text."""
    
    #creates a list of keys for starting point
    key_list =[]
    for k in chains.keys():
        key_list.append(k)

    #eventual string structure for markov sentence
    markov_output_string = ""

    while True:
        #create a starting key tuple
        starting_point = random.choice(key_list)
        if starting_point[0][0].isupper():
            markov_output_string += starting_point[0] + " " + starting_point[1] + " "
            key = starting_point
            # print "key=", key
            chain_one = random.choice(chains[key])
            # print "chain_one =", chain_one
            next_tuple = (key[1], chain_one)
            markov_output_string += chain_one + " "
            # print "this is the markov string =", markov_output_string
            #print "what the next tuple will look like =", next_tuple
            break

    while len(markov_output_string) <= 125:
        next_value = random.choice(chains[next_tuple])
        markov_output_string += next_value + " "
        # print markov_out put_string
        next_tuple = (next_tuple[1], next_value)
    return markov_output_string + "..."

def main():
    chain_dict = make_chains()
    make_text(chain_dict)

if __name__ == "__main__":
     main()