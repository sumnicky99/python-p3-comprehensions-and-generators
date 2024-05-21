#!/usr/bin/env python3

def return_evens(num_list):
    # Using list comprehension to filter out even numbers from num_list
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers

def make_exclamation(sentence_list):
    if not sentence_list:  # Check if the sentence_list is empty
        return []  # Return an empty list if it is empty
    else:
        # Using list comprehension to add exclamation mark to each sentence
        exclamated_sentences = [sentence + '!' for sentence in sentence_list]
        return exclamated_sentences
