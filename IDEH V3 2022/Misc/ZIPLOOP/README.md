# Challenge Name: ZIPLOOP


![date](https://img.shields.io/badge/date-06.03.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Misc-blueviolet.svg)   
![value](https://img.shields.io/badge/value-20-blue.svg)  

## Description

Created By **m4rc0s**

The flag is zipped 500 times, can you extract it?

> Be smart and dont waste your time on doing the process manually.  

[Download Attachement](https://s3.eu-west-3.amazonaws.com/crisis-assets/crisis_attachements/Aqt5WMmlmIDh06ow6oAo6YHKUsMeDpSgddT25GXS.zip)

## Detailed solution

![image](https://user-images.githubusercontent.com/72421091/157146263-414b94a2-966a-4ea1-84c7-56bd15af3b23.png)

We have a file that has been zipped 500 times so we need to create a script to unzip all file to find the flag

```bash
#!/bin/bash
for i in {499..0}
do
    unzip $i.zip;
done
```
```
Archive:  10.zip
 extracting: 9.zip
Archive:  9.zip
 extracting: 8.zip
Archive:  8.zip
 extracting: 7.zip
Archive:  7.zip
 extracting: 6.zip
Archive:  6.zip
 extracting: 5.zip
Archive:  5.zip
 extracting: 4.zip
Archive:  4.zip
 extracting: 3.zip
Archive:  3.zip
 extracting: 2.zip
Archive:  2.zip
 extracting: 1.zip
Archive:  1.zip
 extracting: flag
unzip:  cannot find or open 0.zip, 0.zip.zip or 0.zip.ZIP.
```
The last zip file was 1.zip

Let's read **flag** file

## Flag

```
CRISIS{ff9f33b7ec2}
```
