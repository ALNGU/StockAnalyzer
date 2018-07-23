import pandas as pd
from YahooFinanceHistory import YahooFinanceHistory

df = YahooFinanceHistory('AAPL', days_back=30).get_quote()

print (df)
