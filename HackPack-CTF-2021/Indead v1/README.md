# Challenge Name: Indead v1




![date](https://img.shields.io/badge/date-17.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![misc category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Medium-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)

## Description

Job posting website for security experts, pentesters and hackers. http://indead-upload-avatar.ctf2021.hackpack.club

Hint : flag.txt is located in /var/www/ 

## Detailed solution 

Starting by opening http://indead-upload-avatar.ctf2021.hackpack.club we can see a upload file feature used to upload pictures

We can bypass the upload function and upload a php shell using an image file header or merge an image with our php code and change content-type to image 

Uploading an image and checking the requests i found that the file has been uploaded to ```/very_long_directory_path/``` 

Checking the source page i found some tags which is a php webshell https://gist.github.com/joswr1ght/22f40787de19d80d110b37fb79ac3985 

I didn't check the upload using a fake image php webshell so i just used the php shell that i found 

We know from hint that the flag.txt is in /var/www/ so i listed the files inside /var/www to verify 
  
```
cd /var/www/ && cat flag.txt https://indead-upload-avatar.ctf2021.hackpack.club/very_long_directory_path/?cmd=cd+%2Fvar%2Fwww%2F+%26%26+cat+flag.txt
```




## Flag

```
flag{y3t_an0ther_file_uplo@d_vuln}
```
