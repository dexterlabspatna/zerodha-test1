from flask import Flask, request, jsonify
import json
import kitesettings
from kiteconnect import KiteConnect
import os
app = Flask(__name__)

kite = KiteConnect(kitesettings.API_KEY)

#TO-DO Local
#print(kite.login_url())
#reqt_token = input("token:")
#gen_ssn = kite.generate_session(
#request_token=reqt_token, api_secret=kitesettings.api_secret)
#acc_tok = gen_ssn['access_token']
#print(acc_tok)
#kite.set_access_token(acc_tok)
#order_id = ''

def order_place(symbol, exchange, transaction, quantity, price):
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
        print("Order Placed")
    except Exception as e:
        print("Order Failed")

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
    result = order_place(data['tradingsymbol'], data['exchange'], data["transaction_type"].upper(), data['quantity'], data['price'])
    print(result)
    return{
        "code": "error",
        "message": "order"
    }
