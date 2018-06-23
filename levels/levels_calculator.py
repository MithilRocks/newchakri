from datetime import date 
import levels
import json

n = levels.Levels("NIFTY 50", date(2018, 5, 10), date(2018, 5, 17))
n.get_index_price_history()
print(n.angles())
