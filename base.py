from flask import Flask, render_template, url_for
from levels import levels
from datetime import date, timedelta
import datetime
import json

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    end_date = datetime.date.today()
    start_date = end_date - timedelta(days=7)

    nifty_50_daily = levels.Levels("NIFTY 50", start_date, end_date)
    nifty_50_daily.get_index_price_history()

    bank_nifty_daily = levels.Levels("BANKNIFTY", start_date, end_date)
    bank_nifty_daily.get_index_price_history()

    data = {}
    data['css'] = url_for('static', filename='css/bootstrap.min.css')
    data['js'] = url_for('static', filename='js/bootstrap.min.js')
    
    data['bank_nifty_daily'] = bank_nifty_daily.angles()
    data['nifty_50_daily'] = nifty_50_daily.angles()
    
    return render_template('home.html', data = data)

if __name__ == "__main__":
    app.run(debug=True)