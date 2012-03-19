#!/usr/bin/env python
# coding=utf-8

import sys
import urllib

# The following dict contains descriptions of possible options used.
OPTIONS = {'a' : 'Ask',
           'a2': 'Av. daily volume',
           'a5': 'Ask size',
           'b' : 'Bid',
           'b2': 'Ask (real-time)',
           'b3': 'Bid (real-time)',
           'b4': 'Book value',
           'b6': 'Bid size',
           'c' : 'Change',
           'c1': 'Change',
           'c3': 'Commission',
           'c6': 'Change (real-time)',
           'c8': 'After hours change (real-time)',
           'd' : 'Dividend/share',
           'd1': 'Last trade date',
           'd2': 'Trade date',
           'e' : 'Earnings/share',
           'e1': 'Error indication',
           'e7': 'EPS est. current year',
           'e8': 'EPS est. next year',
           'e9': 'EPS est. next quarter',
           'f6': 'Float shares',
           'g' : 'Day\'s low',
           'h' : 'Day\'s high',
           'j' : '52-week low',
           'k' : '52-week high',
           'g1': 'Holdings gain',
           'g3': 'Annualized gain',
           'g4': 'Holdings gain',
           'g5': 'Holdings gain (real-time)',
           'g6': 'Holdings gain (real-time)',
           'i' : 'More info',
           'i5': 'Order book (real-time)',
           'j1': 'Market capitalization',
           'j3': 'Market capitalization (real-time)',
           'j4': 'EBITDA',
           'j5': 'Change from 52-week low',
           'j6': 'Change from 52-week low',
           'k1': 'Last trade (real-time)',
           'k2': 'Change (real-time)',
           'k3': 'Last trade size',
           'k4': 'Change from 52-week high',
           'k5': 'Change from 52-week high',
           'l' : 'Last trade',
           'l1': 'Last trade',
           'l2': 'High limit',
           'l3': 'Low limit',
           'm' : 'Day\'s range',
           'm2': 'Day\'s range (real-time)',
           'm3': '50-day moving average',
           'm4': '200-day moving average',
           'm5': 'Change from 200-day moving average',
           'm6': 'Change from 200-day moving average',
           'm7': 'Change from 50-day moving average',
           'm8': 'Change from 50-day moving average',
           'n' : 'Name',
           'n4': 'Notes',
           'o' : 'Open',
           'p' : 'Previous close',
           'p1': 'Price paid',
           'p2': 'Change',
           'p5': 'Price/sales',
           'p6': 'Price/book',
           'q' : 'Ex-dividend date',
           'r' : 'P/E ratio', 
           'r1': 'Dividend pay date',
           'r2': 'P/E ratio (real-time)',
           'r5': 'PEG ratio',
           'r6': 'Price/EPS estimate current year',
           'r7': 'Price/EPS estimate next year',
           's' : 'Symbol',
           's1': 'Shares owned',
           's7': 'Short ratio',
           't1': 'Last trade',
           't6': 'Trade links',
           't7': 'Ticker trend',
           't8': '52-week target estimate',
           'v' : 'Volume',
           'v1': 'Holding\'s value',
           'v7': 'Holding\'s value (real-time)',
           'w' : '52-week range',
           'w1': 'Day\'s value change',
           'w4': 'Day\'s value change (real-time)',
           'x' : 'Stock exchange',
           'y' : 'Dividend & yeild'}

def get_data(symbols, options, filename='stocks.csv'):
    '''Save data to file.'''
    head = 'http://finance.yahoo.com/d/quotes.csv?s=' + symbols
    tail = '+&f=' + options
    try:
        data = urllib.urlopen(head + tail).read()
        open(filename, 'w').write(data)
    except:
        # Infinite loop - find a way to handle possible errors.
        get_data(symbols, options, filename)

def strip_chars(string, chars):
    '''Remove chars from string.'''
    return ''.join(char for char in string if char not in chars)

def parse_data(filename='stocks.csv'):
    '''Parse the csv file.'''
    data = []
    tmp_lst = []
    tmp_str = ''
    with open(filename) as file:
        for line in file:
            for char in line:
                if char not in ',\r\n':
                    tmp_str += char
                elif tmp_str != '':
                    tmp_lst.append(strip_chars(tmp_str, '"'))
                    tmp_str = ''
            data.append(tmp_lst)
            tmp_lst = []
    return data

def repr_data(data):
    '''Print data in a concrete manner.'''
    for stock in data:
        print '%s' % stock[0]
        print 'Last trade:  %s \t Change:       %s' % (stock[1], stock[2])
        print 'Day\'s low:   %s \t Day\'s high:   %s' % (stock[3], stock[4])
        print '52-week low: %s \t 52-week high: %s' % (stock[5], stock[6])
        print '1 yr target: %s\n' % stock[7]

def main():
    get_data('aapl+goog+msft+brk-a+aa+yhoo', 'sl1p2ghjkt8')
    repr_data(parse_data())

if __name__ == '__main__':
    main()

