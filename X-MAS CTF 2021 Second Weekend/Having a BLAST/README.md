# Challenge Name: Having a BLAST

![date](https://img.shields.io/badge/date-18.12.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Bioinformatics-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  


## Description

Hi! We have just opened our first Lapland Bio Lab, where we are trying to build the toys of the future! (Ethics not included. We are thankfully not concerned about them, that's the Legal department's job!).

While scavenging through files, we have found this DNA sequence that contains a few exons from what the file says, a "homo sapiens gene that encodes the [REDACTED] enzyme". There is nothing more descriptive than that, huh. Can you find the enzyme encoded by this gene? We need this done by today. Thanks!

Attached DNA sequence:

```
CGCTTCCTCCCCAAATTGCTCAGCGCCACCGGTATGCAGGGGCCAGCGGGCAGCGGCTGGGAGGAGGGGAGTGGGAGCCCGCCAGGTGTAACCCCTCTCTTCTCCCCCTAGCCTCGGAGGCTCCCAGCACCTGCCCAGGCTTCACCCATGGGGAGGCTGCTCGGAGGCCCGGCCTCCCCCTGCCCCTCCTCCTCCTCCACCAGCTTCTCCTCCTCTTCCTCTCCCACCTCCGGCGGCTGTGAACACGGCCTCTTCCCCTACGGCCACAGGGGCCCCTCCTCTAATGAGTGGTCGGACCGTGGGGAAGGGCCCCACTCAGGGATCTCAGACCTAGTGCTCCCTTCCTCCTCAAACCGAGAGACTCACACTGGACAGGGCAGGAGGAGGGGGCCGTGCCTCCCACCCTTCTCAGGGACCCCCACGCCTTTGTTGTTTGAATGGAAATGGAAAAGCCAGTATTCTTTTTATAAAATTATCTTTTTGGAACCTGAGCCTGACATTGGGGGGAAGTGGGAGGCCGGACGGGTAGCACCCC
```

(The flag format is X-MAS{enzymename})

By: Milkdrop

## Detailed solution

The solution for the challenge is to use the DNA sequence to identify the enzyme
- First we need to convert the DNA sequence to Amino acid sequence
- Use a search database to identify the protein using Amino acid sequence

![image](https://user-images.githubusercontent.com/72421091/146805094-fe660c1f-c4d4-457e-a111-1512e4f28438.png)


To be able to convert the DNA sequence to Amino acid sequence we need to use a mapping table



The genetic code (referred as DNA codon table for DNA sequences) shows how we uniquely relate a 4-nucleotide sequence (A, T, G, C) to a set of 20 amino acids. It describes a set of rules by which information encoded within genetic material is translated into proteins by living cells. The diagram given below shows the DNA codon table in the form of a chart.

Each unique three character sequence of nucleotides, sometimes called a nucleotide triplet, corresponds to one amino acid. 

![image](https://user-images.githubusercontent.com/72421091/146806179-2aeec83c-e5af-410a-978c-4b543c8260ad.png)

Here is the mapping table 

```python
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
```

I'm gonna use a python script to translate the dna sequence to amino acide sequence by going 3 by 3

NB : the attached dna sequence has an addtional charactere at the end i don't know if it's correct or not. I'll just cut it form the sequence  

```python
# Read dna sequence
seq = open("dna.txt","r").read()[0:-1]

# Clear file
seq=seq.replace("\n","")
seq=seq.replace("\r","")

# Translate the DNA sequence to Amino acide sequence
def translate(seq):

    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    
    protein = ""
    if len(seq)%3==0:
        for i in range(0,len(seq),3):
            codon=seq[i:i+3]
            protein+=table[codon]
    return protein

print("Amino acide sequence :")
print(translate(seq))
```

Amino acide sequence :

```
RFLPKLLSATGMQGPAGSGWEEGSGSPPGVTPLFSP_PRRLPAPAQASPMGRLLGGPASPCPSSSSTSFSSSSSPTSGGCEHGLFPYGHRGPSSNEWSDRGEGPHSGISDLVLPSSSNRETHTGQGRRRGPCLPPFSGTPTPLLFEWKWKSQYSFYKIIFLEPEPDIGGKWEAGRVAP
```

To search for the protein using amino acid sequence i'll use https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins

BLASTP programs search protein databases using a protein query.

Use the Amino acide sequence as query and BLAST

![image](https://user-images.githubusercontent.com/72421091/146811102-3a86b2b6-edb1-4e06-bc6d-ac1e5cc78e31.png)

We have a 100% match, it's **acetylcholinesterase readthrough isoform [synthetic construct]**

![image](https://user-images.githubusercontent.com/72421091/146811462-3b34a418-44a7-4e80-ac07-6b15cbbdeeae.png)

Acetylcholinesterase (AChE) is a cholinergic enzyme primarily found at postsynaptic neuromuscular junctions, especially in muscles and nerves.
