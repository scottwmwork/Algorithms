#!/usr/bin/python

import argparse

def find_max_profit(prices):

  current_max = []

  for index1 in range(len(prices)):

    difference = 0

    for index2 in range(index1 + 1, len(prices)):

      difference = prices[index2] - prices[index1]

      if index1 == 0:
        current_max.append(difference)
      elif difference > current_max[len(current_max)-1]:
        current_max.append(difference)

  max_profit = current_max[len(current_max) - 1]
  
  return max_profit



# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()


# print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))