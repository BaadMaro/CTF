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

#flag with key 12 => flag{surround_this_flag_with_flag_format}


                
            

