
# Challenge Name: The Mystery Riddle



![date](https://img.shields.io/badge/date-31.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Reverse-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)


## Attached files

- [vim](vim)

## Detailed solution

Let's start by checking our file. It's an elf 64bit executable 

```  
file vim
vim: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=679e4c6b05b68e9917d09772fab3d58bcee70be1, for GNU/Linux 3.2.0, not stripped
``` 

Executing the file show a text and wait to get an input probably to test it 
  
``` 
./vim

How do you exit vim?
I: :q
LET ME ouuuuuuuut!!
``` 

Let's do some reversing using IDA. At the main function we see the text that printed while executing the file, we can also the scanf that save our input  

We can see also some lea and mov instructions to save some strings

![image](https://user-images.githubusercontent.com/72421091/113429351-4aa8f700-93d0-11eb-90be-7607b9c4ba89.png)

After main end we can see some jumps and comparaison 

![image](https://user-images.githubusercontent.com/72421091/113430087-7a0c3380-93d1-11eb-873b-ac9d60fd51b6.png)

At the end we can see a call for strcmp to compare our input with the secret flag and print ```You are a legend o_*``` if we use the right input

![image](https://user-images.githubusercontent.com/72421091/113430183-a1630080-93d1-11eb-8e6f-4d1621f8b8f7.png)

Now we need to add a breakpoint at the strcmp function to leak the secret flag used to compare. I'll use gdb 

Starting by open gdb with our file and check functions 
```
sudo gdb vim
GNU gdb (Debian 10.1-1.7) 10.1.90.20210103-git
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from vim...
(No debugging symbols found in vim)
``` 
  
```  
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001030  strcpy@plt
0x0000000000001040  puts@plt
0x0000000000001050  printf@plt
0x0000000000001060  srand@plt
0x0000000000001070  strcmp@plt
0x0000000000001080  time@plt
0x0000000000001090  __isoc99_scanf@plt
0x00000000000010a0  sleep@plt
0x00000000000010b0  __cxa_finalize@plt
0x00000000000010c0  _start
0x00000000000010f0  deregister_tm_clones
0x0000000000001120  register_tm_clones
0x0000000000001160  __do_global_dtors_aux
0x00000000000011a0  frame_dummy
0x00000000000011a5  main
0x0000000000001920  __libc_csu_init
0x0000000000001980  __libc_csu_fini
0x0000000000001984  _fini
```  
Let's add a breakpoint at the strcmp function and run the file 

```  
(gdb) breakpoint strcmp@plt
Undefined command: "breakpoint".  Try "help".
(gdb) break strcmp@plt
Breakpoint 1 at 0x1070
(gdb) run
Starting program: /home/kali/vim
How do you exit vim?
I: aaaaaaaa

Breakpoint 1, 0x0000555555555070 in strcmp@plt ()
```  

The strcmp function compares the rax register with the rdx register. s2 is the input and s1 is the secret flag

![image](https://user-images.githubusercontent.com/72421091/113433597-68c62580-93d7-11eb-96d0-bc635c5a95b5.png)

Let's leak the registers rax and rdx  
  
```  
(gdb) info registers
rax            0x7fffffffdd80      140737488346496
rbx            0x0                 0
rcx            0x11                17
rdx            0x7fffffffe24c      140737488347724
rsi            0x7fffffffe24c      140737488347724
rdi            0x7fffffffdd80      140737488346496
rbp            0x7fffffffe5a0      0x7fffffffe5a0
rsp            0x7fffffffdd68      0x7fffffffdd68
r8             0x7ffff7fad1c4      140737353798084
r9             0x34c7c4b1          885507249
r10            0x7ffff7fef110      140737354068240
r11            0x7ffff7f4fff0      140737353416688
r12            0x5555555550c0      93824992235712
r13            0x0                 0
r14            0x0                 0
r15            0x0                 0
rip            0x555555555070      0x555555555070 <strcmp@plt>
eflags         0x202               [ IF ]
cs             0x33                51
ss             0x2b                43
ds             0x0                 0
es             0x0                 0
fs             0x0                 0
```  

```
(gdb) x/s 0x7fffffffe24c
0x7fffffffe24c: "aaaaaaaa"
(gdb) x/s 0x7fffffffdd80
0x7fffffffdd80: "flag{Nanda_Yo!:3}"
```  

We can see our input and the secret flag 


## Flag

```
flag{Nanda_Yo!:3}
```
