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