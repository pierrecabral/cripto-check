from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/shortenurl', methods=['GET', 'POST'])
def shortenurl():
    base_url = "https://api.coinbase.com/v2/prices/spot?currency="
    url = ''.join([base_url, request.form['shortcode']])
    response = requests.get(url)
    data = response.json()
    currency = data["data"]["currency"]
    price = data["data"]["amount"]
    return render_template('shortenurl.html', shortcode=f"The BTC price in {currency} is {price}")


@app.route('/health')
def health():
    return "200"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
