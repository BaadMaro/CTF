# Challenge Name: Simple CAuthentification


![date](https://img.shields.io/badge/date-06.03.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Reverse-blueviolet.svg)   
![value](https://img.shields.io/badge/value-10-blue.svg)  


## Description

Created By **m4rc0s**

You should reverse this binary to know the flag.

Attempt to get the password

[Download Attachement](https://s3.eu-west-3.amazonaws.com/crisis-assets/crisis_attachements/KCEPBe2Emug0PeTspqA2gcEEOW0UeCn0BxnCT8MS.zip)

## Detailed solution

Let's start by checking our file auth. It's an elf 64-bit executable

```bash
┌──(kali㉿kali)-[~]
└─$ file auth
auth: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=5f8fefb60a5f9db2b9b492e534c43a0e01f443da, for GNU/Linux 3.2.0, not stripped
```

Let's execute it

```bash
┌──(kali㉿kali)-[~]
└─$ ./auth
Please insert your password :
123
Incorrect Password  
```
We need the find the password. Let's do some reversing using GHIDRA

Here is the main function

```c

undefined8 main(void)

{
  int iVar1;
  long in_FS_OFFSET;
  char local_28 [24];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  puts("Please insert your password : ");
  __isoc99_scanf(&DAT_00102027,local_28);
  iVar1 = strcmp(local_28,"DfX2NNNNN==");
  if (iVar1 == 0) {
    putchar(0x43);
    putchar(0x52);
    putchar(0x49);
    putchar(0x53);
    putchar(0x49);
    putchar(0x53);
    putchar(0x7b);
    putchar(99);
    putchar(0x38);
    putchar(0x78);
    putchar(0x6f);
    putchar(0x31);
    putchar(0x62);
    putchar(0x44);
    putchar(0x7d);
  }
  else {
    printf("Incorrect Password");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

Our input is stored in a variable and used with strcmp function to compare it with the password **DfX2NNNNN==**

The output when we send the right input is the secret key, listed using hex chars one by one

We can either decode the hex chars or use the password **DfX2NNNNN==** to get it from the executable 

![image](https://user-images.githubusercontent.com/72421091/156961722-73d49576-97ec-4fcb-addc-b2e60b9c632f.png)

We found our flag

## Flag

```
CRISIS{c8xo1bD}
```
