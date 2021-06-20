# Practice challenges
https://hsctf.com/#slide-5

![image](https://user-images.githubusercontent.com/72421091/122653582-6903d080-d13d-11eb-9a7d-b02a10f37655.png)



# Challenge Name: Cryptography

![date](https://img.shields.io/badge/date-14.06.2021-brightgreen.svg)  
![crypto category](https://img.shields.io/badge/category-Cryptography-blueviolet.svg)   


## Description

65 63 7a 76 6a 63 62 75 20 63 7a 20 71 6a 67 69 6d 77 7a 76 20 6c 6a 6d 20 65 63 70 74 2e 20 71 71 63 20 76 66 67 61 71 20 66 71 66 20 6f 20 73 64 67 66 20 72 71 70 2c 20 65 78 66 65 6d 20 76 76 75 68 20 75 71 6c 67 20 6b 6d 68 20 66 71 62 20 67 6f 65 6e 20 6c 71 20 6a 74 73 6d 7a 2e 20 61 20 63 75 20 6b 61 62 67 77 75 61 67 72 20 66 77 73 76 20 67 71 69 20 69 74 6a 67 20 69 64 7a 71 20 69 67 20 75 77 6e 6a 71 20 69 7a 6b 61 20 63 62 70 20 6e 67 77 20 6c 67 67 71 67 6e 67 20 62 6a 73 20 64 74 6f 63 7a 66 2c 20 6b 74 78 75 6a 20 71 75 20 68 74 74 20 73 70 61 79 73 64 20 69 67 20 76 70 67 20 64 64 64 74 6e 6d 6f 2e 20 68 74 74 20 63 67 67 20 6b 67 20 75 72 73 70 6a 74 33 6f 77 72 30 76 33 75 2e

## Detailed solution

Decode the hex values using Cyberchef  
  
```
eczvjcbu cz qjgimwzv ljm ecpt. qqc vfgaq fqf o sdgf rqp, exfem vvuh uqlg kmh fqb goen lq jtsmz. a cu kabgwuagr fwsv gqi itjg idzq ig uwnjq izka cbp ngw lggqgng bjs dtoczf, ktxuj qu htt spaysd ig vpg dddtnmo. htt cgg kg urspjt3owr0v3u.
```  

It's a ciphertext let's use a identifier https://www.boxentriq.com/code-breaking/cipher-identifier  

The ciphertext is likely **Vigenere Cipher** 

Let's decode it with https://www.dcode.fr/vigenere-cipher with automatic decryption 

![image](https://user-images.githubusercontent.com/72421091/122653104-7b303f80-d13a-11eb-9390-3a5b74b00bbc.png)

We found our original text with the key **COMPSCI**  

## Flag

```
icanbr3akc0d3s
```

# Challenge Name: Reverse Engineering

![date](https://img.shields.io/badge/date-14.06.2021-brightgreen.svg)  
![reverse category](https://img.shields.io/badge/category-Reverse-blueviolet.svg)   


## Description  

```java    
import java.util.Scanner;


public class SuperSecure {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String input = in.next();
    if(input.length() != 10) {
      System.out.println("LOL no");
      System.exit(0);
    }
    String changed = change(input);
    if(changed.equals("fvbl}bf334")) {
      System.out.println("Awesome!");
      System.out.println("The flag is: " + input);
    } else {
      System.out.println("LOL no");
    }
   }
   private static String change(String s) {
    char[] temp = new char[10];
    for(int i = 0; i < s.length(); i++) {
      temp[i] = (char)(s.charAt(i) + 3);
    }
    return new String(temp);
  }
}

``` 
## Detailed solution

Our flag is the reversed output from the change function that is equal to **fvbl}bf334** 

So we need to reverse the change function 

```python
changed = 'fvbl}bf334'
flag = ''

for i in changed:
    flag += chr(ord(i) - 3)

print(flag)
```
  
## Flag

```
cs_iz_c001
```

# Challenge Name: Recon

![date](https://img.shields.io/badge/date-14.06.2021-brightgreen.svg)  
![Misc category](https://img.shields.io/badge/category-Misc-blueviolet.svg)   


## Description




[sample-recon.jpg](sample-recon.jpg)

## Detailed solution

Checking the image 
```
┌──(kali㉿kali)-[~]
└─$ file sample-recon.jpg
sample-recon.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 2400x1800, components 3
```
```
┌──(kali㉿kali)-[~]
└─$ exiftool sample-recon.jpg
ExifTool Version Number         : 12.16
File Name                       : sample-recon.jpg
Directory                       : .
File Size                       : 2.5 MiB
File Modification Date/Time     : 2021:06:14 11:58:02+00:00
File Access Date/Time           : 2021:06:14 19:09:16+00:00
File Inode Change Date/Time     : 2021:06:14 19:09:16+00:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Image Width                     : 2400
Image Height                    : 1800
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2400x1800
Megapixels                      : 4.3
```
Zooming at image 
  
![image](https://user-images.githubusercontent.com/72421091/122653464-81bfb680-d13c-11eb-8ba7-07e561de1e6e.png)

``` The blank is the key. I made a program to calculate _______ numbers ```  

Searching using the image we found that it's **Ada Lovelace**  

https://en.wikipedia.org/wiki/Ada_Lovelace   

Ada Lovelace's notes were labelled alphabetically from A to G. In note G, she describes an algorithm for the Analytical Engine to compute **Bernoulli numbers**


## Flag

```
Bernoulli
```
