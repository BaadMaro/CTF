# Challenge Name: secure

![date](https://img.shields.io/badge/date-10.07.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![web category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![value](https://img.shields.io/badge/value-104-blue.svg)  


## Description

Just learned about encryption—now, my website is unhackable!

secure.mc.ax

Author : BrownieInMotion

[index.js](index.js)

## Detailed solution

Opening the challenge link https://secure.mc.ax/

![image](https://user-images.githubusercontent.com/72421091/125511905-60a687d1-610c-4c52-9014-e8ceff0a743c.png)

It's a classic login page that use POST with username and password to /login

```javascript
  <script>
    (async() => {
      await new Promise((resolve) => window.addEventListener('load', resolve));
      document.querySelector('form').addEventListener('submit', (e) => {
        e.preventDefault();
        const form = document.createElement('form');
        form.setAttribute('method', 'POST');
        form.setAttribute('action', '/login');

        const username = document.createElement('input');
        username.setAttribute('name', 'username');
        username.setAttribute('value',
          btoa(document.querySelector('#username').value)
        );

        const password = document.createElement('input');
        password.setAttribute('name', 'password');
        password.setAttribute('value',
          btoa(document.querySelector('#password').value)
        );

        form.appendChild(username);
        form.appendChild(password);

        form.setAttribute('style', 'display: none');

        document.body.appendChild(form);
        form.submit();
      });
    })();
  </script>
```
Let's check the [index.js](index.js) file. Here is the login part
  
```javascript
app.post('/login', (req, res) => {
  if (!req.body.username || !req.body.password)
    return res.redirect('/?message=Username and password required!');

  const query = `SELECT id FROM users WHERE
          username = '${req.body.username}' AND
          password = '${req.body.password}';`;
  try {
    const id = db.prepare(query).get()?.id;

    if (id) return res.redirect(`/?message=${process.env.FLAG}`);
    else throw new Error('Incorrect login');
  } catch {
    return res.redirect(
      `/?message=Incorrect username or password. Query: ${query}`
    );
  }
});
```
To be able to get the flag we need to make the query true without knowing the username and password 

Let's perform some sql injection in the password parametre. I'm gonna use burp

Capture the post request while logging in and focus the password parametre

![2021-07-13_20h26_58](https://user-images.githubusercontent.com/72421091/125513268-80d6b72e-9234-43ea-ab06-022eaa45d9e4.png)

Use some payloads from https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/Intruder/Auth_Bypass.txt

We got our flag we can url decode it from that alert parametre or check the success page

![image](https://user-images.githubusercontent.com/72421091/125513372-d2502161-83f9-40e1-bee0-cd9c66d7bc3f.png)

![image](https://user-images.githubusercontent.com/72421091/125513481-9b03d9e9-f6fe-42ef-aa9b-842e4d642724.png)


## Flag

```
flag{50m37h1n6_50m37h1n6_cl13n7_n07_600d}
```
