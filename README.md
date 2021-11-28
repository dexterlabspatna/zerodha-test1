# zerodha-trial
download code
https://github.com/dexterlabspatna/zerodha-test1.git

Linux/AWS
Open inbound for port 443
sudo su
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 443
#windows/heruko
To Run in local
	set FLASK_APP = app.py
	python -m flask run

Login in Zerodha
1.open terminal
	python kiteGetAccessToken.py

2. Enter Cred
	ID
	PWD
	OTP

5. Request Token
	Get Token from url
	
6. Access Token
	Enter Request Token in command prompt
	Access Token is printed on prompt
	
7. Change in Git
	Copy the Access Token
	Paste in git/kitesettings.py

To view logs type in powershell
cd Desktop
heroku logs -a nifty-test --tail 2>&1 | tee HEROKU.log

APIs
https://zerodha-test1.herokuapp.com/zerodhahook
https://zerodha-test1.herokuapp.com/btc
https://zerodha-test1.herokuapp.com/log
https://zerodha-test1.herokuapp.com/welcome

Alarm json

{
"transaction_type": "{{strategy.order.action}}",
"tradingsymbol":"NIFTY21OCTFUT",
"exchange": "NFO",
"quantity": "50",
"price": {{close}}
}
