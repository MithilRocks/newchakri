from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    data = {}
    data['css'] = url_for('static', filename='css/bootstrap.min.css')
    return render_template('home.html', data = data)

if __name__ == "__main__":
    app.run(debug=True)