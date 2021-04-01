
# Challenge Name: password hint


![date](https://img.shields.io/badge/date-08.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)




## Detailed solution

Starting by opening challenge link http://ec2-18-196-160-18.eu-central-1.compute.amazonaws.com/ 

It's a login page 

![image](https://user-images.githubusercontent.com/72421091/113343422-b6835500-9327-11eb-90bb-15bdce7e106e.png)

Checking the page source view-source:http://ec2-18-196-160-18.eu-central-1.compute.amazonaws.com/ at Forget password we found a domain 

```html
<div class="col">
   <p class="help-text text-end"><a href="http://ct.ctfeasy.unaux.com/">Forgot password?</a></p>
</div>
``` 
Opening http://ct.ctfeasy.unaux.com/ we can a text **have you ever recon before** ( when i solved the challenge this website was not working)

It's a hint to do reconnaissance. The challenge name also has the same hint. 

I used nslookup to see the dns records https://www.nslookup.io/dns-records/ctctf.easy.unaux.com  
  
```
TXT records : "v=spf1 include:flag_ezz_recon_all_the_time_congrats"
```
We can also use the tool dig (Domain Information Groper) 

```
dig -t txt ctctf.easy.unaux.com 

;; ANSWER SECTION:
ctctf.easy.unaux.com.	21599	IN	TXT	"v=spf1 include:flag_ezz_recon_all_the_time_congrats"
``` 


## Flag

```
flag_ezz_recon_all_the_time_congrats
```
