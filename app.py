from flask import Flask, request, jsonify
import json
import logging
import kitesettings
from kiteconnect import KiteConnect
import os
import webbrowser
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)


kite = KiteConnect(kitesettings.API_KEY)
# print(kite.login_url())
# reqt_token = input("token:")
# gen_ssn = kite.generate_session(
#     request_token=reqt_token, api_secret=kitesettings.api_secret)
# acc_tok = gen_ssn['access_token']
# print(acc_tok)
# kite.set_access_token(acc_tok)
# order_id = ''


def order_place(symbol, exchange, transaction, quantity, price):
    # kite = KiteConnect(kitesettings.API_KEY)
    kite.set_access_token(kitesettings.access_token)

    # order_id = kite.place_order(tradingsymbol="INFY",
    #                                 exchange=kite.EXCHANGE_NSE,
    #                                 transaction_type=kite.TRANSACTION_TYPE_BUY,
    #                                 quantity=1,
    #                                 price=1300.0,
    #                                 variety=kite.VARIETY_REGULAR,
    #                                 order_type=kite.ORDER_TYPE_MARKET,
    #                                 product=kite.PRODUCT_CNC)
    try:
        order_id = kite.place_order(tradingsymbol=symbol,
                                    exchange=exchange,
                                    transaction_type=transaction,
                                    quantity=quantity,
                                    price=price,
                                    variety=kite.VARIETY_REGULAR,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product=kite.PRODUCT_NRML)
        logging.info("Order placed. ID is: {}".format(order_id))
    except Exception as e:
        logging.info("Order placement failed: {}".format(e))

    return order_id


@app.route("/login")
def hello_world():
    key = kitesettings.API_KEY
    # url = "https://kite.zerodha.com/connect/login?v=4&api_key="+key
    # print(url)
    # os.system('start chrome ' + url)

    # webbrowser.open(url)
    return "<p>Hello, World!</p>"


@app.route("/welcome")
def welcome():
    print("WELCOME")
    return "<p>welcome</p>"

@app.route('/log', methods=['POST'])
def log():
    print(request.data)
    return "<p>log</p>"


@app.route('/zerodhahook', methods=['POST'])
def webhook():
    print(request.data)
    data = json.loads(request.data)

    # ---testing--------------------
    transaction = data["transaction_type"].upper()
    #symbol = data['tradingsymbol']
    #exchange = data['exchange']
    #quantity = data['quantity']
    #price = data['price']
    
    #uncomment
    #result = order_place(data['tradingsymbol'], data['exchange'], data["transaction_type"].upper(), data['quantity'], data['price'])
    
    print(result)

    return{
        "code": "error",
        "message": "order"
    }
