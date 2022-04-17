# Challenge Name: Container


![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-OSINT-blueviolet.svg)   
![value](https://img.shields.io/badge/value-150-blue.svg)  


## Description

we recently brought this container to transofm it into a amahlaba . you need to find our customer name and Manufacturer  

flag format thnb{customername_Manufacturername} 

_Author : c3p0d4y_  

[container.jpg](https://thnbdarija.ctfd.io/files/fe98dc670c61a6bf156e7f3b3d4566a8/container.jpg?token=eyJ1c2VyX2lkIjoyNywidGVhbV9pZCI6MTUsImZpbGVfaWQiOjF9.YltdMQ.cPo78SQUxp3QlqEO-QUmHwZFvdc)
  
## Detailed solution

Start by checking the image

![container](https://user-images.githubusercontent.com/72421091/163735784-f25d7fde-3365-42f2-8022-dfcb5abe7afc.jpg)

Doing some research we found some details about container identification system https://transportgeography.org/contents/chapter5/intermodal-transportation-containerization/container-identification-system/  

![image](https://user-images.githubusercontent.com/72421091/163735812-7223ea64-dd7a-4ddd-ad77-38a73e96b244.png)

Let's list our container details 

- Owner code : ARD
- Product group code : U
- Registration number  : 501207
- Check digit : 8
- Size and type code : 45G1

ARD is used by company called CARU Containers B.V., we can use there portal to search for our container using the container number **ARDU5012078**  

https://portal.carucontainers.com/

https://portal.carucontainers.com/scripts/caruweb02.wsc/WService=caru/system/web/sp-web-menu.r?program=DP.WEB-UNIT_INQUIRY&containernumber=ARDU5012078&Submit=Open 

![image](https://user-images.githubusercontent.com/72421091/163735920-7aee8d94-b88c-4210-978a-251d1785d64d.png)

We have also some attachements  

![image](https://user-images.githubusercontent.com/72421091/163735931-a0cb9f54-d611-42d0-a6c3-53660de074f8.png)

CSC Plate/Certification has some technical details https://portal.carucontainers.com/scripts/caruweb02.wsc/WService=caru/system/web/sp-web-stream_attachment.r?attachmentnr=2748628&attseqnr=1&companycode=CS&accesstoken=ciicjlYkBfkdndjC

We are intrested in Customername and Manufacturername  

![image](https://user-images.githubusercontent.com/72421091/163735994-60fbd9c9-22ab-422a-a512-39dc6c81672e.png)

![image](https://user-images.githubusercontent.com/72421091/163736005-d1dd3657-85ec-481f-8f8f-6930f4e31fde.png)  

The flag format is thnb{customername_Manufacturername}

## Flag

```
thnb{CARU_SBPC}
```
