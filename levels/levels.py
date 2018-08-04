from nsepy import get_history
from datetime import date, datetime, timedelta
import pandas as pd
from collections import deque

class Levels:

    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date

    def get_index_history(self):
        self.data = get_history(symbol=self.symbol, start=self.start_date, end=self.end_date, index=True)

    def get_future_history(self):
        pass

    def averages(self, prices):
        return round(sum(prices)/len(prices), 2)

    def gann_angle(self, n1, n2):
        return round((n1*2 - n2), 2)

class Daily(Levels):
    """
    This function calculates the daily levels for specified symbols 
    """
    def __init__(self, symbol, start_date, end_date):
        super().__init__(symbol, start_date, end_date)

    def main(self):
        """
        The main function where the magic happens  
        """
        highs = self.data['High'].to_dict()
        lows = self.data['Low'].to_dict()
        closes = self.data['Close'].to_dict()

        average_highs = deque()
        average_lows = deque()
        average_closes = deque()

        counter, daily = 0, {}
        daily['levels'] = {}
        daily['camrilla'] = {}
        daily['pivot'] = {}
        
        for date in highs:
            average_highs.extend([highs[date]])
            average_lows.extend([lows[date]])
            average_closes.extend([closes[date]])

            if counter >= 3:
                average_highs.popleft()
                average_lows.popleft()
                average_closes.popleft()
            
            if len(average_highs) == 3:
                daily['levels'][date] = {}

                daily['levels'][date]['high'] = highs[date]
                daily['levels'][date]['low'] = lows[date]
                daily['levels'][date]['close'] = closes[date]

                daily['levels'][date]['h2'] = self.averages(list(average_highs)[1:])
                daily['levels'][date]['h3'] = self.averages(average_highs)

                daily['levels'][date]['c2'] = self.averages(list(average_closes)[1:])
                daily['levels'][date]['c3'] = self.averages(average_closes)

                daily['levels'][date]['l2'] = self.averages(list(average_lows)[1:])
                daily['levels'][date]['l3'] = self.averages(average_lows)

                daily['levels'][date]['g1'] = self.gann_angle(daily['levels'][date]['high'], daily['levels'][date]['close'])
                daily['levels'][date]['g2'] = self.gann_angle(daily['levels'][date]['close'], daily['levels'][date]['low'])
                daily['levels'][date]['g3'] = self.gann_angle(daily['levels'][date]['low'], daily['levels'][date]['close'])
                daily['levels'][date]['g4'] = self.gann_angle(daily['levels'][date]['close'], daily['levels'][date]['high'])

                daily['camrilla'][date] = {}

                cam = Camrilla(highs[date], lows[date], closes[date])
                pi = Pivot(highs[date], lows[date], closes[date])

                daily['camrilla'][date]['r1'] = cam.r1()
                daily['camrilla'][date]['r2'] = cam.r2()
                daily['camrilla'][date]['r3'] = cam.r3()
                daily['camrilla'][date]['r4'] = cam.r4()
                daily['camrilla'][date]['r5'] = cam.r5()
                daily['camrilla'][date]['s1'] = cam.s1()
                daily['camrilla'][date]['s2'] = cam.s2()
                daily['camrilla'][date]['s3'] = cam.s3()
                daily['camrilla'][date]['s4'] = cam.s4()
                daily['camrilla'][date]['s5'] = cam.s5()

                daily['pivot'][date] = pi.pivot_levels()

            counter += 1

        return daily

class Weekly(Levels):

    def __init__(self, symbol, start_date, end_date):
        super().__init__(symbol, start_date, end_date)

    def main(self):
        highs = self.data['High'].to_dict()
        lows = self.data['Low'].to_dict()
        closes = self.data['Close'].to_dict()
        dates = list(highs)

        counter, highest_high, lowest_low = 0, 0, 0
        data = {}

        for date in dates:

            if counter == 0:
                highest_high = highs[date]
                lowest_low = lows[date]

            if highs[date] > highest_high:
                highest_high = highs[date]

            if lowest_low > lows[date]:
                lowest_low = lows[date]

            counter += 1

            if counter == 5:
                data[date] = {}
                data[date]['High'] = highest_high
                data[date]['Low'] = lowest_low
                data[date]['Close'] = closes[date]
                counter = 0

        average_highs = deque()
        average_lows = deque()
        average_closes = deque()

        counter, weekly = 0, {}
        weekly['levels'] = {}
        weekly['camrilla'] = {}
        weekly['pivot'] = {}

        for date, levels in data.items():
            average_highs.extend([levels['High']])
            average_lows.extend([levels['Low']])
            average_closes.extend([levels['Close']])

            if counter >= 3:
                average_highs.popleft()
                average_lows.popleft()
                average_closes.popleft()
            
            if len(average_highs) == 3:
                weekly['levels'][date] = {}

                weekly['levels'][date]['high'] = levels['High']
                weekly['levels'][date]['low'] = levels['Low']
                weekly['levels'][date]['close'] = levels['Close']

                weekly['levels'][date]['h2'] = self.averages(list(average_highs)[1:])
                weekly['levels'][date]['h3'] = self.averages(average_highs)

                weekly['levels'][date]['c2'] = self.averages(list(average_closes)[1:])
                weekly['levels'][date]['c3'] = self.averages(average_closes)

                weekly['levels'][date]['l2'] = self.averages(list(average_lows)[1:])
                weekly['levels'][date]['l3'] = self.averages(average_lows)

                weekly['levels'][date]['g1'] = self.gann_angle(weekly['levels'][date]['high'], weekly['levels'][date]['close'])
                weekly['levels'][date]['g2'] = self.gann_angle(weekly['levels'][date]['close'], weekly['levels'][date]['low'])
                weekly['levels'][date]['g3'] = self.gann_angle(weekly['levels'][date]['low'], weekly['levels'][date]['close'])
                weekly['levels'][date]['g4'] = self.gann_angle(weekly['levels'][date]['close'], weekly['levels'][date]['high'])

                weekly['camrilla'][date] = {}

                cam = Camrilla(levels['High'], levels['Low'], levels['Close'])
                pi = Pivot(levels['High'], levels['Low'], levels['Close'])

                weekly['camrilla'][date]['r1'] = cam.r1()
                weekly['camrilla'][date]['r2'] = cam.r2()
                weekly['camrilla'][date]['r3'] = cam.r3()
                weekly['camrilla'][date]['r4'] = cam.r4()
                weekly['camrilla'][date]['r5'] = cam.r5()
                weekly['camrilla'][date]['s1'] = cam.s1()
                weekly['camrilla'][date]['s2'] = cam.s2()
                weekly['camrilla'][date]['s3'] = cam.s3()
                weekly['camrilla'][date]['s4'] = cam.s4()
                weekly['camrilla'][date]['s5'] = cam.s5()

                weekly['pivot'][date] = pi.pivot_levels()

            counter += 1

        return weekly

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