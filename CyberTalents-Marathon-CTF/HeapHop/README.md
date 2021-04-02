
# Challenge Name: HeapHop



![date](https://img.shields.io/badge/date-24.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Hard-blue.svg)
![score](https://img.shields.io/badge/score-200-blue.svg)


## Attached files

- [HeapHop56348583746.tar.7z](https://hubchallenges.s3-eu-west-1.amazonaws.com/Forensics/HeapHop56348583746.tar.7z) https://hubchallenges.s3-eu-west-1.amazonaws.com/Forensics/HeapHop56348583746.tar.7z  

## Detailed solution  

The description : the first 3 bytes from heaps

We start by extract the HeapHop56348583746.tar.7z and after the chall.tar. We found chall.vmem, it's a VMEM file.  

Virtual Memory or VMEM is a file extension used by virtualization software like VMware, Virtualbox, etc. VMEM files generally store RAM or Physical Memory of the related virtual machine.  

I'll use the tool volatility to interact with virtual memory file https://github.com/volatilityfoundation/volatility  

Starting by identify the image using the plugin imageinfo 
  
``` 
volatility_2.6_win64_standalone.exe -f chall.vmem imageinfo
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (C:\Users\maros\Desktop\Marouane\CTF\tools\volatility_2.6_win64_standalone\chall.vmem)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf80002a0f0a0L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002a10d00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2021-03-11 14:03:26 UTC+0000
     Image local date and time : 2021-03-11 16:03:26 +0200
```  

Let's perform a filescan and use the profil Win7SP1x64  
  
``` 
volatility_2.6_win64_standalone.exe -f chall.vmem --profil=Win7SP1x64 filescan --output-file=vmem-files.txt
``` 
  
We found a file that has the challenge name 
  
``` 
Offset(P)            #Ptr   #Hnd Access Name
0x0000000006ff0f20      3      1 ------ \Device\HarddiskVolume1\Users\labib\Desktop\heapshop.exe
``` 
Let's check the runing processes using pslist 

``` 
volatility_2.6_win64_standalone.exe -f chall.vmem --profil=Win7SP1x64 pslist --output-file=vmem-ps.txt
``` 

We found the heapshop executable running 
  
```
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit                          
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xfffffa800173e460 heapshop.exe           1580   1204      1       24      1      1 2021-03-11 14:03:20 UTC+0000
```  

i'll use the plugin vadtree to see the heap structure  

```
volatility_2.6_win64_standalone.exe -f chall.vmem --profil=Win7SP1x64 vadtree --output=dot --output-file=graph.dot -p 1580
``` 
We need to see the dot graph, i'll use https://dreampuf.github.io/GraphvizOnline/ 
  
![image](https://user-images.githubusercontent.com/72421091/113368859-a7b49680-9357-11eb-828e-6bae794eb9bc.png)  

The graph highlights heaps with red color  

Let's dump the whole VAD strcture with the plugin vaddump  

``` 
volatility_2.6_win64_standalone.exe -f chall.vmem --profil=Win7SP1x64 vaddump -p 1580 -D heapshop  

Volatility Foundation Volatility Framework 2.6
Pid        Process              Start              End                Result
---------- -------------------- ------------------ ------------------ ------
      1580 heapshop.exe         0x00000000750a0000 0x00000000750a7fff heapshop\heapshop.exe.eb3e460.0x00000000750a0000-0x00000000750a7fff.dmp
      1580 heapshop.exe         0x0000000000400000 0x00000000004dafff heapshop\heapshop.exe.eb3e460.0x0000000000400000-0x00000000004dafff.dmp
      1580 heapshop.exe         0x0000000000290000 0x0000000000293fff heapshop\heapshop.exe.eb3e460.0x0000000000290000-0x0000000000293fff.dmp
      1580 heapshop.exe         0x0000000000050000 0x000000000008ffff heapshop\heapshop.exe.eb3e460.0x0000000000050000-0x000000000008ffff.dmp
      1580 heapshop.exe         0x0000000000020000 0x000000000002ffff heapshop\heapshop.exe.eb3e460.0x0000000000020000-0x000000000002ffff.dmp
      1580 heapshop.exe         0x0000000000010000 0x000000000001ffff heapshop\heapshop.exe.eb3e460.0x0000000000010000-0x000000000001ffff.dmp
      1580 heapshop.exe         0x0000000000040000 0x0000000000040fff heapshop\heapshop.exe.eb3e460.0x0000000000040000-0x0000000000040fff.dmp
      1580 heapshop.exe         0x0000000000090000 0x000000000028ffff heapshop\heapshop.exe.eb3e460.0x0000000000090000-0x000000000028ffff.dmp
      1580 heapshop.exe         0x00000000002e0000 0x000000000035ffff heapshop\heapshop.exe.eb3e460.0x00000000002e0000-0x000000000035ffff.dmp
      1580 heapshop.exe         0x00000000002a0000 0x00000000002a0fff heapshop\heapshop.exe.eb3e460.0x00000000002a0000-0x00000000002a0fff.dmp
      1580 heapshop.exe         0x00000000002b0000 0x00000000002cffff heapshop\heapshop.exe.eb3e460.0x00000000002b0000-0x00000000002cffff.dmp
      1580 heapshop.exe         0x0000000000360000 0x00000000003c6fff heapshop\heapshop.exe.eb3e460.0x0000000000360000-0x00000000003c6fff.dmp
      1580 heapshop.exe         0x0000000000800000 0x000000000080ffff heapshop\heapshop.exe.eb3e460.0x0000000000800000-0x000000000080ffff.dmp
      1580 heapshop.exe         0x0000000000610000 0x000000000070ffff heapshop\heapshop.exe.eb3e460.0x0000000000610000-0x000000000070ffff.dmp
      1580 heapshop.exe         0x0000000000510000 0x000000000060ffff heapshop\heapshop.exe.eb3e460.0x0000000000510000-0x000000000060ffff.dmp
      1580 heapshop.exe         0x0000000074da0000 0x0000000074dfbfff heapshop\heapshop.exe.eb3e460.0x0000000074da0000-0x0000000074dfbfff.dmp
      1580 heapshop.exe         0x0000000074d50000 0x0000000074d9bfff heapshop\heapshop.exe.eb3e460.0x0000000074d50000-0x0000000074d9bfff.dmp
      1580 heapshop.exe         0x0000000074e00000 0x0000000074e3efff heapshop\heapshop.exe.eb3e460.0x0000000074e00000-0x0000000074e3efff.dmp
      1580 heapshop.exe         0x000000007efb0000 0x000000007efd2fff heapshop\heapshop.exe.eb3e460.0x000000007efb0000-0x000000007efd2fff.dmp
      1580 heapshop.exe         0x0000000077190000 0x00000000772aefff heapshop\heapshop.exe.eb3e460.0x0000000077190000-0x00000000772aefff.dmp
      1580 heapshop.exe         0x00000000768a0000 0x000000007694bfff heapshop\heapshop.exe.eb3e460.0x00000000768a0000-0x000000007694bfff.dmp
      1580 heapshop.exe         0x0000000075160000 0x00000000751a5fff heapshop\heapshop.exe.eb3e460.0x0000000075160000-0x00000000751a5fff.dmp
      1580 heapshop.exe         0x0000000077080000 0x000000007718ffff heapshop\heapshop.exe.eb3e460.0x0000000077080000-0x000000007718ffff.dmp
      1580 heapshop.exe         0x00000000773b0000 0x0000000077558fff heapshop\heapshop.exe.eb3e460.0x00000000773b0000-0x0000000077558fff.dmp
      1580 heapshop.exe         0x00000000772b0000 0x00000000773a9fff heapshop\heapshop.exe.eb3e460.0x00000000772b0000-0x00000000773a9fff.dmp
      1580 heapshop.exe         0x0000000077590000 0x000000007770ffff heapshop\heapshop.exe.eb3e460.0x0000000077590000-0x000000007770ffff.dmp
      1580 heapshop.exe         0x000000007f0e0000 0x000000007ffdffff heapshop\heapshop.exe.eb3e460.0x000000007f0e0000-0x000000007ffdffff.dmp
      1580 heapshop.exe         0x000000007efde000 0x000000007efdefff heapshop\heapshop.exe.eb3e460.0x000000007efde000-0x000000007efdefff.dmp
      1580 heapshop.exe         0x000000007efdb000 0x000000007efddfff heapshop\heapshop.exe.eb3e460.0x000000007efdb000-0x000000007efddfff.dmp
      1580 heapshop.exe         0x000000007efdf000 0x000000007efdffff heapshop\heapshop.exe.eb3e460.0x000000007efdf000-0x000000007efdffff.dmp
      1580 heapshop.exe         0x000000007efe0000 0x000000007f0dffff heapshop\heapshop.exe.eb3e460.0x000000007efe0000-0x000000007f0dffff.dmp
      1580 heapshop.exe         0x000000007ffe0000 0x000000007ffeffff heapshop\heapshop.exe.eb3e460.0x000000007ffe0000-0x000000007ffeffff.dmp
```  

As the challenge description mention, we need to extract the first 3 bytes from heaps to get our flag

```
xxd -a heapshop.exe.eb3e460.0x000000007efde000-0x000000007efdefff.dmp | less  
00000000: 735f 6100 ffff ffff 0000 4000 0002 6977  s_a.......@...iw
```  
```  
xxd -a heapshop.exe.eb3e460.0x000000007efdb000-0x000000007efddfff.dmp | less  
00000000: 5265 5f7e 0000 0000 20fd 0800 0000 0000  Re_~.... .......
```  
```
xxd -a heapshop.exe.eb3e460.0x0000000000800000-0x000000000080ffff.dmp | less   
00000000: 616e 74d1 45f5 0001 eeff eeff 0000 0000  ant.E...........  
```  
```  
xxd -a heapshop.exe.eb3e460.0x0000000000610000-0x000000000070ffff.dmp | less   
00000000: 5f56 6168 45f5 0101 eeff eeff 0000 0000  _VahE...........    
```  
```  
xxd -a heapshop.exe.eb3e460.0x0000000000510000-0x000000000060ffff.dmp | less  
00000000: 6473 7daa 3e75 0001 eeff eeff 0000 0000  ds}.>u..........  
```  
```  
xxd -a heapshop.exe.eb3e460.0x00000000002e0000-0x000000000035ffff.dmp | less  
00000000: 6631 3400 0000 0000 7354 1cb3 3e75 0001  f14.....sT..>u..  
```  
```  
xxd -a heapshop.exe.eb3e460.0x00000000002a0000-0x00000000002a0fff.dmp | less  
00000000: 696d 7000 0000 0000 0100 0000 0000 0000  imp.............  
```  
```  
xxd -a heapshop.exe.eb3e460.0x00000000002b0000-0x00000000002cffff.dmp | less  
00000000: 3072 7400 e83f 5100 0100 0000 2041 5100  0rt..?Q..... AQ.  
```  
```  
xxd -a heapshop.exe.eb3e460.0x0000000000020000-0x000000000002ffff.dmp | less  
00000000: 6534 7000 0000 0000 ecb0 bae2 969d 0001  e4p.............  
```  
```  
xxd -a heapshop.exe.eb3e460.0x0000000000010000-0x000000000001ffff.dmp | less  
00000000: 397b 6800 0000 0000 77c0 77c4 78f8 0001  9{h.....w.w.x...
```  

We can combine the first 3 bytes from each heap and put it in order to get the flag format flag{}  

``` 
0x000000007efde000-0x000000007efdefff -> s_a  
0x000000007efdb000-0x000000007efddfff -> Re_  
0x0000000000800000-0x000000000080ffff -> ant  
0x0000000000610000-0x000000000070ffff -> _Vah  
0x0000000000510000-0x000000000060ffff -> ds}  
0x00000000002e0000-0x000000000035ffff -> f14  
0x00000000002a0000-0x00000000002a0fff.dmp -> imp  
0x00000000002b0000-0x00000000002cffff.dmp -> 0rt  
0x0000000000020000-0x000000000002ffff.dmp -> e4p   
0x0000000000010000-0x000000000001ffff.dmp -> 9{h  
``` 


## Flag

```
f149{he4ps_aRe_imp0rtant_Vads}
```
