transaccion1 = {
 'cantidad': '10',
 'emisor': 'Alicia',
 'receptor': 'Juan'}
transaccion2 = {
 'cantidad': '150',
 'emisor': 'Juan',
 'receptor': 'Alicia'}
transaccion3 = {
 'cantidad': '200',
 'emisor': 'Alicia',
 'receptor': 'Pedro' }
transaccion4 = {
 'cantidad': '30',
 'emisor': 'Rodrigo',
 'receptor': 'Tomas' }
transaccion5 = {
 'cantidad': '20',
 'emisor': 'Pedro',
 'receptor': 'Tomas' }
transaccion6 = {
 'cantidad': '42',
 'emisor': 'Rosa',
 'receptor': 'Javier' }
mempool = [transaccion1, transaccion2, transaccion3, transaccion4, transa
ccion5, transaccion6]
mi_transaccion = {
 'cantidad': '100',
 'emisor': 'Claudio',
 'receptor': 'Gabriel' }
mempool.append(mi_transaccion)
block_transacciones = [transaccion1, transaccion6, my_transaccion]