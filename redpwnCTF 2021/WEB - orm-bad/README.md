# Challenge Name: orm-bad

![date](https://img.shields.io/badge/date-09.07.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![web category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![value](https://img.shields.io/badge/value-102-blue.svg)  


## Description

I just learned about orms today! They seem kinda difficult to implement though... Guess I'll stick to good old raw sql statements!

orm-bad.mc.ax

Author : ra

[app.js](app.js)


## Detailed solution

Start by oppening the challenge link https://orm-bad.mc.ax/

![2021-07-13_15h54_41](https://user-images.githubusercontent.com/72421091/125474442-711fe1bc-8716-4d01-a6ec-18f004df249d.png)


Checking the page source  view-source:https://orm-bad.mc.ax/
  
```html
<!DOCTYPE html>
<html lang="en">

<body>
    <div style="text-align:center">
        
        <h1>Sign in:</h1>
        <form id="login_form" action="/flag" method="POST">
            <label for="username">Username: </label><input type="text" name="username" id="username"><br>
            <label for="password">Password: </label><input type="password" name="password" id="username"><br>
            <input type="submit" name="submit" id="submit" value="Login">
        </form>
    </div>
</body>
```
Just a simple login form that POST username and password to /flag

Now let's check the [app.js](app.js) file

We cann se that our app is a NodeJS/Express web app that use sqlite3 as database

Let's check the POST request to /flag

```javascript
app.post('/flag', (req, res) => {
    db.all("SELECT * FROM users WHERE username='" + req.body.username + "' AND password='" + req.body.password + "'", (err, rows) => {
        try {
            if (rows.length == 0) {
                res.redirect("/?alert=" + encodeURIComponent("you are not admin :("));
            } else if(rows[0].username === "admin") {
                res.redirect("/?alert=" + encodeURIComponent(flag));
            } else {
                res.redirect("/?alert=" + encodeURIComponent("you are not admin :("));
            }
        } catch (e) {
            res.status(500).end();
        }
    })
})
```
We can see the sql query used to login ```"SELECT * FROM users WHERE username='" + req.body.username + "' AND password='" + req.body.password + "'"``` 

To bypass login and get the flag we need to use the username admin (rows[0].username === "admin") and make the query true without knowing the password

Let's perform some sql injection in the password parametre. I'm gonna use burp

Capture the post request while logging in and focus the password parametre

![image](https://user-images.githubusercontent.com/72421091/125477742-db725124-2196-41fa-8b6a-af91c0d32f4d.png)

Use some payloads from https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/Intruder/Auth_Bypass.txt 

We got our flag we can url decode it from that alert parametre or check the success page

![image](https://user-images.githubusercontent.com/72421091/125478434-6a439727-3ae1-4423-b33b-b8c1e7603f36.png)

![image](https://user-images.githubusercontent.com/72421091/125478760-132fba72-6105-4afd-a06d-6a87d883c6c3.png)



## Flag

```
flag{sqli_overused_again_0b4f6}
```
