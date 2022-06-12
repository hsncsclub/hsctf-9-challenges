import requests
#URL = "http://localhost:8005"
URL = "http://web1.hsctf.com:8005"
resp = requests.post(URL, files={"file": ("solve.png", open("solve.png"))})
with open("out.png", "wb") as f:
	f.write(resp.content)
