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
