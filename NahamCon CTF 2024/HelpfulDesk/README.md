
# Challenge Name: HelpfulDesk


![date](https://img.shields.io/badge/date-23.05.2024-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  

## Description

Author: @HuskyHacks  
  
HelpfulDesk is the go-to solution for small and medium businesses who need remote monitoring and management. Last night, HelpfulDesk released a security bulletin urging everyone to patch to the latest patch level. They were scarce on the details, but I bet that can't be good...  
  
**Press the `Start` button on the top-right to begin this challenge.**

## Detailed solution

Start by checking the challenge URL http://challenge.nahamcon.com:31593/

![Pasted image 20240525183913](https://github.com/BaadMaro/CTF/assets/72421091/c57a7d60-bbbe-4a27-b2db-fc75dc97cbca)

We can see a section for a security update and also version 1.1 mentioned

http://challenge.nahamcon.com:31593/Security/Bulletin

![Pasted image 20240525184028](https://github.com/BaadMaro/CTF/assets/72421091/9bab6048-cd6e-471f-842b-b1aadafb1c8d)

There is a new version 1.2 that fixed a critical security vulnerability so which mean that our version 1.1 is vulnerable

The page has the source code linked http://challenge.nahamcon.com:31593/api/v1/downloads/helpfuldesk-1.1.zip

We have the main app in DLL file. We can use `dotpeek` to extract files

![Pasted image 20240525220552](https://github.com/BaadMaro/CTF/assets/72421091/f8ecbcb1-3467-4ed8-8074-dc0b575d2146)

I start by doing static analysis using `snyk` to check for vulnerabilities

```
snyk code test
```

```
 ✗ [High] Path Traversal 
   Path: HelpfulDesk/Controllers/DashboardController.cs, line 99 
   Info: Unsanitized input from an HTTP parameter flows into global::System.IO.File.Exists, where it is used as a path. This may result in a Path Traversal vulnerability and allow an attacker to obtain information about arbitrary files.

 ✗ [High] Path Traversal 
   Path: HelpfulDesk/Controllers/DownloadsController.cs, line 26 
   Info: Unsanitized input from an HTTP parameter flows into global::System.IO.File.Exists, where it is used as a path. This may result in a Path Traversal vulnerability and allow an attacker to obtain information about arbitrary files.
```

We have two path traversal vulnerabilities. I tried first with the `Download` one but i was not able to make it work. 

The second vulnerability is in the dashboard which require login to access the dashboard

During the beginning of CTF, the used credentials were `admin:admin` and made the challenge simple which is not intended 

In `HelpfulDesk\HelpfulDesk\Controllers\SetupController.cs` we have a setup wizard to create an account and check if the setup already done with the file `credentials.json` to block access to it with 403. We can bypass that using `/` at the end of path

```
if (File.Exists(this._credsFilePath))

      {

        PathString path = ((ControllerBase) this).HttpContext.Request.Path;

        if (((PathString) ref path).Value.Equals("/Setup/SetupWizard", StringComparison.OrdinalIgnoreCase))

          return (IActionResult) this.View("Error", (object) new ErrorViewModel()

          {

            RequestId = "Server already set up.",

            ExceptionMessage = "Server already set up.",

            StatusCode = 403

          });

      }
```

![Pasted image 20240525222330](https://github.com/BaadMaro/CTF/assets/72421091/f0709f48-b517-466d-a836-237d5644385c)

Let's create an account and use it for login

![Pasted image 20240525222444](https://github.com/BaadMaro/CTF/assets/72421091/50d09f16-af65-463f-bdf1-abfb2c9d8737)

![Pasted image 20240525222510](https://github.com/BaadMaro/CTF/assets/72421091/46ed6431-05e2-489f-86bb-3b1aee4e237f)

We have the flag with `HOST-WIN-DX130S2`

http://challenge.nahamcon.com:30785/Dashboard/DownloadFile?fileName=flag.txt

## Flag

```
flag{2fd5d91a4504ecf32a1b701a4b7122db}
```

