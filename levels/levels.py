from nsepy import get_history
from datetime import date, datetime, timedelta
import pandas as pd
from collections import d

class Camrilla:
    
    def __init__(self, high, low, close):
        self.high = high 
        self.low = low
        self.close = close 

    def r5(self):
        return round(( self.high  /  self.low * self.close ),2)
    
    def r4(self):
        return round( ( ( self.high / self.low + 0.83) / 1.83 * self.close ), 2 )

    def r3(self):
        return round( ( ( self.high / self.low + 2.66 ) / 3.66 * self.close ), 2 )

    def r2(self):
        return round( ( ( self.high / self.low + 4.5 ) / 5.5 * self.close ), 2 )

    def r1(self):
        return round( ( ( self.high / self.low + 10 ) / 11 * self.close ), 2)

    def s1(self):
        return round((-(((self.high / self.low + 10) / 11) - 2) * self.close), 2)

    def s2(self):
        return round( (-(((self.high / self.low + 4.5) / 5.5) - 2) * self.close), 2)

    def s3(self):
        return round( (-(((self.high / self.low + 2.66) / 3.66) - 2) * self.close), 2)

    def s4(self):
        return round((-(((self.high / self.low + 0.83) / 1.83) - 2) * self.close), 2)

    def s5(self):
        return round( (-(self.high / self.low - 2) * self.close), 2)

class Pivot:

    def __init__(self, high, low, close):
        self.high = high
        self.low = low
        self.close = close

    def pivot_levels(self):
        p = round( ((self.high+self.low+self.close) / 3), 2)
        pr1 = round(((2 * p) - self.low), 2)
        ps1 = round(((2 * p) - self.high), 2)
        ps2 = round((ps1 - (pr1 - p)), 2)
        pr2 = round(( pr1+(p-ps1) ), 2)
        pr3 = round((pr2+(ps1-ps2)), 2)
        ps3 = round(( ps2 - (pr2-pr1) ), 2)

        return {'pr1':pr1, 'pr2':pr2, 'pr3':pr3, 'p':p, 'ps1':ps1, 'ps2':ps2, 'ps3':ps3}

class Levels:

    def __init__(self, symbol, start=date(2015, 1, 1), end=date(2015, 1, 10)):
        self.symbol = symbol
        self.start_date = start
        self.end_date = end

    def get_index_price_history(self):
        start = self.start_date - timedelta(days=7)
        self.data = get_history(symbol=self.symbol, start=start, end=self.end_date, index=True)

    def averages(self, prices_list=[]):
        total = 0
        for x in prices_list:
            total += x 
        
        return round(total/len(prices_list), 2)
    
    def gann_angle(self, n1, n2):
        return round((n1*2 - n2), 2)

class Daily(Levels):

    def __init__(self, symbol, start=date(2015, 1, 1), end=date(2015, 1, 10)):
        super().__init__(symbol, start, end)

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
        levels, camrilla, pivot = {}, {}, {}
        
        for single_date in pd.bdate_range(self.start_date, self.end_date):
            levels[single_date.strftime("%Y-%m-%d")] = {}
            levels[single_date.strftime("%Y-%m-%d")]["h2"] = str(self.averages(high[j:j+2]))
            levels[single_date.strftime("%Y-%m-%d")]["h3"] = str(self.averages(high[i:i+3]))
            levels[single_date.strftime("%Y-%m-%d")]["c2"] = str(self.averages(close[j:j+2]))
            levels[single_date.strftime("%Y-%m-%d")]["c3"] = str(self.averages(close[i:i+3]))
            levels[single_date.strftime("%Y-%m-%d")]["l2"] = str(self.averages(low[j:j+2]))
            levels[single_date.strftime("%Y-%m-%d")]["l3"] = str(self.averages(low[i:i+3]))

            levels[single_date.strftime("%Y-%m-%d")]["g1"] = str(self.gann_angle(high[k], close[k]))
            levels[single_date.strftime("%Y-%m-%d")]["g2"] = str(self.gann_angle(close[k], low[k]))
            levels[single_date.strftime("%Y-%m-%d")]["g3"] = str(self.gann_angle(low[k], close[k]))
            levels[single_date.strftime("%Y-%m-%d")]["g4"] = str(self.gann_angle(close[k], high[k]))

            camrilla_levels = Camrilla(high[k], low[k], close[k])

            camrilla[single_date.strftime("%Y-%m-%d")] = {}
            camrilla[single_date.strftime("%Y-%m-%d")]["r1"] = str(camrilla_levels.r1())
            camrilla[single_date.strftime("%Y-%m-%d")]["r2"] = str(camrilla_levels.r2())
            camrilla[single_date.strftime("%Y-%m-%d")]["r3"] = str(camrilla_levels.r3())
            camrilla[single_date.strftime("%Y-%m-%d")]["r4"] = str(camrilla_levels.r4())
            camrilla[single_date.strftime("%Y-%m-%d")]["r5"] = str(camrilla_levels.r5())
            camrilla[single_date.strftime("%Y-%m-%d")]["s1"] = str(camrilla_levels.s1())
            camrilla[single_date.strftime("%Y-%m-%d")]["s2"] = str(camrilla_levels.s2())
            camrilla[single_date.strftime("%Y-%m-%d")]["s3"] = str(camrilla_levels.s3())
            camrilla[single_date.strftime("%Y-%m-%d")]["s4"] = str(camrilla_levels.s4())
            camrilla[single_date.strftime("%Y-%m-%d")]["s5"] = str(camrilla_levels.s5())

            my_pivot = Pivot(high[k], low[k], close[k])
            pivot[single_date.strftime("%Y-%m-%d")] = {}
            pivot[single_date.strftime("%Y-%m-%d")] = my_pivot.pivot_levels()

            i, j, k = i+1, j+1, k+1

        return {'levels':levels, 'camrilla': camrilla, 'pivot': pivot}

class Weekly(Levels):

    def __init__(self, symbol, start=date(2015, 1, 1), end=date(2015, 1, 10)):
        super().__init__(symbol, start, end)

    def angles(self):
        highs = self.data['High'].to_dict()
        lows = self.data['Low'].to_dict()
        closes = self.data['Close'].to_dict()

        weekly, weekly_counter = {}, 0

        for date, h in highs.items():
            if weekly_counter == 0:
                high = 0
            
            if h > high:
                high = h

            if weekly_counter == 4:
                weekly[date] = {}
                weekly[date]['High'] = high
                weekly_counter = 0
            else:
                weekly_counter += 1

        weekly_counter = 0

        for date, l in lows.items():
            if weekly_counter == 0:
                low = l
            
            if l <= low:
                low = l

            if weekly_counter == 4:
                weekly_counter = 0
                weekly[date]['Low'] = low
            else:
                weekly_counter += 1

        weekly_counter = 0
        
        for date, c in closes.items():
            if date in weekly:
                weekly[date]['Close'] = c

        

        

        