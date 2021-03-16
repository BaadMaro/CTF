
# Challenge Name: Do I KNOW you? 


![date](https://img.shields.io/badge/date-16.03.2021-brightgreen.svg)  
![solved after CTF](https://img.shields.io/badge/solved-after%20CTF-red.svg) 
![misc category](https://img.shields.io/badge/category-forensics-lightgrey.svg)
![score](https://img.shields.io/badge/score-300-blue.svg)


## Attached files
- [important.zip](important.zip)





## Detailed solution  

The challenge description tell us to try unlocking the zip file and has the word **KNOWN** upercase which we should take it as a hint.  

I tired first to crack the zip encryption key, i extract the pkzip hash using **zip2john** and try to crack it using **john** and **hashcat** with the known wordlist **rockyou** but no success. 

I start searching for attacks used to crack zip files, i finded some talks about an attack called **known-plaintext attack** which match the hint from our challenge.  

I started read more about the attack, i finded a cool article [ZIP known plaintext attacks in-depth exploitation](https://www.programmersought.com/article/13436370754/) that explain it with details.  

In the past, known plaintext attack need to have a complete plaintext file in the encrypted zip file and require the plaintext to be compressed with the same standard, so that the attack may be successful.

But there is some attacks that require only a small part of the plaintext bytes in the encrypted compressed package called **ZIP Attacks with Reduced Known Plaintext** like **Biham and Kocher's attack** :  

- **Paper** : ZIP Attacks with Reduced Known Plaintext https://math.ucr.edu/~mike/zipattacks.pdf

I founded a tool called **Bkcrack** that crack zip encryption with Biham and Kocher's known plaintext attack. We have an explaination in the usage part and a cool demonstration in the tutorial file.   

https://github.com/kimci86/bkcrack   
https://github.com/kimci86/bkcrack/blob/master/example/tutorial.md

**Data required for the attack :**

The attack requires at least 12 bytes of known plaintext. At least 8 of them must be contiguous. The larger the contiguous known plaintext, the faster the attack.

Our important.zip file has two compressed files : backup_of_the_virtual_machine.vdi and flag.txt

````bash
zipinfo important.zip
Archive:  important.zip
Zip file size: 490 bytes, number of entries: 2
-rwxr-x---  3.0 unx       39 TX stor 21-Feb-28 17:31 backup_of_the_virtual_machine.vdi
-rw-r--r--  3.0 unx       35 TX stor 21-Feb-28 17:30 flag.txt
2 files, 74 bytes uncompressed, 74 bytes compressed:  0.0%
````
We can see that we have a .vdi file, it's a VirtualBox Virtual Hard Disk which has a known file header : 

https://en.wikipedia.org/wiki/List_of_file_signatures

````
3C 3C 3C 20 4F 72 61 63 6C 65 20 56 4D 20 56 69 72 74 75 61 6C 42 6F 78 20 44 69 73 6B 20 49 6D 61 67 65 20 3E 3E 3E  

<<< Oracle VM VirtualBox Disk Image >>>
````

We start by creating our plaintext file using the vdi file header :  

````bash
echo -n -e "<<< Oracle VM VirtualBox Disk Image >>>" > plaintext
````
Check the created plaintext file : 

````bash
xxd plaintext
00000000: 3c3c 3c20 4f72 6163 6c65 2056 4d20 5669  <<< Oracle VM Vi
00000010: 7274 7561 6c42 6f78 2044 6973 6b20 496d  rtualBox Disk Im
00000020: 6167 6520 3e3e 3e                        age >>>
````

We run bkcrack : 

./bkcrack -C important.zip -c backup_of_the_virtual_machine.vdi -p plaintext  

![image](https://user-images.githubusercontent.com/72421091/111373052-bfbfc100-869b-11eb-9149-1956a48ad849.png)

We found our keys c0b28d75 388fb6b1 ec96948d now we need to extract the flag.txt file : 

````bash
./bkcrack -C important.zip -c flag.txt -k c0b28d75 388fb6b1 ec96948d -d flag 
bkcrack 1.0.1 - 2021-03-15
Wrote deciphered text.
````

Let's read the flag file


## Flag

```
IDEH{n0t_0nly_cr4ck1ng_1s_th3_k3y}
```
