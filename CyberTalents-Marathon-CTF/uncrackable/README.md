
# Challenge Name: uncrackable



![date](https://img.shields.io/badge/date-11.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Medium-blue.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)


## Attached files

- [uncrackable.tar.gz](uncrackable.tar.gz)

## Detailed solution

Started by extracting the file  
  
```
extract tar -xvf uncrackable.tar.gz 
```
We found a PDF file and a folder that contains many files. The PDF is protected by a password. 

Let's extract the hash from the PDF to crack it. I'll use pdf2john  
  
```bash
root@kali:~# python pdf2john.py sec2.pdf
sec2.pdf:$pdf$2*3*128*-3904*1*16*9db3c812d6a0c898af95886f6d043eaa*32*44041e94111587f666acac56c794a44f00000000000000000000000000000000*32*1df5734e447cc82abf998e9befa24a81ca624be57d6759bb964b7c41ebc6a03a:::::sec2.pdf
```  
I tried to crack it using the wordlist rockyou but no success.  

I noticed that the filenames in the data folder kinda similar, so i tired to use the filenames as a wordlist to crack the pdf hash   
  
```bash
root@kali:~/data# ls -1 | sed -e 's/\..*$//' > /root/1.txt
``` 
Let's use the filenames wordlist to crack the pdf hash using john  

```bash
root@kali:~# john --wordlist=1.txt hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PDF [MD5 SHA2 RC4/AES 32/64])
Cost 1 (revision) is 3 for all loaded hashes
Press 'q' or Ctrl-C to abort, almost any other key for status
2kqefH793Gn81YJATlGJd6zgfVBVhIKX (sec2.pdf)
1g 0:00:00:00 DONE (2021-03-11 15:11) 100.0g/s 3600p/s 3600c/s 3600C/s 2jV0socJDeUhH83R5aa8l4kqhbKx0yUn..2lVxw4oLrOTkuH1wc6nNJausvdYu9Qoi
Use the "--show --format=PDF" options to display all of the cracked passwords reliably
Session completed
``` 
We found the password : ```2kqefH793Gn81YJATlGJd6zgfVBVhIKX```  

Now let's open the PDF using the password  

 ![image](https://user-images.githubusercontent.com/72421091/113355943-70cf8800-9339-11eb-8222-10a51aec53c3.png)



## Flag

```
FLag{A_dRop0ut_wi1l_b3at_4_geNius_7hrou9h_haRd_worK}
```
