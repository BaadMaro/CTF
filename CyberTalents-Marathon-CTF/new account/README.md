
# Challenge Name: new account



![date](https://img.shields.io/badge/date-28.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)


## Attached files

- [Security436509324654726509.evtx](Security436509324654726509.evtx)

## Detailed solution

An attacker after compromising the machine added a new account as admin  

Starting by checking the file, it's a windows event log (evtx).  

I'll use a tool called EvtxECmd to parse data as json

https://ericzimmerman.github.io/#!index.md 
  
```
EvtxECmd -f System.evtx --json "C:\Users\maros\Desktop\EvtxExplorer"
```  
We need to search for two event IDs : 

- Event ID 4720 : A user account was created
- Event ID 4732 : A member was added to a security-enabled local group 

We found the event id 4720, a new user was created withe name **Sam** 
  
```json
{"PayloadData1":"Target: John-PC\\Sam (S-1-5-21-792323161-214100996-3742390483-1003)","UserName":"John-PC\\John (S-1-5-21-792323161-214100996-3742390483-1000)","MapDescription":"New user created","ChunkNumber":1,"Computer":"John-PC","Payload":"{\"EventData\":{\"Data\":[{\"@Name\":\"TargetUserName\",\"#text\":\"Sam\"},{\"@Name\":\"TargetDomainName\",\"#text\":\"John-PC\"},{\"@Name\":\"TargetSid\",\"#text\":\"S-1-5-21-792323161-214100996-3742390483-1003\"},{\"@Name\":\"SubjectUserSid\",\"#text\":\"S-1-5-21-792323161-214100996-3742390483-1000\"},{\"@Name\":\"SubjectUserName\",\"#text\":\"John\"},{\"@Name\":\"SubjectDomainName\",\"#text\":\"John-PC\"},{\"@Name\":\"SubjectLogonId\",\"#text\":\"0x177F1\"},{\"@Name\":\"PrivilegeList\",\"#text\":\"-\"},{\"@Name\":\"SamAccountName\",\"#text\":\"Sam\"},{\"@Name\":\"DisplayName\",\"#text\":\"%%1793\"},{\"@Name\":\"UserPrincipalName\",\"#text\":\"-\"},{\"@Name\":\"HomeDirectory\",\"#text\":\"%%1793\"},{\"@Name\":\"HomePath\",\"#text\":\"%%1793\"},{\"@Name\":\"ScriptPath\",\"#text\":\"%%1793\"},{\"@Name\":\"ProfilePath\",\"#text\":\"%%1793\"},{\"@Name\":\"UserWorkstations\",\"#text\":\"%%1793\"},{\"@Name\":\"PasswordLastSet\",\"#text\":\"%%1794\"},{\"@Name\":\"AccountExpires\",\"#text\":\"%%1794\"},{\"@Name\":\"PrimaryGroupId\",\"#text\":\"513\"},{\"@Name\":\"AllowedToDelegateTo\",\"#text\":\"-\"},{\"@Name\":\"OldUacValue\",\"#text\":\"0x0\"},{\"@Name\":\"NewUacValue\",\"#text\":\"0x15\"},{\"@Name\":\"UserAccountControl\",\"#text\":\", %%2080, %%2082, %%2084\"},{\"@Name\":\"UserParameters\",\"#text\":\"%%1793\"},{\"@Name\":\"SidHistory\",\"#text\":\"-\"},{\"@Name\":\"LogonHours\",\"#text\":\"%%1797\"}]}}","Channel":"Security","Provider":"Microsoft-Windows-Security-Auditing","EventId":4720,"EventRecordId":"443","ProcessId":496,"ThreadId":1092,"Level":"LogAlways","Keywords":"Audit success","SourceFile":"C:\\Users\\maros\\Desktop\\EvtxExplorer\\security.evtx","ExtraDataOffset":0,"HiddenRecord":false,"TimeCreated":"2020-06-09T15:51:03.9362930+00:00","RecordNumber":443}
``` 

We found the event id 4732, a member with the User SID S-1-5-21-792323161-214100996-3742390483-1003 has been added to Administrators group. It's the user Sam  
  
```json
{"PayloadData1":"Target: Builtin\\Administrators (S-1-5-32-544)","PayloadData2":"SubjectLogonId: 0x177F1","PayloadData3":"MemberName: -","PayloadData4":"MemberSid: S-1-5-21-792323161-214100996-3742390483-1003","PayloadData5":"PrivilegeList: -","UserName":"John-PC\\John (S-1-5-21-792323161-214100996-3742390483-1000)","MapDescription":"A member was added to a security-enabled local group","ChunkNumber":1,"Computer":"John-PC","Payload":"{\"EventData\":{\"Data\":[{\"@Name\":\"MemberName\",\"#text\":\"-\"},{\"@Name\":\"MemberSid\",\"#text\":\"S-1-5-21-792323161-214100996-3742390483-1003\"},{\"@Name\":\"TargetUserName\",\"#text\":\"Administrators\"},{\"@Name\":\"TargetDomainName\",\"#text\":\"Builtin\"},{\"@Name\":\"TargetSid\",\"#text\":\"S-1-5-32-544\"},{\"@Name\":\"SubjectUserSid\",\"#text\":\"S-1-5-21-792323161-214100996-3742390483-1000\"},{\"@Name\":\"SubjectUserName\",\"#text\":\"John\"},{\"@Name\":\"SubjectDomainName\",\"#text\":\"John-PC\"},{\"@Name\":\"SubjectLogonId\",\"#text\":\"0x177F1\"},{\"@Name\":\"PrivilegeList\",\"#text\":\"-\"}]}}","Channel":"Security","Provider":"Microsoft-Windows-Security-Auditing","EventId":4732,"EventRecordId":"448","ProcessId":496,"ThreadId":540,"Level":"LogAlways","Keywords":"Audit success","SourceFile":"C:\\Users\\maros\\Desktop\\EvtxExplorer\\security.evtx","ExtraDataOffset":0,"HiddenRecord":false,"TimeCreated":"2020-06-09T15:51:04.0664802+00:00","RecordNumber":448}
``` 
  
**Bonus**  

We can use a tool called deepBlueCLI, it's a PwerShell Module for Threat Hunting via Windows Event Logs  

https://github.com/sans-blue-team/DeepBlueCLI  

![image](https://user-images.githubusercontent.com/72421091/113418911-51c70980-93be-11eb-8bb3-d0103898337a.png)

As we can see a user with name Sam has been created and added to the local administrators group  

Flag format is the md5 of the username  

Md5(Sam) = ba0e0cde1bf72c28d435c89a66afc61a  

## Flag

```
flag{ba0e0cde1bf72c28d435c89a66afc61a}
```
