#!/home/anaconda3/bin/python3
import json
from logging import addLevelName
from eth_utils import address
from web3 import Web3, contract

infura_url = "https://mainnet.infura.io/v3/0cb275803b764f1bb2af700fce70aa8d"
web3 = Web3(Web3.HTTPProvider(infura_url))
conexion = web3.isConnected()

if conexion:
    #leer el ultimo bloque de Ethereum
    num_bloque = web3.eth.blockNumber
    print("Estoy en el bloque: {} de Ethereum".format(num_bloque))
  
def leer_saldo_wallet():
    saldo=web3.eth.get_balance("0xcde51ab01d803c4261c0D8016cbab5656194E366")
    # Pasar el saldo expresado en Wei a Ether:
    wei_to_eth= web3.fromWei(saldo,"ether")
    print ("El saldo de mi Wallet es: {}".format(wei_to_eth))
    return wei_to_eth

leer_saldo_wallet()

#Conectarse y leer un Smart Contract de un tercero
abi =json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_tokenContract","type":"address"}],"name":"withdrawAltcoinTokens","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"burn","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_participant","type":"address"},{"name":"_amount","type":"uint256"}],"name":"adminClaimAirdrop","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_addresses","type":"address[]"},{"name":"_amount","type":"uint256"}],"name":"adminClaimAirdropMultiple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"finishDistribution","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_tokensPerEth","type":"uint256"}],"name":"updateTokensPerEth","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"getTokens","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"minContribution","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"distributionFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenAddress","type":"address"},{"name":"who","type":"address"}],"name":"getTokenBalance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"tokensPerEth","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalDistributed","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"amount","type":"uint256"}],"name":"Distr","type":"event"},{"anonymous":false,"inputs":[],"name":"DistrFinished","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"},{"indexed":false,"name":"_balance","type":"uint256"}],"name":"Airdrop","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_tokensPerEth","type":"uint256"}],"name":"TokensPerEthUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"burner","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"}]' )
address=Web3.toChecksumAddress("0xeab7b16ad4c5b6553d4bf42532da37516ab4bec5")
contract=web3.eth.contract(address=address,abi=abi)

#print(contract)

total_Supply= contract.functions.totalSupply().call()
print("Leyendo el Smart Contract de: {}".format(contract.functions.name().call()))
print("Total Supply es: {} ".format(web3.fromWei(total_Supply,"ether")))
print("Simbolo: {}".format(contract.functions.symbol().call()))
saldo_del_holder = contract.functions.balanceOf(Web3.toChecksumAddress("0xae4da76877c9edcaf4f5a76ef3e5c3a63248f591")).call()
print("Holder tiene: {} ".format(web3.fromWei(saldo_del_holder,"ether")))
