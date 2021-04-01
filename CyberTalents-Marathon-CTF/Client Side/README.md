
# Challenge Name: Client Side


![date](https://img.shields.io/badge/date-21.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)




## Detailed solution

Starting by opening the challenge link http://35.225.49.73/login/login.html we have a login page  

![image](https://user-images.githubusercontent.com/72421091/113365275-9f575e00-934d-11eb-9050-dd7e6fc27bba.png)

The login verification use the function verify()  

```html
<input type="submit" value="Log in" onclick="verify(); return false;" />
``` 
  
We can see the javascript part with the verify function 

```javascript
<script type="text/javascript">
  function verify() {
    checkpass = document.getElementById("pass").value;
    split = 3;
    if (checkpass.substring(split*8, split*9) == 'd!}') {
      if (checkpass.substring(split*7, split*8) == '4dd') {
        if (checkpass.substring(split*6, split*7) == '$_b') {
          if (checkpass.substring(split*5, split*6) == '3_i') {
           if (checkpass.substring(split*4, split*5) == '$id') {
            if (checkpass.substring(split*3, split*4) == 'nt_') {
              if (checkpass.substring(split*2, split*3) == 'li3') {
                if (checkpass.substring(split, split*2) == 'g{C') {
                  if (checkpass.substring(0,split) == 'fla') {
                    alert("You got the flag!")
                    }
                  }
                }
              }
            }
          }
        }
      }
    }

    else {
      alert("Incorrect password");
    }
  }
</script>
```  
We can see the flag parts from 0 to 9

## Flag

```
flag{Cli3nt_$id3_i$_b4ddd!}
```
