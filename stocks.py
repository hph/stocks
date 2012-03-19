#!/usr/bin/env python
# coding=utf-8

import sys
import urllib

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

