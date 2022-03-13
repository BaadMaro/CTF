# Challenge Name: Wallet Recover


![date](https://img.shields.io/badge/date-13.03.2022-brightgreen.svg)  
![solved](https://img.shields.io/badge/solved-after%20CTF-red.svg)    
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-30-blue.svg)  


## Description

Created By **sicmundos**

I forgot my wallet password … and now 5 BTC is lost !

Can you help me recover my account?

I will give what you need in FLAG token

[Download Attachement](https://s3.eu-west-3.amazonaws.com/crisis-assets/crisis_attachements/dKl3qBbJCa2AehbOllS4pbky2cFuuVKRflMyZfEA.zip)

## Detailed solution

The attached file contains an android application. We can use an emulator like **Bluestackes** to check it

The app has a login screen 

![image](https://user-images.githubusercontent.com/72421091/158082951-5849995f-c198-40a4-8788-e033ed83ced0.png)

If we try a random username and password we get an error message 

![image](https://user-images.githubusercontent.com/72421091/158082976-691ea423-74c6-44e3-8964-3c2d14a0e16f.png)

Let's start reversing the app, i'll use apktool to extract the apk file

```bash
┌──(kali㉿kali)-[~]
└─$ apktool d -s login.apk -f
I: Using Apktool 2.5.0-dirty on login.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /home/kali/.local/share/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
W: Cant find 9patch chunk in file: "drawable-hdpi-v4/notification_bg_low_normal.9.png". Renaming it to *.png.
W: Cant find 9patch chunk in file: "drawable-xhdpi-v4/notification_bg_normal_pressed.9.png". Renaming it to *.png.
W: Cant find 9patch chunk in file: "drawable-mdpi-v4/notification_bg_normal_pressed.9.png". Renaming it to *.png.
W: Cant find 9patch chunk in file: "drawable-hdpi-v4/notification_bg_normal_pressed.9.png". Renaming it to *.png.
W: Cant find 9patch chunk in file: "drawable-mdpi-v4/notification_bg_low_pressed.9.png". Renaming it to *.png.
W: Cant find 9patch chunk in file: "drawable-xhdpi-v4/notification_bg_normal.9.png". Renaming it to *.png.
W: Cant find 9patch chunk in file: "drawable-mdpi-v4/notification_bg_normal.9.png". Renaming it to *.png.
W: Cant find 9patch chunk in file: "drawable-mdpi-v4/notification_bg_low_normal.9.png". Renaming it to *.png.
W: Cant find 9patch chunk in file: "drawable-hdpi-v4/notification_bg_low_pressed.9.png". Renaming it to *.png.
W: Cant find 9patch chunk in file: "drawable-xhdpi-v4/notification_bg_low_normal.9.png". Renaming it to *.png.
W: Cant find 9patch chunk in file: "drawable-hdpi-v4/notification_bg_normal.9.png". Renaming it to *.png.
W: Cant find 9patch chunk in file: "drawable-xhdpi-v4/notification_bg_low_pressed.9.png". Renaming it to *.png.
I: Decoding values */* XMLs...
I: Copying raw classes.dex file...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```
Output 

![image](https://user-images.githubusercontent.com/72421091/158083102-af17e3df-7834-4691-9067-03597ec019a9.png)

The code is packed into .dex files. Dex stands for Dalvik Executable. A Dex file contains code that is ultimately executed by the Android Runtime.

We can convert dex files to jar files using the dex2jar tool

```bash
┌──(kali㉿kali)-[~]
└─$ d2j-dex2jar login/classes.dex
dex2jar login/classes.dex -> ./classes-dex2jar.jar
```
Now let's decompile the jar file using JD-GUI http://java-decompiler.github.io/

![image](https://user-images.githubusercontent.com/72421091/158083299-0a46a626-d544-4d5f-9109-791caaf89a97.png)

It's a flutter app

When an Android app is built using Flutter, two special libraries are generated for each supported architecture, and stored in the standard lib/ directory inside the APK

More details here : https://rloura.wordpress.com/2020/12/04/reversing-flutter-for-android-wip/

Our focus is libapp.so, it contains all the compiled Dart code written during development .Let's back to the extracted apk and check the lib folder

![image](https://user-images.githubusercontent.com/72421091/158083373-437d5be9-a3ba-41c2-b90a-01f828ba6a22.png)

Challenge is about to find the password so we can start by the easiest by checking **libapp.so** strings

![image](https://user-images.githubusercontent.com/72421091/158083648-0d07137c-945b-4fb2-afaf-b6c800f70368.png)

We found message for the login failure from the app. Let's search for the flag format

![image](https://user-images.githubusercontent.com/72421091/158083694-ef195e82-563d-4f04-a9f8-5f02fc11252c.png)  

We found our flag 

## Flag

```
CRISIS{Jpv1mLlyEU}
```




