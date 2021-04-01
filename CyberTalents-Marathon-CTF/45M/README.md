
# Challenge Name: 45M


![date](https://img.shields.io/badge/date-09.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Reverse-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)


## Attached files

- [45M.asm](45M.asm)


## Detailed solution

It's an assembly code, we can see two functions **main** and **flag_checker** and some tests to see if the input number correct or wrong. 

Starting by analysing the code, at the main function we can see a printf for the text  "Enter the secret number: " and a scanf to save an integer input. 

Before calling the flag_checker function our input has been moved to the register eax and after to edi 

Now the function flag_checker has veen calledm our input is located at the register edi.  
  
```
        push    rbp
        mov     rbp, rsp
        mov     DWORD PTR [rbp-4], edi
        xor     DWORD PTR [rbp-4], 133337
        sar     DWORD PTR [rbp-4], 3
        add     DWORD PTR [rbp-4], 1337
        sub     DWORD PTR [rbp-4], 137
        mov     edx, DWORD PTR [rbp-4]
        mov     eax, edx
        add     eax, eax
        add     eax, edx
        mov     DWORD PTR [rbp-4], eax
        cmp     DWORD PTR [rbp-4], 1128648
``` 

Our input moved from edi to a variable, let's see the operation workflow  

``` 
flag = flag ^ 133337
flag = flag(remove first 3 bytes / right shifting)
flag = flag + 1337
flag = flag - 137
edx = flag
eax = flag
eax = flagx2
eax = flagx2 + flag = flagx3
x = eax = 3xflag
x = 1128648
``` 
Reversing process  :

1128648 / 3 = 376216 + 137 - 1337 = 375016 -> '1011011100011101000'  

Adding the removed first 3 bytes 1011011100011101000XXX. XXX can be 000, 001, 010, 011, 100, 101, 110, 111. I tried first using 000  

1011011100011101000000 -> 3000128  

3000128 ^ 133337 = 3133337 

Testing our solution, i'll use an online assembly compiler https://carlosrafaelgn.com.br/asm86/  

use variable or registre like ebx  
``` 
        mov     val, 3133337           
        xor     val, 133337
        sar     val, 3
        add     val, 1337
        sub     val, 137
        mov     edx, val
        mov     eax, edx
        add     eax, eax
        add     eax, edx
        mov     val, eax 
``` 

---> val = 1128648 

![45m](https://user-images.githubusercontent.com/72421091/113353826-2a2c5e80-9336-11eb-8ff4-e9c962e53bdc.png)

Lets see our orignal code
``` 
        cmp     val, 1128648  -> true -> jne .L2 not gonna happen -> eax = 1 -> jmp .L3 finish flag function
        mov     DWORD PTR [rbp-8], eax     eax = 1
        cmp     DWORD PTR [rbp-8], 0       false
        je      .L5      --> not gonna happen
        mov     edi, OFFSET FLAT:.LC2
        call    puts   ----> "Correct number :D"
```  

So 3133337 is our secret number


## Flag

```
flag{3133337}
```
