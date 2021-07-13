# Challenge Name: scissor

![date](https://img.shields.io/badge/date-09.07.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Crypto-blueviolet.svg)   
![value](https://img.shields.io/badge/value-102-blue.svg)  


## Description

I was given this string and told something about scissors.

egddagzp_ftue_rxms_iuft_rxms_radymf

Author : BrownieInMotion

[encrypt.py](encrypt.py)


## Detailed solution

Start by analyzing the encrypt code 

```python
import random

key = random.randint(0, 25)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shifted = alphabet[key:] + alphabet[:key]
dictionary = dict(zip(alphabet, shifted))

print(''.join([
    dictionary[c]
    if c in dictionary
    else c
    for c in input()
]))
```
- A random key from 0 to 25 is genereted
- The key is used to shift alphabet
- zip function used to pair each element of alphabet and shifted varaiables together https://www.w3schools.com/python/ref_func_zip.asp
- a dictionary (associative array) has been created from the output of zip function https://realpython.com/python-dicts/
- An input is been used, we can see a loop with the input caracteres, a test is performed to check if the caractere is in the dicionary or not 
- Finally we have the output in the challenge description ```egddagzp_ftue_rxms_iuft_rxms_radymf```

To be able to decrypt the output we need to :
- Find the used key (0,25)
- Loop with each caractere from the output and try to find the reversed caracter using the same performed test
- Save the matching caracteres and print all the keys from 0 to 25 

Here is the solve code [crypto-scissor.py](crypto-scissor.py)

```python
import string

flag = ''
solve = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
output = 'egddagzp_ftue_rxms_iuft_rxms_radymf'

for i in range(0,26):    
    shifted = alphabet[i:] + alphabet[:i]
    dictionary = dict(zip(alphabet, shifted))
    for j in range(len(output)):
        for c in string.printable:
            solve = ''.join([
                dictionary[c]
                if c in dictionary
                else c                
            ])
            
            if solve == output[j]:
                flag += c
    print(str(i) + " => " + flag)
    flag = ""
```

Output 
```
0 => egddagzp_ftue_rxms_iuft_rxms_radymf
1 => dfcczfyo_estd_qwlr_htes_qwlr_qzcxle
2 => cebbyexn_drsc_pvkq_gsdr_pvkq_pybwkd
3 => bdaaxdwm_cqrb_oujp_frcq_oujp_oxavjc
4 => aczzwcvl_bpqa_ntio_eqbp_ntio_nwzuib
5 => zbyyvbuk_aopz_mshn_dpao_mshn_mvytha
6 => yaxxuatj_znoy_lrgm_cozn_lrgm_luxsgz
7 => xzwwtzsi_ymnx_kqfl_bnym_kqfl_ktwrfy
8 => wyvvsyrh_xlmw_jpek_amxl_jpek_jsvqex
9 => vxuurxqg_wklv_iodj_zlwk_iodj_irupdw
10 => uwttqwpf_vjku_hnci_ykvj_hnci_hqtocv
11 => tvsspvoe_uijt_gmbh_xjui_gmbh_gpsnbu
12 => surround_this_flag_with_flag_format
13 => rtqqntmc_sghr_ekzf_vhsg_ekzf_enqlzs
14 => qsppmslb_rfgq_djye_ugrf_djye_dmpkyr
15 => proolrka_qefp_cixd_tfqe_cixd_clojxq
16 => oqnnkqjz_pdeo_bhwc_sepd_bhwc_bkniwp
17 => npmmjpiy_ocdn_agvb_rdoc_agvb_ajmhvo
18 => molliohx_nbcm_zfua_qcnb_zfua_zilgun
19 => lnkkhngw_mabl_yetz_pbma_yetz_yhkftm
20 => kmjjgmfv_lzak_xdsy_oalz_xdsy_xgjesl
21 => jliifleu_kyzj_wcrx_nzky_wcrx_wfidrk
22 => ikhhekdt_jxyi_vbqw_myjx_vbqw_vehcqj
23 => hjggdjcs_iwxh_uapv_lxiw_uapv_udgbpi
24 => giffcibr_hvwg_tzou_kwhv_tzou_tcfaoh
25 => fheebhaq_guvf_synt_jvgu_synt_sbezng
```

We can see our flag with key 12 ```surround_this_flag_with_flag_format```  

## Flag

```
flag{surround_this_flag_with_flag_format}
```
