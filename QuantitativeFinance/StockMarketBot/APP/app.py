""" 
This simple bot only works with American stocks 
"""

from secret import TWILIO_ACCOUNT, TWILIO_TOKEN
from marketstack import get_stock_price

from flask import Flask
from flask import request
from twilio.rest import Client

app = Flask(__name__)

client = Client(TWILIO_ACCOUNT, TWILIO_TOKEN)
TWILIO_NUMBER = 'whatsapp: '

# This function processes the body of messages received by Whatsapp 
def send_msg(msg, recipient):
    client.messages.create (
        from_ = TWILIO_NUMBER,
        body = msg,
        to = recipient
    )

# This function interacts with WhatsApp messages and calls the get_stock_market function that queries stock prices
def process_msg(msg):
    response = ""
    if msg == "hi":
        response = "Hello, welcome to the stock market bot!"
        response += "Type sym:<stock_symbol> to know the price of the stock."
    elif 'sym' in msg:
        data = msg.split(":")
        stock_symbol = data[1]
        stock_prices = get_stock_price(stock_symbol)
        high_price = stock_prices['high_price']
        low_price = stock_prices['low_price']
        response = "The Stock price of {0} is: high price ${1} and low price ${2} in day".format(str(stock_symbol), str(high_price), str(low_price))

    else:
        response = "Please type hi to get started."
    return response

@app.route("/webhook", methods=["POST"])
def webhook():
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response, sender)
    return "OK", 200