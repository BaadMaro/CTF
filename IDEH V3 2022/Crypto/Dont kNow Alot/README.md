# Challenge Name: Dont kNow Alot


![date](https://img.shields.io/badge/date-10.03.2022-brightgreen.svg)  
![solved after CTF](https://img.shields.io/badge/solved-after%20CTF-red.svg)  
![category](https://img.shields.io/badge/category-Crypto-blueviolet.svg)   
![value](https://img.shields.io/badge/value-20-blue.svg) 


## Description

Created By **sicmundos**

The laws of genetics apply even if you refused to learn them.

[Download Attachement](https://s3.eu-west-3.amazonaws.com/crisis-assets/crisis_attachements/TThNoXHghAOSVmldSEgU6v9ElaMHx9ZOjQVQtLlu.zip)

## Detailed solution

We have two hint from challenge name and description
- three uppercase characteres in challenge name => DNA
- description => genetics 

So the challenge is about dna code but not the real usage of it it's only a cipher used for crypto challenges   

If you want to see a real challenge here is a link for a writeup i made about identifying an Enzyme using DNA sequence 

- https://github.com/BaadMaro/CTF/tree/main/X-MAS%20CTF%202021%20Second%20Weekend/Having%20a%20BLAST

There is two mapping table to convert from binary to english letters 

![image](https://user-images.githubusercontent.com/72421091/157745384-2e63df82-c6c0-4a23-bae6-f1db3dfaf36e.png)

![image](https://user-images.githubusercontent.com/72421091/157745399-c96698b5-7edc-4f27-a379-2f3a75d3bbb1.png)

Now we need to create a script to convert binary to dna letters and from dna letters to english letters

We can clean { } _ from the flag.txt file and add them later to the flag  

```python
#cipher without "{}_"
cipher = "101100010111010001011100010001011100011110001011001000000011001110000000000001001101000011001000"
#cipher parts
c0 = "101100010111010001011100010001011100"
c1 = "011110001011001000"
c2 = "000011001110000000"
c3 = "000001001101000011001000"

def binaryseq(seq):
    # binary values to nucleotide sequence
    table1 = {'00':'A','10':'C','01':'G','11':'T'}
    f1 = ""
    if len(seq)%2==0:
        for i in range(0,len(seq),2):
            f1+=table1[seq[i:i+2]]
        return f1

def translate(seq):
    table2 = {
        'AAA':'a','AAC':'b','AAG':'c','AAT':'d',
        'ACA':'e','ACC':'f', 'ACG':'g','ACT':'h',
        'AGA':'i','AGC':'j','AGG':'k','AGT':'l',
        'ATA':'m','ATC':'n','ATG':'o','ATT':'p',
        'CAA':'q','CAC':'r','CAG':'s','CAT':'t',
        'CCA':'u','CCC':'v','CCG':'w','CCT':'x',
        'CGA':'y','CGC':'z','CGG':'A','CGT':'B',
        'CTA':'C','CTC':'D','CTG':'E','CTT':'F',
        'GAA':'G','GAC':'H','GAG':'I','GAT':'J',
        'GCA':'K','GCC':'L','GCG':'M','GCT':'N',
        'GGA':'O','GGC':'P','GGG':'Q','GGT':'R',
        'GTA':'S','GTC':'T','GTG':'U','GTT':'V',
        'TAA':'W','TAC':'X','TAG':'Y','TAT':'Z',
        'TCA':'1','TCC':'2','TCG':'3','TCT':'4',
        'TGA':'5','TGC':'6','TGG':'7','TGT':'8',
        'TTA':'9','TTC':'0','TTG':' ','TTT':'.'
        }
    f2 = ""
    if len(seq)%3==0:
        for i in range(0,len(seq),3):
            f2+=table2[seq[i:i+3]]
        return f2


print(translate(binaryseq(cipher)))
print(translate(binaryseq(c0)) + "{" + translate(binaryseq(c1)) + "_" + translate(binaryseq(c2)) + "_" + translate(binaryseq(c3)) + "}")

```

We found our flag

```
CRISIS{The_dna_code}
```

