
# Challenge Name: USB SN


![date](https://img.shields.io/badge/date-06.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Medium-blue.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)


## Attached files

- [System.evtx](System.evtx)

## Detailed solution

The challenge is to find the serial number for a SanDisk USB. Starting by checking the file, it's a windows event log (evtx).  

I'll use a tool called EvtxECmd to parse data as json 

https://ericzimmerman.github.io/#!index.md 

```
EvtxECmd -f System.evtx --json "C:\Users\maros\Desktop\EvtxExplorer"
``` 
  
Searching for usb devices we found a DeviceInstanceID  

```
"DeviceInstanceID: STORAGE\\VOLUME\\_??_USBSTOR#DISK&amp;VEN_SANDISK&amp;PROD_ULTRA_USB_3.0&amp;REV_1.00#4C530000080406123243&amp;0#{53F56307-B6BF-11D0-94F2-00A0C91EFB8B}"
```  

It contains :
- Vendor (VEN) : SANDISK
- Product name (Prod) : ULTRA USB 3.0
- Revision : 1.00
- Serial Number : 4C530000080406123243

Flag format is md5 of the usb serial number  

## Flag

```
flag{a46a2bae610f55525c5995a5b831c768}
```
