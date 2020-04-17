#!/usr/bin/python

import argparse


# def find_max_profit(prices):
#     # declare variable to store position at sell value and buy value
#     x = 0
#     y = 0
#     # loop through the array to find biggest i value
#     for i in range(len(prices)):
#         # variable to store end profit
#         max_profit_so_far = max(prices) - min(prices)
#         # find min value and store it in position x
#         current_min_price_so_far = min(prices)
#         # if curr_min[i] is smaller then i + 1
#         if min(prices[i]) < max(prices[i])
#         max_profit = [max(prices) - min(prices)]

#     return max_profit
def find_max_profit(prices):
    # keep track of current min price and max profit so far
    # current_min_price = prices[0]
    # max profit = price - lowest price
    # current_min_price = prices[0]
    # current_max_profit = prices[1] - current_min_price
    # loop through prices
    current_min_price = prices[0]
    current_max_profit = prices[1] - current_min_price
    for i in range(1, len(prices)):
        if prices[i] < current_min_price:
            current_min_price = prices[i]
        elif current_max_profit < prices[i] - current_min_price:
            current_max_profit = prices[i] - current_min_price
    return current_max_profit
    # conditional - if current_min price > arr[i]
    # set current_min_price = arr[i]

    # buy price must be to the left of the biggest value
    # buy price is the smallest i value to the left of the sell price
    # subtract biggest value from smallest value
    # return this variable
# find_max_profit([10, 7, 5, 8, 11, 9])
find_max_profit([100, 90, 80, 50, 20, 10])

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

# def find_max_profit(prices):
#   min_price = prices[0]
#   max_profit = prices[1] - min_price

#   for i in range(1, len(prices)):
#     price = prices[i]
#     max_profit = max(price - min_price, max_profit)
#     min_price = min(price, min_price)

#   return max_profit
