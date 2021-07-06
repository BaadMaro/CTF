# Challenge Name: HK-GANG CTF-1


![date](https://img.shields.io/badge/date-01.07.2021-brightgreen.svg)  
![misc category](https://img.shields.io/badge/category-WMisc-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)


## Description

i lost my file in this link find it for me please i need my file

https://www.men.gov.ma/AR/LISTS/SURVEY2/summary.ASPX?isDlg=1

Author : Abdelkarim Mouchquelita

Challenge link : https://hkgang.com/%d8%a5%d9%81%d8%aa%d8%aa%d8%a7%d8%ad-%d8%b5%d9%86%d9%81-%d8%a7%d9%84%d8%aa%d8%ad%d8%af%d9%8a%d8%a7%d8%aa-ctf-1/ 

## Detailed solution

Start by opening the link and we can see some strings at the end

![image](https://user-images.githubusercontent.com/72421091/124539429-6085e800-de15-11eb-8c2e-dad4c6994b23.png)

- thm{flag}

- http://itor.novola.co.il/btw_mbrok_3lina.jpeg
	 
- dGFfd2FjaF9tbl9ueXRla19iYWdoaV9sZmxhZ19iaGFkX3NvaG9sYQ==
 	 
- bWdodGw5YWNoX2xmbGFnX2huYV9rbmtoYWZvX2w5cjNh

As we can see the last two strings are base64 encoded, let's decode them

```bash
┌──(kali㉿kali)-[~]
└─$ echo "bWdodGw5YWNoX2xmbGFnX2huYV9rbmtoYWZvX2w5cjNh" | base64 -d
mghtl9ach_lflag_hna_knkhafo_l9r3a  
```

```bash
┌──(kali㉿kali)-[~]
└─$ echo "dGFfd2FjaF9tbl9ueXRla19iYWdoaV9sZmxhZ19iaGFkX3NvaG9sYQ==" | base64 -d
ta_wach_mn_nytek_baghi_lflag_bhad_sohola
```
Sentences is in Moroccan language and it's mean that there is no flag here x)

No let's switch to the link that we found http://itor.novola.co.il/btw_mbrok_3lina.jpeg  

![image](https://user-images.githubusercontent.com/72421091/124539811-0fc2bf00-de16-11eb-8618-a08b64dc78bf.png)

Let's analyze the image file 

```bash
┌──(kali㉿kali)-[~]
└─$ file btw_mbrok_3lina.jpeg
btw_mbrok_3lina.jpeg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, comment: "http://itor.novola.co.il/its_{...}.txt  brackets=what you need", baseline, precision 8, 225x225, components 3
```  

Checking strings and we found a new hint

```bash
┌──(kali㉿kali)-[~]
└─$ strings btw_mbrok_3lina.jpeg
JFIF
@http://itor.novola.co.il/its_{...}.txt  brackets=what you need
%7%*.1444
$:?<2>-361
9($(934366133133333<35333133<1333333533333333333333333
```
http://itor.novola.co.il/its_{...}.txt  brackets=what you need => we need flag so let's replace it in the new link 

http://itor.novola.co.il/its_flag.txt  
  
```
HHHHHHH NOOPE IS NOT A FLAG BUT FROM THIS CODE YOU CAN GET YOUR FLAG ENJOY. @MCHKLT



UEsDBAoACQAAABeF3FInPEYAJQAAABkAAAAEABwAZmxhZ1VUCQADfu3ZYJPt2WB1eAsAAQToAwAABOgDAACZ+Erjlaph7Vt5BFooXLiR8d4BrpMPyPMRdp9gh2FH/gH4v+G7UEsHCCc8RgAlAAAAGQAAAFBLAQIeAwoACQAAABeF3FInPEYAJQAAABkAAAAEABgAAAAAAAEAAACkgQAAAABmbGFnVVQFAAN+7dlgdXgLAAEE6AMAAAToAwAAUEsFBgAAAAABAAEASgAAAHMAAAAAAA==


@file, bye.
```  
Another base64 encoded string let's decode it 
  
```bash


┌──(kali㉿kali)-[~]
└─$ echo "UEsDBAoACQAAABeF3FInPEYAJQAAABkAAAAEABwAZmxhZ1VUCQADfu3ZYJPt2WB1eAsAAQToAwAABOgDAACZ+Erjlaph7Vt5BFooXLiR8d4BrpMPyPMRdp9gh2FH/gH4v+G7UEsHCCc8RgAlAAAAGQAAAFBLAQIeAwoACQAAABeF3FInPEYAJQAAABkAAAAEABgAAAAAAAEAAACkgQAAAABmbGFnVVQFAAN+7dlgdXgLAAEE6AMAAAToAwAAUEsFBgAAAAABAAEASgAAAHMAAAAAAA==" | base64 -d
PK
        ▒▒R'<F%flagUT   ~▒▒`▒▒▒`ux
                                  ▒▒▒▒J㕪a▒[yZ(\▒▒▒▒▒▒▒▒v▒`▒aG▒▒▒P'<F%PK
        ▒▒R'<F%▒▒flagUT~▒▒`ux
                             ▒▒PKJs 
                             
```
We have a binary file. Looking at the header we can see PK which mean that the file is a zip https://en.wikipedia.org/wiki/List_of_file_signatures 

Decode and saving the file  

```bash
echo "UEsDBAoACQAAABeF3FInPEYAJQAAABkAAAAEABwAZmxhZ1VUCQADfu3ZYJPt2WB1eAsAAQToAwAABOgDAACZ+Erjlaph7Vt5BFooXLiR8d4BrpMPyPMRdp9gh2FH/gH4v+G7UEsHCCc8RgAlAAAAGQAAAFBLAQIeAwoACQAAABeF3FInPEYAJQAAABkAAAAEABgAAAAAAAEAAACkgQAAAABmbGFnVVQFAAN+7dlgdXgLAAEE6AMAAAToAwAAUEsFBgAAAAABAAEASgAAAHMAAAAAAA==" | base64 -d > 1.zip
```  

```bash
┌──(kali㉿kali)-[~]
└─$ file 1.zip                                                                                                    
1.zip: Zip archive data, at least v1.0 to extract
``` 
  
``` 
┌──(kali㉿kali)-[~]
└─$ zipinfo 1.zip
Archive:  1.zip
Zip file size: 211 bytes, number of entries: 1
-rw-r--r--  3.0 unx       25 TX stor 21-Jun-28 15:40 flag
1 file, 25 bytes uncompressed, 25 bytes compressed:  0.0%
``` 
As we can see the file is zip that has a flag file compressed. Let's try to extract it 
  
``` bash
┌──(kali㉿kali)-[~]
└─$ unzip 1.zip
Archive:  1.zip
[1.zip] flag password:
   skipping: flag                    incorrect password
``` 

The zip file is protected we need to crack the password. I'm gonna use **zip2john** to extract the hash and crack it with **john**  

```bash
┌──(kali㉿kali)-[~]
└─$ zip2john 1.zip > hash.txt                                                                                     
```
```bash
┌──(kali㉿kali)-[~]
└─$ cat hash.txt
1.zip/flag:$pkzip2$1*2*2*0*25*19*463c27*0*3e*0*25*0046*8517*99f84ae395aa61ed5b79045a285cb891f1de01ae930fc8f311769f60876147fe01f8bfe1bb*$/pkzip2$:flag:1.zip::1.zip
```
it's PKZIP. Let's use john to crack the hash we can try first with john default wordlist

```bash
┌──(kali㉿kali)-[~]
└─$ john --format=pkzip hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 1 candidate buffered for the current salt, minimum 8 needed for performance.
Warning: Only 4 candidates buffered for the current salt, minimum 8 needed for performance.
Warning: Only 1 candidate buffered for the current salt, minimum 8 needed for performance.
Warning: Only 7 candidates buffered for the current salt, minimum 8 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
Warning: Only 6 candidates buffered for the current salt, minimum 8 needed for performance.
Proceeding with wordlist:/usr/share/john/password.lst, rules:Wordlist
Proceeding with incremental:ASCII
0g 0:00:00:12  3/3 0g/s 6968Kp/s 6968Kc/s 6968KC/s kbmo0c..kbmgaw
0g 0:00:00:14  3/3 0g/s 7180Kp/s 7180Kc/s 7180KC/s 1boaar..1bozdi
0g 0:00:01:16  3/3 0g/s 7816Kp/s 7816Kc/s 7816KC/s bevged80..bevg06jk
99999            (1.zip/flag)
1g 0:00:01:20 DONE 3/3 (2021-07-01 22:12) 0.01247g/s 7865Kp/s 7865Kc/s 7865KC/s 7r5p8..99912
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```
```bash
┌──(kali㉿kali)-[~]
└─$ john --show hash.txt
1.zip/flag:99999:flag:1.zip::1.zip

1 password hash cracked, 0 left
```  

We were able to crack the zip hash, the password is 99999 

Let's extract the flag file from zip using the password 
  
```bash
┌──(kali㉿kali)-[~]
└─$ unzip 1.zip                                                                                                  
Archive:  1.zip
[1.zip] flag password:
 extracting: flag
```

```bash
┌──(kali㉿kali)-[~]
└─$ cat flag
HKG{t4e_b3st_1n_m0rocc0}
``` 

And we found our flag  

## Flag

```
HKG{t4e_b3st_1n_m0rocc0}
```
