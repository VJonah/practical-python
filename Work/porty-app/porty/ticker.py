# ticker.py

import csv
from . import report
from .follow import follow
from .tableformat import create_formatter


def select_columns(rows,indices):
    '''
    Filter a series of rows by select column indices.
    '''
    for row in rows:
        yield [row[index] for index in indices]



def convert_types(rows,types):
    '''
    Convert data in rows
    '''
    for row in rows:
        yield [func(val) for func,val in zip(types,row)]

def make_dicts(rows,headers):
    '''
    Make a dictionary out of a row and list of header names
    '''
    for row in rows:
        yield dict(zip(headers,row))
#def filter_symbols(rows,names):
    #'''
    #Filter stocks based on their symbol names
    #'''
    #for row in rows:
        #if row['name'] in names:
            #yield row

def parse_stock_data(lines):
    '''
    Parse stock data to a list of values
    '''
    rows = csv.reader(lines)
    rows = select_columns(rows,[0,1,4])
    rows = convert_types(rows,[str,float,float])
    rows = make_dicts(rows,['name','price','change'])
    return rows

def ticker(portfile,logfile,fmt):
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = create_formatter(fmt)
    formatter.headings(['Name','Price','Change'])
    for rowdata in rows:
        formatter.row([rowdata['name'],f"{rowdata['price']:.2f}",f"{rowdata['change']:.2f}"])

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfoliofile logfile fmt' % args[0])
    ticker(args[1],args[2],args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
