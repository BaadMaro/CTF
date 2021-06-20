# Challenge Name: warmup-rev


![date](https://img.shields.io/badge/date-18.06.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![reverse category](https://img.shields.io/badge/category-Reverse-blueviolet.svg)   
![value](https://img.shields.io/badge/value-371-blue.svg)  



## Description

Time to get warmed up!

- [WarmupRev.java](WarmupRev.java)



## Detailed solution

To be able to solve this challenge we need to :
- Reverse the functions hot, warm, cool and cold
- Find the flag string wich has the length 33 and ```hot(warm(cool(cold(flag))))``` equal to the match string ```"4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy"``` 

We need to reverse the 4 functions hot, warm, cool and cold  

Reversing the functions hot, cool and cold was simple but the function warm can produce the same string from differents output 

Warm function cut a string into 3 parts using the index of "l" and in the end it return 3 parts ```c + b + a```

We can find easy the a part but c and b can have different values. the only thing that we know about c and b that b end with "l"

So the part ```c + b``` can produce differents c and b up to **27 combinations** in our case that can give us the same output after using the warm function 

So in the end we gonna find 27 flag that match the condition ```(flag.length() == 33 && hot(warm(cool(cold(flag)))).equals("4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy"))``` but the correct one should have the flag format **flag{}**
 
Here is the solution [warmup-rev-solve.java](warmup-rev-solve.java)

```java
import java.util.Scanner;


public class WarmupRev {
  
	public static String cold(String t) {
		return t.substring(17) + t.substring(0, 17);
	}

	public static String rcold(String t) {
		return t.substring(16) + t.substring(0, 16);
	}
	
	public static String cool(String t) {
		String s = "";
		for (int i = 0; i < t.length(); i++)
			if (i % 2 == 0)
				s += (char) (t.charAt(i) + 3 * (i / 2));
			else
				s += t.charAt(i);
		return s;
	}

	public static String rcool(String t) {
		String s = "";
		for (int i = 0; i < t.length(); i++)
			if (i % 2 == 0)
				s += (char) (t.charAt(i) - 3 * (i / 2));
			else
				s += t.charAt(i);
		return s;
	}
		
	public static String warm(String t) {
		String a = t.substring(0, t.indexOf("l") + 1);
		String t1 = t.substring(t.indexOf("l") + 1);
		String b = t1.substring(0, t1.indexOf("l") + 1);
		String c = t1.substring(t1.indexOf("l") + 1);
		return c + b + a;
	}


	
	public static String hot(String t) {
		int[] adj = {-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 
				21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, 
				-73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13};
		String s = "";
		for (int i = 0; i < t.length(); i++)
			s += (char) (t.charAt(i) + adj[i]);
		return s;
	}

	public static String rhot(String t) {
		int[] adj = {-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 
				21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, 
				-73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13};
		String s = "";
		for (int i = 0; i < t.length(); i++)
			s += (char) (t.charAt(i) - adj[i]);
		return s;
	}

	public static String rwarm(String test, int i) {
                String a1 = test.substring(test.indexOf("l") + 1);                
                String cb1 = test.substring(0,test.indexOf("l") + 1);            
                String c1 = cb1.substring(0,i); 
                String b1 = cb1.substring(i);
                return a1+b1+c1;


        }

	public static void main(String[] args) {
		String match = "4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy";
                String flag = "";
                for (int i = 0; i < 27; i++) {                       
                       String flag1 = rcold(rcool(rwarm(rhot(match),i)));
                       System.out.println(i + "    =>  " + flag1);
                       if (flag1.length() == 33 && hot(warm(cool(cold(flag1)))).equals(match)) {
			           if (flag1.substring(0,5).equals("flag{")) {
                                       flag = flag1;
                                   }
                       }
                }
                System.out.println();
                System.out.println("The flag is " + flag); // flag{1ncr34s3_1n_3nth4lpy_0f_5y5} with i = 15
                

	}
  
}
```

![image](https://user-images.githubusercontent.com/72421091/122682745-27356180-d1f3-11eb-8732-ee3038ed9fd6.png)



## Flag

```
flag{1ncr34s3_1n_3nth4lpy_0f_5y5}
```
