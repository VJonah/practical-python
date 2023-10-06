# tableformat.py

# an example of an "abstract base class"
class TableFormatter:
    def headings(self,headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()
    def row(self,rowdata):
       '''
       Emit a single row of table data
       '''
       raise NotImplementedError()
class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self,headers):
        for h in headers:
            print(f'{h:>10s}',end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self,rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self,headers):
        print(','.join(headers))
    def row(self,rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''

    def headings(self,headers):
        print('<tr>',end='')
        for h in headers:
            print(f'<th>{h}</th>',end='')
        print('</tr>')
    def row(self,rowdata):
        print('<tr>',end='')
        for d in rowdata:
            print(f'<td>{d}</td>',end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(fmt):
    '''
    Create an appropriate formatter given a format name
    '''
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {fmt:s}')

def print_table(portfolio,attribute_list,formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(attribute_list)
    for stock in portfolio:
        rowdata = [str(getattr(stock,attr)) for attr in attribute_list]
        formatter.row(rowdata)
