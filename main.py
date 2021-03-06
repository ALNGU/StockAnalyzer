import pandas as pd
import csv
from collections import defaultdict
from YahooFinanceHistory import YahooFinanceHistory

#companylist.csv contains all of the ticker symbols and a lot of other info
#that may or may not be useful later on

def main():
   tickerList = getTickers()
   dfList = getStockData(tickerList)
   print (dfList)


def getStockData(tickerList):
   dfList = list()
   for tickerSymbol in tickerList:
      try:
         df = YahooFinanceHistory(tickerSymbol, days_back=30).get_quote()
         dfList.append(df)
      except:
         print("could not find " + tickerSymbol)
   return dfList

# returns a list of tickers
def getTickers():

   columns = defaultdict(list) # each value in each column is appended to a list

   with open('companylist.csv') as f:
       reader = csv.DictReader(f) # read rows into a dictionary format
       for row in reader: # read a row as {column1: value1, column2: value2,...}
           for (k,v) in row.items(): # go over each column name and value
               columns[k].append(v) # append the value into the appropriate list
                                    # based on column name k
   #print(columns['Symbol'])
   return (columns['Symbol'])


if __name__ == "__main__": main()
