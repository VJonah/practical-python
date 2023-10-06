# report.py
#
# Exercise 2.4


import csv
from . import fileparse
from . import tableformat
from .portfolio import Portfolio


def read_portfolio(filename,**opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price
    '''
    with open(filename,'rt') as lines:
        return  Portfolio.from_csv(lines)

def read_prices(filename):
    #prices = {}
    #with open(filename, 'rt') as f:
        #rows = csv.reader(f)
        #for row in rows:
            #if row != []:
                #prices[row[0]] = float(row[1])
    with open(filename,'rt') as f:
       prices =  fileparse.parse_csv(f,types=[str,float],has_headers=False)
    prices = dict(prices)
    return prices

def make_report(portfolio,prices):
    report = []
    for s in portfolio:
        price = prices[s.name]
        change =  prices[s.name] -  float(s.price)
        row = s.name,int(s.shares),prices[s.name],change
        report.append(row)
    return report

def print_report(reportdata,formatter):
    '''
    Print a nicely formatted table from a list of (name,shares,price,change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    #print("%10s %10s %10s %10s" % headers)
    #print(f"{'':->10} " * len(headers))
    for name, shares, price, change in reportdata:
        rowdata = [name,str(shares),f"{'$'+f'{price:0.2f}'}",f"{change:0.2f}"]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename,prices_filename,fmt='txt'):
    '''
    Make a stock report given portfolio and price data files
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create the report data
    report = make_report(portfolio,prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report,formatter)

def main(argv):
    if len(argv) == 3:
        portfolio_report(argv[1],argv[2])
    elif len(argv) == 4:
        portfolio_report(argv[1],argv[2],fmt=argv[3])
    else:
        raise SystemExit('Usage: %s portfile pricefile' % argv[0])

if __name__ == '__main__':
    import sys
    import logging
    # This file sets up basic configuration of the logging module.
    # Change settings here to adjust logging output as needed.
    logging.basicConfig(
        filename = 'app.log',            # Name of the log file (omit to use stderr)
        filemode = 'w',                  # File mode (use 'a' to append)
        level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
    )

    main(sys.argv)
