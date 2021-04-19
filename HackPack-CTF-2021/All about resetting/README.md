# Challenge Name: All about resetting




![date](https://img.shields.io/badge/date-17.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![misc category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![score](https://img.shields.io/badge/score-50-blue.svg)

## Description

Who can guess my password or.. http://all-about-resetting.ctf2021.hackpack.club

## Detailed solution

Start by opening challenge link http://all-about-resetting.ctf2021.hackpack.club 

It's a login page 

![image](https://user-images.githubusercontent.com/72421091/115284782-a7304400-a13c-11eb-94c1-6dfd9362beb5.png)

Let's check the page source view-source:https://all-about-resetting.ctf2021.hackpack.club/ 

```html
<!-- Maintaned by Nikos (npantel@ncsu.edu) -->
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Login V1</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">

</head>

<!-- Maintaned by Nikos (npantel@ncsu.edu) -->
<body>	
	<span class="login100-form-title">
		Member Login
	</span>

	<div>
		<input placeholder="Email">

		</input>
	</div>

	<div>
		<input placeholder="Password">

		</input>
	</div>
	
	<div class="container-login100-form-btn">
		<button class="login100-form-btn">
			Login
		</button>
	</div>
	
	<form action="/reset" method="post">
		<button type="submit" value="Send Email" >Forgot Password?</button>
	</form>
	
</body>
</html>
```

We have only the Forget passowrd? option with a POST request to /reset 

at https://all-about-resetting.ctf2021.hackpack.club/reset  we can see a POST request to /rest2 using the email from input 

![image](https://user-images.githubusercontent.com/72421091/115286194-50c40500-a13e-11eb-91b0-3ee93935fcc0.png) 

```html
				<form action = "/reset2" method = "POST">
					<p><h3>Enter user email to RESET</h3></p>
					<p><input type = 'text' name = 'email' placeholder="Email"/></p>
					<p><input type = 'submit' value = 'Login'/></p>
				</form>
```

I tried with a random email but i got nothing 

Checking the response headers i found a set-cookie header with a flask cookie

```
set-cookie: session=.eJyrVkpLzMyJT84rUbIy1AFyyvKLMktS0_PLUovyEvOSU5WslLITszOLS_KTixKTK5UQakpSE3OBsvk5lbkFmYnJ-cVKtQBcuByb.YH3Pcg.XajTlQMYBDBUBL5sG7nPoo1o908; HttpOnly; Path=/
```

Let's use flask-unsign to decod the cookie https://pypi.org/project/flask-unsign/  

```
flask-unsign --decode --cookie .eJyrVkpLzMyJT84rUbIy1AFyyvKLMktS0_PLUovyEvOSU5WslLITszOLS_KTixKTK5UQakpSE3OBsvk5lbkFmYnJ-cVKtQBcuByb.YH3Pcg.XajTlQMYBDBUBL5sG7nPoo1o908
{'fail_cnt': 1, 'favoritegovernance': 'kakistocracy', 'favoriteteam': 'olympiacos'}
```  

We have two values :
- favoritegovernance : kakistocracy
- favoriteteam : olympiacos

Back to our home page we found a coomen tag with an email 

```html
<!-- Maintaned by Nikos (npantel@ncsu.edu) -->
```

I used the email npantel@ncsu.edu with the reset feature 

![image](https://user-images.githubusercontent.com/72421091/115287964-64706b00-a140-11eb-88e0-711ea769f888.png)

![image](https://user-images.githubusercontent.com/72421091/115287994-6f2b0000-a140-11eb-9e91-aa9dcf908498.png) 

The answer is **kakistocracy** we go it from decoding the flask cookie  

![image](https://user-images.githubusercontent.com/72421091/115288093-91bd1900-a140-11eb-8a65-cb7292c89cfd.png) 

We got our flag 



## Flag

```
flag = flag{Wh4t_1s_th1s_gov3rn4nc3_!!!}
```





