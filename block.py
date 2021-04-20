from datetime import datetime
from hashlib import sha256


class Block:
    def __init__(self, transacciones, hash_previo, nonce = 0):
        self.timestamp = datetime.now()
        self.transacciones = transacciones
        self.hash_previo = hash_previo
        self.nonce = nonce
        self.hash = self.generate_hash()

    def __str__(self):
        # prints block contents
        return ("timestamp:{}\n" + \
               "transacciones:{}\n" + \
               "hash actual:{}\n").format(self.timestamp, self.transacciones,  self.hash)


    def generate_hash(self):
        contenido_bloque = str(self.timestamp)+str(self.transacciones)+str(self.nonce)+str(self.hash_previo)
        block_hash = sha256(contenido_bloque.encode())
        return block_hash.hexdigest()
        

if __name__ == "__main__":

    print(Block({},0))