const sleep = (time) => new Promise((resolve) => setTimeout(resolve, time));

const challenges = new Map([
	[
		"markdown-plus-plus",
		{
			title: "Submit Page",
			header: "Show us what you've created!",
			timeout: 10 * 1000,
			urlRegex: /^http:\/\/web1\.hsctf\.com:8002\/display/,
			handler: async function (url, ctx) {
				const URL = "http://web1.hsctf.com:8002/";
				const FLAG = "flag{waterfall_bfutsftfejpk}";

				let page = await ctx.newPage();
				await page.goto(`${URL}/create`);
				await page.type("#login-form > [name=username]", FLAG);
				await page.click("#login-form > [type=submit]");
				await page.waitForNavigation();
				await page.close();
				page = await ctx.newPage();
				await page.goto(url, { timeout: 3000, waitUntil: "domcontentloaded" });
				await sleep(3000);
				await page.close();
			},
		},
	],
	[
		"hsgtf",
		{
			title: "Report",
			header: "Report Error to Admin",
			timeout: 50 * 1000,
			handler: async function (url, ctx) {
				const URL = "http://web1.hsctf.com:8001";
				const ADMIN_SECRET =
					"003db352756e870182e7360ed9d1bb3df2add8989374927a42ef39688c89304d";
				let page = await ctx.newPage();
				await page.setCookie({
					name: "secret",
					value: ADMIN_SECRET,
					url: URL,
					httpOnly: true,
					sameSite: "None",
				});
				await page.goto(url, { timeout: 3000, waitUntil: "domcontentloaded" });
				await sleep(40 * 1000);
				await page.close();
			},
		},
	],
]);
module.exports = {
	challenges,
};
