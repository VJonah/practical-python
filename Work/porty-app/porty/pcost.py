# pcost.py
#
# Exercise 1.27
#
import csv
import sys
from . import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) for a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
    return total


def main(argv):
    if len(argv) != 2:
        raise SystemExit('Usage: %s portfoliofile' %args[0])
    filename = argv[1]
    cost = portfolio_cost(filename)
    print(f"Total cost {cost:0.2f}")

if __name__ == '__main__':
    import sys
    main(sys.argv)
