from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transacciones_todas = []
        self.rootBlock()

    def rootBlock(self):
        transacciones = {}
        root = Block(transacciones, "0")
        self.chain.append(root)
        return self.chain

    # por si quieren imprimir el contenido del blockchain
    def imprimir_bloques(self):
        for i in range(len(self.chain)):
            bloque_actual = self.chain[i]
            print("Bloque {} \n{sep}\n{}{sep}\n".format(i, bloque_actual, sep = "-"*80))
            # bloque_actual.print_contents()

    # añadir bloque al blockchain
    def adjuntar_bloque(self, transacciones):
        bloque_hash_previo = self.chain[len(self.chain)-1].hash
        bloque_nuevo = Block(transacciones, bloque_hash_previo)
        proof = self.proof_of_work(bloque_nuevo)
        self.chain.append(bloque_nuevo)
        return proof, bloque_nuevo

    def validar_chain(self):
        for i in reversed(range(0, len(self.chain))):
            actual = self.chain[i]
            previo = self.chain[i-1]
            if(actual.hash != actual.generate_hash()):
                print("El hash actual es distinto al hash generado del bloque ({})".format(i))
                return False
            if(previo.hash != actual.hash_previo):
                print("El hash del bloque previo es distinto al valor del hash previo almacenado en el bloque actual({})".format(i))
                return False
        return True
    
    def proof_of_work(self, bloque, dificultad=2):
        proof = bloque.generate_hash()
        while proof[:dificultad] != '0'*dificultad:
            bloque.nonce += 1
            proof = bloque.generate_hash()
        bloque.nonce = 0
        return proof