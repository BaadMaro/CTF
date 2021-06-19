# Challenge Name: message-board

![date](https://img.shields.io/badge/date-15.06.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![web category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![value](https://img.shields.io/badge/value-305-blue.svg)  


## Description

Your employer, LameCompany, has lots of gossip on its company message board: message-board.hsc.tf. You, Kupatergent, are able to access some of the tea, but not all of it! Unsatisfied, you figure that the admin user must have access to ALL of the tea. Your goal is to find the tea you've been missing out on.

Your login credentials: username: kupatergent password: gandal

Server code is attached (slightly modified).

[message-board-master.zip](message-board-master.zip)

## Detailed solution

Start by opening the challenge link https://message-board.hsc.tf/  

![image](https://user-images.githubusercontent.com/72421091/122657103-4cc15d00-d158-11eb-91f5-efc9767c5bf3.png)

We have a login page https://message-board.hsc.tf/login  

![image](https://user-images.githubusercontent.com/72421091/122657152-c8230e80-d158-11eb-9df6-182658900f84.png)

It's a normal login form that use POST request  

```html
    <form action="/login" method="POST">
        <div class="mb-3">
            <label class="form-label" for="username">Username</label>
            <input class="form-control" type="text" name="username" id="">
        </div>
        <div class="mb-3">
            <label class="form-label" for="password">Password</label>
            <input class="form-control" type="password" name="password" id="">
        </div>
        <button class="btn btn-primary" type="submit">Login</button>
        <p class="form-text">Gossip abounds</p>
    </form>
```

Now let's check the source code [message-board-master.zip](message-board-master.zip) 

It's a Express-NodeJS web application let's see the app.js 

```js
const express = require("express")
const cookieParser = require("cookie-parser")
const ejs = require("ejs")
require("dotenv").config()

const app = express()
app.use(express.urlencoded({ extended: true }))
app.use(cookieParser())
app.set("view engine", "ejs")
app.use(express.static("public"))

const users = [
    {
        userID: "972",
        username: "kupatergent",
        password: "gandal"
    },
    {
        userID: "***",
        username: "admin"
    }
]

app.get("/", (req, res) => {
    const admin = users.find(u => u.username === "admin")
    if(req.cookies && req.cookies.userData && req.cookies.userData.userID) {
        const {userID, username} = req.cookies.userData
        if(req.cookies.userData.userID === admin.userID) res.render("home.ejs", {username: username, flag: process.env.FLAG})
        else res.render("home.ejs", {username: username, flag: "no flag for you"})
    } else {
        res.render("unauth.ejs")
    }
})

app.route("/login")
.get((req, res) => {
    if(req.cookies.userData && req.cookies.userData.userID) {
        res.redirect("/")
    } else {
        res.render("login.ejs", {err: false})
    }
})
.post((req, res)=> {
    const request = {
        username: req.body.username,
        password: req.body.password
    }
    const user = users.find(u => (u.username === request.username && u.password === request.password))
    if(user) {
        res.cookie("userData", {userID: user.userID, username: user.username})
        res.redirect("/")
    } else {
        res.render("login", {err: true}) // didn't work!
    }
})

app.get("/logout", (req, res) => {
    res.clearCookie("userData")
    res.redirect("/login")
}) 

app.listen(3000, (err) => {
    if (err) console.log(err);
    else console.log("connected at 3000 :)");
})
```  

The login POST request test if the usersname and password exist in the ``` const users ``` 

As we can users has **kupatergent** and admin, the password and userID for the admin has been edited for the challenge  

So we can only login as ```kupatergent:gandal``` 

![image](https://user-images.githubusercontent.com/72421091/122657442-7c259900-d15b-11eb-802a-4342bb8975ef.png)

After login in using ```kupatergent:gandal``` we can the message no flag for you 

```js
app.get("/", (req, res) => {
    const admin = users.find(u => u.username === "admin")
    if(req.cookies && req.cookies.userData && req.cookies.userData.userID) {
        const {userID, username} = req.cookies.userData
        if(req.cookies.userData.userID === admin.userID) res.render("home.ejs", {username: username, flag: process.env.FLAG})
        else res.render("home.ejs", {username: username, flag: "no flag for you"})
    } else {
        res.render("unauth.ejs")
    }
})
``` 
As we can see if we acces the home page a test check our cookie and extract the userID and username and compare them to username and userID of the admin 

If our cookie has the admin username and userID we gonna see the flag 

A cookie has been generated after login in ```kupatergent:gandal``` we can see it in dev tools 

```
userData=j%3A%7B%22userID%22%3A%22972%22%2C%22username%22%3A%22kupatergent%22%7D
``` 

It's url encoded let's decode it 
  
```
j:{"userID":"972","username":"kupatergent"}
```  

As we can the cookie has the userID and the username. So to be able to get the flag we need to craft a cookie with 

j:{"userID":"X","username":"admin"} as X is admin userID 

So we need to brutforce the userID until we got a page with flag 


## Flag

```

```
