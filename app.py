from flask import Flask, request, jsonify
import json
import kitesettings
from kiteconnect import KiteConnect
import os
app = Flask(__name__)

kite = KiteConnect(kitesettings.API_KEY)

def order_place(order_id, symbol, transaction, quantity):
    kite.set_access_token(kitesettings.access_token)

    try:
        order_id = kite.place_order(tradingsymbol=symbol,
                                    exchange="NFO",
                                    transaction_type=transaction,
                                    quantity=quantity,price=0.0,
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
    data = data = json.loads(request.data)
    if data["transaction_type"] == "buy":
        rounded = (round(round(float(data['price']))/100)*100) - 200
        Symbol= "NIFTY"+data["YrMnDt"]+str(rounded)+"CE"
        f = open("CE.txt", "w")
        f.write(Symbol)
        f.close()
    f = open("CE.txt", "r")
    Symbol = f.read()
    print(Symbol)
    qnt = int(data['quantity'])*50
    print(qnt)
    return "<p>log</p>"
	
@app.route('/optionsCE', methods=['POST'])
def webhook2():
    print(request.data)
    data = json.loads(request.data)
    if data["transaction_type"] == "buy":
        rounded = (round(round(float(data['price']))/100)*100) - 200
        SymbolCE= "NIFTY"+data["YrMnDt"]+str(rounded)+"CE"
        f = open("CE.txt", "w")
        f.write(SymbolCE)
        f.close()
    print(SymbolCE)
    f = open("CE.txt","r")
    Symbol = f.read()
    f.close()
    result = order_place('',Symbol, data["transaction_type"].upper(), int(data['quantity'])*50)
    print(result)
    return{
        "code": "error",
        "message": "order"
    }

@app.route('/optionsPE', methods=['POST'])
def webhook():
    print(request.data)
    data = json.loads(request.data)
    if data["transaction_type"] == "buy":
        TT = "SELL"
        rounded = (round(round(float(data['price']))/100)*100) + 200
        SymbolPE= "NIFTY"+data["YrMnDt"]+str(rounded)+"PE"
        f = open("PE.txt", "w")
        f.write(SymbolPE)
        f.close()
    if data["transaction_type"] == "sell":
        TT = "BUY"
    print(SymbolPE)
    f = open("PE.txt","r")
    Symbol = f.read()
    f.close()
    result = order_place('',Symbol, TT, int(data['quantity'])*50)
    print(result)
    return{
        "code": "error",
        "message": "order"
    }
