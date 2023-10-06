# fileparse.py
#
# Exercise 3.3

import csv
import logging
log = logging.getLogger(__name__)


def parse_csv(lines,select=None,types=None,has_headers=True,delimiter=',',silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    rows = csv.reader(lines,delimiter=delimiter)
    #with open(filename) as f:
        #rows = csv.reader(f,delimiter=delimiter)

    # Read the file headers
    headers = next(rows) if has_headers else []

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for i,row in enumerate(rows,start=1):
        if not row: # Skip rows with no data
            continue
        # Filter the row if specific columns were selected
        if select:
            row = [row[i] for i in indices]

        # If a types list was given, apply the type conversions to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types,row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row: %d: Couldn't convert %s", i,row)
                    log.debug("Row: %d: Reason %s", i,e)
                continue
        if has_headers:
            # Make a dictionary
            record = dict(zip(headers,row))
        else:
            record = tuple(row)
        records.append(record)
    return records
