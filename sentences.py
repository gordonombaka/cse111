"""
Author: Gordon Ombaka
Date: 19th October 2024
Week 03 Prove Assignment

Write a Python program named sentences.py that generates simple English sentences. 
During this prove milestone, you will write functions that generate sentences with three parts:

a determiner (sometimes known as an article)
a noun
a verb
For example:

A cat laughed.
One man eats.
The woman will think.

For this milestone, your program must include at least these five functions:

main
make_sentence
get_determiner
get_noun
get_verb
"""
import random

def main():

    def get_determiner(quantity):
  """
    Return a randomly chosen determiner. A determiner is
    a word like 'the', 'a', 'one', 'some', 'many'.
    If quantity is 1, this function will return either 'a',
    'one', or 'the'. Otherwise this function will return
    either 'some', 'many', or 'the'.

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

main()




