
		# ARCHITETTURA DEGLI ELABORATORI #

				# ISTRUZIONI_pt2 #


			    #################	
 			    # TRASFERIMENTO #
 			    #################

.globl main

.data
v: .word 4 6 8 3 2 	# Creo un'etichetta (n) che rappresenta un indirizzo
		   			#  in memoria contenente un vettore di word.
		   			# Le etichette vengono tradotte automaticamente dall'assembler
		  	 		#  in indirizzi di memoria.
h:  .word -128
hu: .word 32768
.text

main:
	
# Ricordiamo:
#	• 32 registri da 32 bit nella CPU
#		.Accesso veloce ai dati

#	• 32 registri da 32 bit nella Coproc. 1
#		.Utilizzabili come 16 da 64

#	• 2^30 word di memoria
#		.Grande array monodimensionale
#		.Indirizzamento al byte (parole consecutive hanno
#		 indirizzi di memoria a distanza di 4)



 		  
# Istruzioni di base:
#	• li (load immediate) -> caricamento costante nella mezza word superiore
#		.Caricamento immediato di una costante
	li $t0, 0xa

#	• la (load address) -> caricamento costante nella mezza word superiore
#		.Caricamento di un'indirizzo in un registro
	la $t1, v

# 	• lw  (load word)
# 		.Trasferire una word da una locazione di memoria 
#		 in un registro
	lw $t2, 4($t1)

# 	• sw  (store word)
#		.Trasferire il contenuto di un registro in una
#		 locazione di memoria
	sw $t0, 0x20($t1)

# 	• l.s  (store floating) -> Coproc 1
#		.Trasferire un float da una locazione di memoria 
#		 in un registro del coproc 1 in single precision
	l.s $f0, 8($t1)
	l.s $f1, 12($t1)
	div.s $f2, $f0, $f1
	

# 	• s.s  (store floating) -> Coproc 1
#		. Trasferire il contenuto di un registro float 
#		  in una locazione di memoria (single precision)
	s.s $f2, 0x24($t1)
	

#	• lh  (load half)
#		.Trasferimento di mezza word da memoria a registro (2 byte)
#		.Estende il bit di segno (MSB) nei 2 byte superiori
	lh $t3, h
	lh $t4, hu		#error
	

#	• lhu (load half unsigned)
#		.Trasferimento di mezza word da registro a memoria (2 byte)
#		.Estende zeri nei 2 byte superiori
	lhu $t5, h		#error
	lhu $t6, hu

#	• sh  (store half)
#		.Trasferimento di una mezza word da registro a memoria

#	• lb  (load byte)
#		.Trasferimento di un byte da memoria a registro
#		.Estende il bit di segno (MSB) nei 3 byte superiori

#	• lbu (load byte unsinged)
#		.Trasferimento di un byte da memoria a registro
#		.Estende zeri nei 3 byte superiori

#	• sb  (store byte)
#		.Trasferimento di un byte da registro a memoria

#	• ll  (load linked) -> lettura di una parola e blocco
#		.Caricamento di una word come prima fase di un'operazione
#		 atomica (un'operazione atomica è un'operazione indivisibile
#		 dal punto di vista logico, nessun'altra operazione può
#		 iniziare prima che l'operazione atomica sia conclusa)

#	• sc  (strore condizional) -> memorizzazione condizionata di una word
#		.Memorizzazione di una word come seconda fase di
#		 un'operazione atomica

#	• lui (load upper immediate) -> caricamento costante nella mezza word superiore
#		.Caricamento di una costante nei 16 bit più significativi










#	la $t0, v 		# Carico l'indirizzo di memoria associato ad n
#	lw $t1, v 		# Carico il primo valore contenuto nell'indirizzo di memoria associato ad n
#	lw $t2, ($t0)   # Carico il primo valore contenuto nell'indirizzo di memoria, contenuto
#					#  nel registro $t0, associato ad n con offset di 0
#	lw $t3, 4($t0)  # Carico il secondo valore
#	li $t1, 0
	
	
