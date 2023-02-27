# Challenge Name: Antediluvian


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-DFIR-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  


## Description

Your company has received a suspicious Word document via email, which is believed to be a targeted attack aimed at compromising the organization. The email address appears to be from a trusted source, but upon closer inspection, something seems off. Your task is to identify and neutralize any potential security threats present in the document before it causes harm to the company's network. This challenge will test your ability to recognize and analyze malicious code and tactics used by attackers. Do not run this on your main machine always. Good luck and be vigilant!

Analyse the file and find an ip addresses that used in this attack

**Download link** : [https://drive.google.com/file/d/1xtSgaeW3HXGH27Erkd_JngFNo9b761b9/view?usp=share_link](https://drive.google.com/file/d/1xtSgaeW3HXGH27Erkd_JngFNo9b761b9/view?usp=share_link)  
**Password** : thnb  
**Flag** : IDEH{IP}  

**Author**: c3p0d4y 

## Detailed solution 

I uploded the file file to virustotal to do a quick overview for the malicious document https://www.virustotal.com/gui/file/28dca7f3b0a2e3796506356cb4cf50461f59534f7b919806440de09e586240f8/details

![image](https://user-images.githubusercontent.com/72421091/221600040-cee73b83-9943-449d-ab20-061857b91865.png)


We can see in behivor tab the techniques used by the malware to infect the target machine https://www.virustotal.com/gui/file/28dca7f3b0a2e3796506356cb4cf50461f59534f7b919806440de09e586240f8/behavior

Here is the attacks used with Execution 

![image](https://user-images.githubusercontent.com/72421091/221599443-dd1151ed-fe33-49f9-b261-7deb30b77458.png)

The malware pull a file called template.dot from a webserver 

![image](https://user-images.githubusercontent.com/72421091/221601014-19de0030-295d-44ac-8d58-e7b6923c31f3.png) 

We got the ip addresses used whith this attack 

You can check the behivor part for more details about the malware like the process tree https://www.virustotal.com/gui/file/28dca7f3b0a2e3796506356cb4cf50461f59534f7b919806440de09e586240f8/behavior

![image](https://user-images.githubusercontent.com/72421091/221601854-8af42eef-236c-4f2c-b25d-e9b5be991fc3.png)

## Flag

```
IDEH{46.101.156.218}
```
