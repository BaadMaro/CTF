# Challenge Name: Stolen funds


![date](https://img.shields.io/badge/date-06.03.2022-brightgreen.svg)  
![solved](https://img.shields.io/badge/solved-after%20CTF-red.svg)  
![category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![value](https://img.shields.io/badge/value-40-blue.svg)  

## Description

Created By **sicmundos**

A hacker has **withdrawn** funds from our contract, he might have left some traces while doing that, can you help us find out his identity?

> **_Address_** : 0x20402a4F943786DdF55D4Ffaf09EEe6752e820e2

> **_Network_** : Rinkeby


## Detailed solution

We can start by using Rinkeby Testnet Explorer to get more details about the adress 

https://rinkeby.etherscan.io/address/0x20402a4F943786DdF55D4Ffaf09EEe6752e820e2

The contract was created by the adress 0x64bCf8EF116c2f3A39e3526bcF7400828563a6ed

We can start checking the transactions https://rinkeby.etherscan.io/txs?a=0x20402a4F943786DdF55D4Ffaf09EEe6752e820e2

We need to focus the withdraw events, i exported all transactions in a csv file https://rinkeby.etherscan.io/exportData?type=address&a=0x20402a4F943786DdF55D4Ffaf09EEe6752e820e2

We can use a filter with the clomun "Methode" to list only ithdraw 

The first withdraw transaction 0x0f17146850f45e45b660997a5e417793faa8a3a47ecdfdbcd1b3fe70fbdd69a6

https://rinkeby.etherscan.io/tx/0x0f17146850f45e45b660997a5e417793faa8a3a47ecdfdbcd1b3fe70fbdd69a6

If we decode the input data, we can see a ascii charactere "C"

![image](https://user-images.githubusercontent.com/72421091/158233484-9bd39fc2-0d78-4519-aa00-2e66e29a4f87.png)

Checking the second one 0xe3d91cdf7ecec6b0b4ce05dbd17340e3bff48dac8475ea90ea700bb87bbdc509 

https://rinkeby.etherscan.io/tx/0xe3d91cdf7ecec6b0b4ce05dbd17340e3bff48dac8475ea90ea700bb87bbdc509  

![image](https://user-images.githubusercontent.com/72421091/158233750-8a96f05b-93f9-4b17-9af4-6599fef8a3e9.png)

If we decode the input data, we can see a ascii charactere "R"

We rt recognizing the flag formt CRISIS. Now we need to grap all characteres manually or create a script 

Script details :
- I'll use the python library [Web3] ( https://web3py.readthedocs.io/en/stable/index.html) to connect to rinkeby network and extract transactions details  
- To be able to interact with the rinkeby network we need to create a project in infora.io and use the project ID
https://web3py.readthedocs.io/en/stable/examples.html#using-infura-rinkeby-node
- For the list of withdraw transactions i'll use the exported csv to simplify the process
- I was able to locate our input flag characteres to simplify the decoding 

```bash
w3.eth.get_transaction('0xfc1da29d326e459b309d091827e906e46787805438389749e9f30dd452b934cd')
AttributeDict({'accessList': [], 'blockHash': HexBytes('0x9ae06bee8782f4133e853566f7c29fe9b4c6a17458947950adde502f995a7c27'), 'block                             Number': 10259148, 'chainId': '0x4', 'from': '0x64bCf8EF116c2f3A39e3526bcF7400828563a6ed', 'gas': 30657, 'gasPrice': 1150001602, 'ha                             sh': HexBytes('0xfc1da29d326e459b309d091827e906e46787805438389749e9f30dd452b934cd'), 'input': '0x31fb67c2000000000000000000000000000                             000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000017d00000000000000000000000000000                             000000000000000000000000000000000', 'maxFeePerGas': 1150001667, 'maxPriorityFeePerGas': 1150001354, 'nonce': 325, 'r': HexBytes('0xc                             3150ab969e202e56d98791bff0ede61dfc8712c45a40dc577d80899b3708c9a'), 's': HexBytes('0x1d6cf1e880244a8a9c2902fc190d3621ab42d2ec039f80c3                             b3df95f8d62611f3'), 'to': '0x20402a4F943786DdF55D4Ffaf09EEe6752e820e2', 'transactionIndex': 41, 'type': '0x2', 'v': 0, 'value': 0})

>>> tx['input'][138:140]
'7d'
>>> chr(0x7d)
'}'
```

Here is the solution

```python
from web3 import Web3, HTTPProvider
import csv

w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/YOUR_PROJECT_ID"))

tx_hashes = []
flag = ""

with open('1.csv', 'r') as export:
    reader = csv.reader(export, delimiter=',')
    for row in reader:
      if row[15] == 'Withdraw':
          tx_hashes.append(row[0])
print(tx_hashes)

for i in tx_hashes:
    tx = w3.eth.get_transaction(i)
    flag += bytes.fromhex(tx['input'][138:140]).decode("ASCII")

print(flag)
```
Output

```
['0x0f17146850f45e45b660997a5e417793faa8a3a47ecdfdbcd1b3fe70fbdd69a6', '0xe3d91cdf7ecec6b0b4ce05dbd17340e3bff48dac8475ea90ea700bb87bbdc509', '0xbfdcef945991ed5be60462897cc4acf1b308f36cc21b6bb232111ad2ab74d0b9', '0x21740d31d66c44dc7cf1d4d75a709f28221af0fbd8c0f03ccae1996447f939de', '0x026772ba9b81f8b6e9cffec45bb680d3b6d52f325b56946b46db04b594ab25f6', '0x9a19b2701d897b77003a796e04ef2df207cf1dbba210f255deb522fab301baf7', '0x5f895ed8211daec43c00ef43ffa0510e6720e232b6817a36423b70bcda7327f1', '0x5e07073f55b5b9e79c0a4e1ef1a25db1f292c2b134759ccf8bc96e3fba44ead4', '0xab5cb5efb27b8ea4d5a110dcbc79527da407e2fcdee07ab8c2ef351d83e042f0', '0xfd6bf266c2a50c2395a8f361d5d604827455329b7eb32f50189c86a9c558c4aa', '0x6b4ee19ec07fbb3e4720336e883aa536e983d67865e2023cbda1af5a2a3d53c1', '0x840f16230bfa528eaa8b2cc3de9af51629a9a84455eac50c736d47e8e099d6c4', '0x77abb9fc5e6cb5db818b644512bca6c28a8ac7afcc8a3f2f67e8daf001eaa9f9', '0x4fe8c7ebdde60fd50c142ca65bbe1ede68b31e156cbc521f860643335ab2ec22', '0x2c2f77fd00c634d87c7bdfabbb6ac84ccee91f89228223d5f36dd827fa882646', '0x7cd72022b08ef8e63d8bffa2a7177b77e06f173ac1857ee3d222dc4d4b78225c', '0xb23b05ec9e2d39653aadb46a6809bc893e00778643c7d5b621a6fe964b96bbdc', '0x6d27bc6ccfbed5ff0dd7bdfd0fdd53e4365c74d64f2b791d29f80d6e0c449a1e', '0x18583053e65b6feee4e7dcef31a66f825041529a700649989a7344a9963bb42d', '0x66471df50fb713812a3e7e3631cb1abeb02fbecab9dc73d3fcaa69c8c43a66b7', '0x9f4d672dea9cc6d3df6c76a7fde2560e079c1832345aebbc88cd0b2458ce34d3', '0xbd02969404f97abcadf1f94795252509df1c15d4fda78ad509accf9a6e614e2f', '0xf91fc233c54ffa476ed0cfd76b29eba9aacfe444877950fe0750710423914682', '0xfc1da29d326e459b309d091827e906e46787805438389749e9f30dd452b934cd']
CRISIS{xtZ254KFhVeu3NnY}
```

## Flag

```
CRISIS{xtZ254KFhVeu3NnY}
```





