from flask import Flask, render_template, request, Response
import requests
import json
import os


app = Flask(__name__)
mode = os.environ.get('app_mode')
if mode == "test":
    base_url = "http://127.0.0.1:5000/mock/"
else:
    base_url = "https://api.coinbase.com/v2/prices/spot?currency="


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/shortenurl', methods=['GET', 'POST'])
def shortenurl():
    url = ''.join([base_url, request.form['shortcode']])
    response = requests.get(url)
    data = response.json()
    currency = data["data"]["currency"]
    price = data["data"]["amount"]
    return render_template('shortenurl.html', shortcode=f"The BTC price in {currency} is {price}")


@app.route('/EUR')
def EUR():
    url = ''.join([base_url, "EUR"])
    response = requests.get(url)
    data = response.json()
    return data


@app.route('/GBP')
def GBP():
    url = ''.join([base_url, "GBP"])
    response = requests.get(url)
    data = response.json()
    return data


@app.route('/USD')
def USD():
    url = ''.join([base_url, "USD"])
    response = requests.get(url)
    data = response.json()
    return data


@app.route('/JPY')
def JPY():
    url = ''.join([base_url, "JPY"])
    response = requests.get(url)
    data = response.json()
    return data


@app.route('/health')
def health():
    status_code = Response(status=200)
    return status_code

# Mock legit response


@app.route('/mock/EUR')
def mock_EUR():
    response = '{"data":{"base":"BTC","currency":"EUR","amount":"37735.92"}}'
    print(response)
    return response

# Mock Wrong Json


@app.route('/mock/GBP')
def mock_GBP():
    response = 'wrong json object'
    print(response)
    return response

# Mock Invalid Currency


@app.route('/mock/ZZZ')
def mock_ZZZ():
    response = '{"errors":[{"id":"invalid_request","message":"Currency is invalid"}]}'
    print(response)
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
