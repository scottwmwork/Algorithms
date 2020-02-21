#!/usr/bin/python

import sys

def rock_paper_scissors(rounds):

  options = ['rock', 'paper', 'scissors']
  results = []
  if rounds == 0:
    return([[]])
  elif rounds == 1:
    return([['rock'], ['paper'], ['scissors']])
  else:

    for option in rock_paper_scissors(rounds-1):

      results.append((option + [options[0]]))
      results.append((option + [options[1]]))
      resilts.append((option + [options[2]]))

    return results

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')