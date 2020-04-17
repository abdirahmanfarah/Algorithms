#!/usr/bin/python

import sys


# def rock_paper_scissors_helper(rock):
#     # base case is an empty array and a [['rock'], ['paper'], ['scissors']]


# def rock_paper_scissors(n):
#     # empty list to return later
#     all_plays = []

#     # the words I want to loop through
#     rock = ['rock', 'paper', 'scissors']
#     # pass in recursion helper function which loops through rock
#     # and based on the n provided, makes combinations based on it
#     # return list which contains all the possible plays
#     # We need to return a list of lists, and the inner list should have a len(arr) = n
#     pass


def rock_paper_scissors(n):
    outcomes = []
    plays = ['rock', 'paper', 'scissors']

    def find_outcome(rounds_left, result=[]):
        if rounds_left == 0:
            outcomes.append(result)
            return
        for play in plays:
            find_outcome(rounds_left - 1, result + [play])
    find_outcome(n, [])
    return outcomes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
