# Challenge Name: suspicious-traffic

![date](https://img.shields.io/badge/date-24.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![Steganography category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-200-blue.svg)  


## Description

I got a hold of a packet capture between a suspicious client and server. It looks really strange, could you take a look?

[capture.pcapng](capture.pcapng)

## Detailed solution

Opening the pcap file with wireshark and searching for http requests i found some http requests with a 2 bytes data XX0A

![image](https://user-images.githubusercontent.com/72421091/116089396-58316400-a692-11eb-8125-25b8730ad0c8.png)

We can see our flag format characters in the first 3 http requests with data. we can use the filter ```http && data``` to get only http requests with data  

I'll use tshark to extract data using the filter, remove the last byte 0A and convert to ascii 
 
```
tshark  -r capture.pcapng -Y "http && data" -T fields -e data | cut -c -2 | xxd -r -p 
```

We got our flag 


## Flag

```
WPI{su3p1ci0uS_htTp}  
```
