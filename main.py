import requests
import json

metodo = str(input('https or http? ')).lower()
proxies = open("proxies.txt", "r")
linhas = proxies.readlines()

for linha in linhas:
	try:
		proxy = linha.rstrip()
		if metodo == 'https':
			r = requests.get("https://ourworldofpixels.com/api/", proxies={'https': proxy})
		elif metodo == 'http':
			r = requests.get("https://ourworldofpixels.com/api/", proxies={'http': proxy})
		else:
			print('Please select a valid method.')
		data = json.loads(r.text)
		if data["banned"] == 0:
			print(proxy)
	except:
		pass
