from blockchain import Blockchain

def printHeader(msg):
    print()
    print("="*80)
    print (msg)
    print("="*80)
    print()
    

def cadena_valida(cadena):
    return "la Cadena es Valida :)!" if cadena.validar_chain() else "la Cadena NO es valida :'("

block_one_transactions = {"emisor":"Alicia", "receptor": "Juan", "cantidad":"34"}
block_two_transactions = {"emisor": "Juan", "receptor":"Pedro", "cantidad":"56"}
block_three_transactions = {"emisor":"Alicia", "receptor":"Pedro", "cantidad":"25"}


mi_blockchain = Blockchain()

printHeader ("Bloque origen")
mi_blockchain.imprimir_bloques()

printHeader ("agregando 3 transacciones")
mi_blockchain.adjuntar_bloque(block_one_transactions)
mi_blockchain.adjuntar_bloque(block_two_transactions)
mi_blockchain.adjuntar_bloque(block_three_transactions)
mi_blockchain.imprimir_bloques()
print (cadena_valida(mi_blockchain))

printHeader ("agregando un bloque invalido")




# transaccion falsa
transaccion_falsa = {"emisor": "Juan", "receptor":"Pedro, Alicia", "cantidad":"10"}
mi_blockchain.chain[2].transacciones = transaccion_falsa

mi_blockchain.imprimir_bloques()
print (cadena_valida(mi_blockchain))
