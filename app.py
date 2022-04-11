from flask import Flask, render_template, request, Response
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


@app.route('/EUR')
def EUR():
    response = requests.get(
        'https://api.coinbase.com/v2/prices/spot?currency=EUR')
    data = response.json()
    # print(data)
    return data


@app.route('/GBP')
def GBP():
    response = requests.get(
        'https://api.coinbase.com/v2/prices/spot?currency=GBP')
    data = response.json()
    # print(data)
    return data


@app.route('/USD')
def USD():
    response = requests.get(
        'https://api.coinbase.com/v2/prices/spot?currency=USD')
    data = response.json()
    # print(data)
    return data


@app.route('/JPY')
def JPY():
    response = requests.get(
        'https://api.coinbase.com/v2/prices/spot?currency=JPY')
    data = response.json()
    # print(data)
    return data


@app.route('/health')
def health():
    status_code = Response(status=200)
    return status_code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
