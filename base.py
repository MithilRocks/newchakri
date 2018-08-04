from flask import Flask, render_template, url_for
from levels import levels
from datetime import date, timedelta
import datetime
import json
from dateutil.relativedelta import relativedelta, MO, FR

app = Flask(__name__)

@app.route('/nifty/daily')
def nifty_daily():
    data = daily("NIFTY 50")
    return render_template('daily.html', data = data)

@app.route('/bank-nifty/daily')
def bnf_daily():
    data = daily("BANKNIFTY")
    return render_template('daily.html', data = data)

@app.route('/nifty/weekly')
def nifty_weekly():
    data = weekly("NIFTY 50")
    return render_template('daily.html', data = data)

@app.route('/bank-nifty/weekly')
def bnf_weekly():
    data = weekly("BANKNIFTY")
    return render_template('daily.html', data = data)

def daily(symbol):
    end_date = datetime.date.today()
    start_date = end_date - timedelta(days=10)

    daily_details = levels.Daily(symbol, start_date, end_date)
    daily_details.get_index_history() 

    data = {}
    data['css'] = url_for('static', filename='css/bootstrap.min.css')
    data['js'] = url_for('static', filename='js/bootstrap.min.js')
    data['symbol'] = symbol
    data['daily'] = daily_details.main()
    
    return data

def weekly(symbol):
    end_date = datetime.date.today() + relativedelta(weekday=FR(-1))
    start_date = datetime.date.today() + relativedelta(weekday = MO(-7))

    weekly_details = levels.Weekly(symbol, start_date, end_date)
    weekly_details.get_index_history()

    data = {}
    data['css'] = url_for('static', filename='css/bootstrap.min.css')
    data['js'] = url_for('static', filename='js/bootstrap.min.js')
    data['symbol'] = symbol
    data['daily'] = weekly_details.main()

    return data

if __name__ == "__main__":
    app.run()