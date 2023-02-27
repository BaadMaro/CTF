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

Let's check the source code

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

As we can see our input ($expression) is being used in eval function

we need bypass the preg_match regex and try to inject data to perform command execuction

## Flag
