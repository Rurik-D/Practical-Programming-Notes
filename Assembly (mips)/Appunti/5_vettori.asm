
		# ARCHITETTURA DEGLI ELABORATORI #

			  # VETTORI E MATRICI #


.globl main

.data
				  #############
 			   	  # DIRETTIVE #
 			      #############
 			      
# Direttive principali per l'assemblatore:
#	• .data		 (definizione dei dati statici)
#	• .text		 (definizione del programma)
#	• .globl sym	 (dichiara il simbolo come globale e può essere referenziato da altri file)

#	• .byte		 (sequenza di byte)
bt: .byte 1 2 3 4

#	• .half		 (sequenza di half-words)
hf: .half 1 2

#	• .word		 (sequenza di words)
wd: .word 1

#	• .asciiz	 (sequenza di caratteri memorizzati come valori ascii, terminata da \0)
asc: .asciiz "sopra la panca"

#	• .float		 (per valori in single precision)


# Etichette (per calcolare gli indirizzi relativi)
#	NomeEtichetta: - direttiva - valori


				   ###########
				   # VETTORI #
				   ###########

# Caratteristiche dei vettori:
#	• Sequenza di N elementi di dimensioni uguali
#	• Elementi consecutivi in memoria
#	• Elementi indirizzabili per indice da D*0 a D*(N-1) dove D è
#	  la dimensione dell'elemento (word 4, half-word 2, byte 1 ecc..)
#	• Definibili staticamente nella sezione .data del programma, usando
#	  un'etichetta (label) per indicare l'indirizzo del primo elemento 
#	  del vettore
#	• Per indirizzare l'elemento i-esimo del vettore V si aggiunge 
#	  l'offest che è uguale a i*D 
#		i*D(V)  =>  offset + indirizzo_primo_el_di_V

# Indirizzamento dei vettori nella memoria ( ENDIANESS ) :
#	• Big endian (usato da Java e dalle CPU SPARC Sun/Oracle, e dal MIPS)
#	  .Byte della word memorizzati dal MSB al LSB

#	• Little endian (usato dalle CPU Intel, ad es. Windows, e da MARS)
#	  .Byte della word memorizzati dal LSB al MSB


				  ######################
				  # SCANSIONE ELEMENTI #
				  #	  TRAMITE CICLI	   #
				  ######################
#.data
	Vettore: .word	1, 2, 3, 4, 5, 6, 7, 8, 9 # vettore da sommare
	N:		 .word	9 						  # numero di elementi
	Somma:	 .word	0 						  # risultato
	
# SCANSIONE PER INDICE (si utilizza un registro per salvare un indice)
#	- Pro:
#		• Comoda se si deve usare l'indice dell'elemento per controlli
#		• L'incremento dell'indice non dipende dalla dimensione degli elementi
#		• Comoda se il vettore è allocato staticamente (nella sezione .data)
#	- Contro:
#		• Bisogna sempre convertire l'indice nel corrispondente offset in byte


# ESEMPIO

.text
	main:	li	 	$t0, 0			  # i = 0
			lw 		$t1, N 			  # lettura di N
			li 		$t2, 0 			  # somma = 0
	loop: 	bge 	$t0, $t1, fine    # è finito il ciclo?
			sll 	$t3, $t0, 2 	  # offset: i*4
			lw 		$t3, Vettore($t3) # lettura di Vettore[i] (riuso t3)
			add 	$t2, $t2, $t3 	  # somma += Vettore[i]
			addi 	$t0, $t0, 3 	  # i += 3
			j 		loop 			  # riparte il ciclo
	fine: 	sw 		$t2, Somma 		  # memorizzo il risultato
	
# SCANSIONE PER PUNTATORE (Manipolazione diretta degli indirizzi in memoria)
#	- Pro:
#		• Si lavora direttamente su indirizzi in memoria
#		• Ci sono meno calcoli nel ciclo
#	- Contro:
#		• Non si ha a disposizione l'indice dell'elemento (ovviamente)
#		• L'incremento del puntatore dipende dalla dimensione degli elementi
#		• Bisogna calcolare l'indirizzo successivo all'ultimo elemento


# ESEMPIO

#.text
#	main: 	lw 		$t1, N 			  # lettura di N
#			la $t0, Vettore 		  # indirizzo di Vettore
#			sll $t1, $t1, 2 		  # dimensione = N * 4
#			add $t1, $t1, $t0 		  # fine = ind.Vettore + dim
#			li $t2, 0 				  # somma = 0
#	loop: 	bge $t0, $t1, fine 		  # è finito il ciclo?
#			lw $t3, ($t0) 			  # lettura di Vettore[i]
#			add $t2, $t2, $t3 		  # somma += Vettore[i]
#			addi $t0, $t0, 12 		  # i += 3 * dim_elemento
#			j loop
#	fine: 	sw $t2, Somma			  # memorizzo il risultato


					###########
					# MATRICI #
					###########

# Una matrice M * N è una successione di M vettori ciascuno di N elementi

# Numero di elementi: 			M * N
# Dimensione totale in byte : 	M * N * D (dimensione degli elementi)

# La si definisce staticamente come un vettore contenente M * N elementi (delle stesse dimensioni)

# .data 
#	 matrice:  .word  0:91    =>	Spazio per una matrice 7 * 13 word

# Se volessimo selezionare l'elemento in posizione x = 9, y = 2:
#  l'elemento si trova al nono elemento della riga 2 
#			offset = 2 * 13 + 9 = word 35
#			byte   = 35 * 4 = byte 140

# MATRICE 3D
# una matrice tridimensionale è una successioni di P matrici 
# 2D (M * N) e ha dimensioni  M * N * P

# l'elemento di coordinate x, y, z è preceduto da:
#	.z (strati)
#	.y (righe)
#	.x (elementi)

# L'elemento si trova quindi in posizione:
#  indirizzo_matrice + (z * (M * N) + y * N + x) * dim_el







