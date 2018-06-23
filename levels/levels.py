from nsepy import get_history
from datetime import date, datetime, timedelta
import pandas as pd

class Levels:

    def __init__(self, symbol, start=date(2015, 1, 1), end=date(2015, 1, 10)):
        self.symbol = symbol
        self.start_date = start
        self.end_date = end

    def get_index_price_history(self):
        start = self.start_date - timedelta(days=7)
        self.data = get_history(symbol=self.symbol, start=start, end=self.end_date, index=True)

    def angles(self):
        # get all the highs
        high = self.data['High'].values.tolist()
        low = self.data['Low'].values.tolist()
        close = self.data['Close'].values.tolist()

        # take only relevant highs
        num_of_days = pd.bdate_range(self.start_date, self.end_date).size
        num_of_days += 2
        high = high[-num_of_days::1]
        close = close[-num_of_days::1]
        low = low[-num_of_days::1]

        # loop through start date to end date and find averages
        i = 0
        j = 1
        k = 2
        final_data = {}
        for single_date in pd.bdate_range(self.start_date, self.end_date):
            final_data[single_date.strftime("%Y-%m-%d")] = {}
            final_data[single_date.strftime("%Y-%m-%d")]["h2"] = str(self.averages(high[j:j+2]))
            final_data[single_date.strftime("%Y-%m-%d")]["h3"] = str(self.averages(high[i:i+3]))
            final_data[single_date.strftime("%Y-%m-%d")]["c2"] = str(self.averages(close[j:j+2]))
            final_data[single_date.strftime("%Y-%m-%d")]["c3"] = str(self.averages(close[i:i+3]))
            final_data[single_date.strftime("%Y-%m-%d")]["l2"] = str(self.averages(low[j:j+2]))
            final_data[single_date.strftime("%Y-%m-%d")]["l3"] = str(self.averages(low[i:i+3]))

            final_data[single_date.strftime("%Y-%m-%d")]["g1"] = str(self.gann_angle(high[k], close[k]))
            final_data[single_date.strftime("%Y-%m-%d")]["g2"] = str(self.gann_angle(close[k], low[k]))
            final_data[single_date.strftime("%Y-%m-%d")]["g3"] = str(self.gann_angle(low[k], close[k]))
            final_data[single_date.strftime("%Y-%m-%d")]["g4"] = str(self.gann_angle(close[k], high[k]))

            i, j, k = i+1, j+1, k+1

        return final_data

    def averages(self, prices_list=[]):
        total = 0
        for x in prices_list:
            total += x 
        
        return round(total/len(prices_list), 3)
    
    def gann_angle(self, n1, n2):
        return round((n1*2 - n2), 3)
