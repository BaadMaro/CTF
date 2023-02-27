# Challenge Name: Locked Portal


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Reverse-blueviolet.svg)   
![value](https://img.shields.io/badge/value-75-blue.svg)  


## Description

I want to access the portal to enter IDEH Reversing world, but they keep asking me to give them a code, can you help me?

**Author**: kw4ntum

## Detailed solution

Start by checking our file. It's a linux ELF binary

![image](https://user-images.githubusercontent.com/72421091/221604850-4be0a88c-9172-4525-a6a4-f3b1acc478c7.png)

If we run the binary, we can see a prompt for a password 

![image](https://user-images.githubusercontent.com/72421091/221605281-1c7c2a1c-7153-496d-b252-b934ece4c2c9.png)

I switched to ghidra to analyze our binary file and try to understand how the password check work 

The program take our password input and use a function called check_password to check if we have acces or not

Here is the decomplied main function 

```c

void main(void)

{
  char cVar1;
  size_t sVar2;
  char local_28 [32];
  
  printf("Enter password: ");
  fgets(local_28,0x1a,stdin);
  sVar2 = strcspn(local_28,"\n");
  local_28[sVar2] = '\0';
  cVar1 = check_password(local_28);
  if (cVar1 == '\0') {
    puts("Access denied, lol!");
  }
  else {
    puts("Access granted. Welcome to IDEH!");
  }
  return 0;
}
```

Now let's check the function check_password 

```c
int check_password(char *param_1)

{
  size_t sVar1;
  int uVar2;
  
  sVar1 = strlen(param_1);
  if ((int)sVar1 == 0x19) {
    if ((((*param_1 == 'I') && (param_1[5] == 'n')) && (param_1[10] == '3')) &&
       ((param_1[0xf] == 'd' && (param_1[0x14] == 'r')))) {
      if ((((param_1[1] == 'D') && ((param_1[6] == '0' && (param_1[0xb] == '_')))) &&
          (param_1[0x10] == 'y')) && (param_1[0x15] == '_')) {
        if ((((param_1[2] == 'E') && (param_1[7] == 'w')) && (param_1[0xc] == 'r')) &&
           ((param_1[0x11] == '_' && (param_1[0x16] == 'r')))) {
          if (((param_1[3] == 'H') && ((param_1[8] == 'm' && (param_1[0xd] == '3')))) &&
             ((param_1[0x12] == 'f' && (param_1[0x17] == '3')))) {
            if ((((param_1[4] == '{') && (param_1[9] == '_')) && (param_1[0xe] == '4')) &&
               ((param_1[0x13] == '0' && (param_1[0x18] == 'v')))) {
              uVar2 = 1;
            }
            else {
              uVar2 = 0;
            }
          }
          else {
            uVar2 = 0;
          }
        }
        else {
          uVar2 = 0;
        }
      }
      else {
        uVar2 = 0;
      }
    }
    else {
      uVar2 = 0;
    }
  }
  else {
    uVar2 = 0;
  }
  return uVar2;
}
```

The function does multiple checks with a comparasion for the characters used in our input and the correct one 

We have the order for each position with param_1[X]. We can append the password manually or use a quick code. 

Here a python code : 

```python
param_1 = [0]*0x19
param_1[0] = 'I'
param_1[1] = 'D'
param_1[2] = 'E'
param_1[3] = 'H'
param_1[4] = '{'
param_1[5] = 'n'
param_1[6] = '0'
param_1[7] = 'w'
param_1[8] = 'm'
param_1[9] = '_'
param_1[10] = '3'
param_1[0x10] = 'y'
param_1[0x11] = '_' 
param_1[0x12] = 'f'
param_1[0x13] = '0'
param_1[0x14] = 'r'
param_1[0x15] = '_'
param_1[0x16] = 'r'
param_1[0x17] = '3'
param_1[0x18] = 'v'
param_1[0xf] = 'd'
param_1[0xb] = '_'
param_1[0xd] = '3'
param_1[0xe] = '4'
param_1[0x13] = '0'
param_1[0xc] = 'r'

print(''.join(p for p in param_1))
```
We got our flag. We just need to add "}" at the end

Here is the c code for our program [locked-portal.c](locked-portal.c)

## Flag

```
IDEH{n0wm_3_r34dy_f0r_r3v}
```
