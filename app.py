from flask import Flask, request, jsonify
import json
import kitesettings
from kiteconnect import KiteConnect
import os
app = Flask(__name__)

kite = KiteConnect(kitesettings.API_KEY)

def order_place(order_id, symbol, exchange, transaction, quantity, price):
    kite.set_access_token(kitesettings.access_token)

    try:
        order_id = kite.place_order(tradingsymbol=symbol,
                                    exchange=exchange,
                                    transaction_type=transaction,
                                    quantity=quantity,
                                    price=price,
                                    variety=kite.VARIETY_REGULAR,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product=kite.PRODUCT_NRML)
        print("Order placed. ID is: {}".format(order_id))
    except Exception as e:
        print("Order placement failed: {}".format(e))

    return order_id

@app.route("/welcome")
def welcome():
    print("WELCOME")
    return "<p>welcome</p>"

@app.route('/log', methods=['POST'])
def log():
    print(request.data)
    return "<p>log</p>"
	
@app.route('/btc', methods=['POST'])
def btc():
    print(request.data)
    return "<p>log</p>"

@app.route('/zerodhahook', methods=['POST'])
def webhook():
    print(request.data)
    data = json.loads(request.data)
    result = order_place('',data['tradingsymbol'], data['exchange'], data["transaction_type"].upper(), data['quantity'], data['price'])
    print(result)
    return{
        "code": "error",
        "message": "order"
    }
@app.route('/options', methods=['POST'])
def webhook1():
    print(request.data)
    data = json.loads(request.data)
    kite.set_access_token(kitesettings.access_token)

    try:
        order_id = kite.place_order(tradingsymbol="NIFTY21NOV18200CE",
                                    exchange="NFO",
                                    transaction_type="BUY",
                                    quantity="50",
                                    price="0.0",
                                    variety=kite.VARIETY_REGULAR,
                                    order_type="SL-M",
                                    product=kite.PRODUCT_NRML,
				    trigger_price=7)
        print("Order placed. ID is: {}".format(order_id))
    except Exception as e:
        print("Order placement failed: {}".format(e))

    return order_id
    return{
        "code": "error",
        "message": "order"
    }
