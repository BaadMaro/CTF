
# Challenge Name: password change


![date](https://img.shields.io/badge/date-28.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)


## Attached files

- [SAM84398934653746593](SAM84398934653746593)

## Detailed solution

The solution for the challenge is to find the password reset date for the user John  

It's a Sam registry file let's extract data using [RegRipper](https://github.com/keydet89/RegRipper3.0)  

```  
Hive (C:\Users\maros\Downloads\SAM84398934653746593) is not dirty.

samparse v.20200825
(SAM) Parse SAM file for user & group mbrshp info


User Information
-------------------------
Username        : Administrator [500]
Full Name       : 
User Comment    : Built-in account for administering the computer/domain
Account Type    : Default Admin User
Account Created : 2020-06-06 17:00:14Z
Name            :  
Last Login Date : 2010-11-20 21:48:12Z
Pwd Reset Date  : 2010-11-20 21:56:34Z
Pwd Fail Date   : Never
Login Count     : 6
Embedded RID    : 500
  --> Password does not expire
  --> Account Disabled
  --> Normal user account

Username        : Guest [501]
Full Name       : 
User Comment    : Built-in account for guest access to the computer/domain
Account Type    : Default Guest Acct
Account Created : 2020-06-06 17:00:14Z
Name            :  
Last Login Date : Never
Pwd Reset Date  : Never
Pwd Fail Date   : Never
Login Count     : 0
Embedded RID    : 501
  --> Password does not expire
  --> Account Disabled
  --> Password not required
  --> Normal user account

Username        : John [1000]
Full Name       : 
User Comment    : 
Account Type    : Default Admin User
Account Created : 2020-06-06 08:00:25Z
Name            :  
Last Login Date : 2020-06-09 09:28:38Z
Pwd Reset Date  : 2020-06-06 08:00:25Z
Pwd Fail Date   : Never
Login Count     : 5
Embedded RID    : 1000
  --> Password does not expire
  --> Password not required
  --> Normal user account

Username        : mark [1001]
Full Name       : mark
User Comment    : 
Account Type    : Custom Limited Acct
Account Created : 2020-06-06 08:15:42Z
Name            :  
Last Login Date : Never
Pwd Reset Date  : Never
Pwd Fail Date   : Never
Login Count     : 0
Embedded RID    : 1001
  --> Password does not expire
  --> Normal user account

Username        : Adam [1002]
Full Name       : Adam
User Comment    : 
Account Type    : Custom Limited Acct
Account Created : 2020-06-06 08:16:19Z
Name            :  
Last Login Date : Never
Pwd Reset Date  : Never
Pwd Fail Date   : Never
Login Count     : 0
Embedded RID    : 1002
  --> Password does not expire
  --> Normal user account

-------------------------
Group Membership Information
-------------------------
Group Name    : Users [4]
LastWrite     : 2020-06-06 08:16:19Z
Group Comment : Users are prevented from making accidental or intentional system-wide changes and can run most applications
Users :
  S-1-5-21-792323161-214100996-3742390483-1001
  S-1-5-4
  S-1-5-11
  S-1-5-21-792323161-214100996-3742390483-1002

Group Name    : Event Log Readers [0]
LastWrite     : 2009-07-14 04:34:12Z
Group Comment : Members of this group can read event logs from local machine
Users         : None

Group Name    : Guests [1]
LastWrite     : 2020-06-06 16:58:02Z
Group Comment : Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted
Users :
  S-1-5-21-792323161-214100996-3742390483-501

Group Name    : Distributed COM Users [0]
LastWrite     : 2009-07-14 04:34:12Z
Group Comment : Members are allowed to launch, activate and use Distributed COM objects on this machine.
Users         : None

Group Name    : Administrators [2]
LastWrite     : 2020-06-06 08:00:25Z
Group Comment : Administrators have complete and unrestricted access to the computer/domain
Users :
  S-1-5-21-792323161-214100996-3742390483-1000
  S-1-5-21-792323161-214100996-3742390483-500

Group Name    : Network Configuration Operators [0]
LastWrite     : 2020-06-06 16:58:10Z
Group Comment : Members in this group can have some administrative privileges to manage configuration of networking features
Users         : None

Group Name    : Cryptographic Operators [0]
LastWrite     : 2020-06-06 16:58:10Z
Group Comment : Members are authorized to perform cryptographic operations.
Users         : None

Group Name    : Power Users [0]
LastWrite     : 2020-06-06 16:58:10Z
Group Comment : Power Users are included for backwards compatibility and possess limited administrative powers
Users         : None

Group Name    : Performance Log Users [0]
LastWrite     : 2009-07-14 04:34:12Z
Group Comment : Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer
Users         : None

Group Name    : Replicator [0]
LastWrite     : 2020-06-06 16:58:10Z
Group Comment : Supports file replication in a domain
Users         : None

Group Name    : Performance Monitor Users [0]
LastWrite     : 2009-07-14 04:34:12Z
Group Comment : Members of this group can access performance counter data locally and remotely
Users         : None

Group Name    : Remote Desktop Users [0]
LastWrite     : 2020-06-06 16:58:10Z
Group Comment : Members in this group are granted the right to logon remotely
Users         : None

Group Name    : IIS_IUSRS [1]
LastWrite     : 2009-07-14 04:34:12Z
Group Comment : Built-in group used by Internet Information Services.
Users :
  S-1-5-17

Group Name    : Backup Operators [0]
LastWrite     : 2020-06-06 16:58:10Z
Group Comment : Backup Operators can override security restrictions for the sole purpose of backing up or restoring files
Users         : None

Analysis Tips:
 - For well-known SIDs, see http://support.microsoft.com/kb/243330
     - S-1-5-4  = Interactive
     - S-1-5-11 = Authenticated Users
 - Correlate the user SIDs to the output of the ProfileList plugin
``` 

We found details for our user John 

``` 
Username        : John [1000]
Full Name       : 
User Comment    : 
Account Type    : Default Admin User
Account Created : 2020-06-06 08:00:25Z
Name            :  
Last Login Date : 2020-06-09 09:28:38Z
Pwd Reset Date  : 2020-06-06 08:00:25Z
Pwd Fail Date   : Never
Login Count     : 5
Embedded RID    : 1000
  --> Password does not expire
  --> Password not required
  --> Normal user account
``` 
The password reset date is ```Pwd Reset Date  : 2020-06-06 08:00:25Z```  

Flag format:  MD5 of YY:MM:DD like 1998-05-15

Md5(2020-06-06) = faf07eb160d2046a12d41230d463e4ca


## Flag

```
faf07eb160d2046a12d41230d463e4ca
```
