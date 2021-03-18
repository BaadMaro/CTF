
# Challenge Name: steg_2in1


![date](https://img.shields.io/badge/date-06.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![stego category](https://img.shields.io/badge/category-stego-lightgrey.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)


## Attached files

- [flag.jpg](flag.jpg)

## Detailed solution

We start by checking our file, it's just a jpeg image 

```shell
file flag.jpg
flag.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 512x288, components 3
```
The challenge name tell us about a 2 files in 1 file using some stegnography. Let's check with steghide 

```shell
steghide info flag.jpg
"flag.jpg":
  format: jpeg
  capacity: 1.0 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "FLAG.txt":
    size: 36.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```

We can access the embedded file inside the image without a passowrd, let's extract it 

```shell
steghide extract -sf flag.jpg
Enter passphrase:
wrote extracted data to "FLAG.txt".
``` 

Let's open the FLAG.txt.  



## Flag

```
IDEH{woRTH_t0_cheCK_STeGH1DE_F1RsT}
```
