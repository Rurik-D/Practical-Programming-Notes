
		# ARCHITETTURA DEGLI ELABORATORI #

				  # PROCEDURE #
            
# Le procedure (o funzioni) sono parti di codice riutilizzabili
# che ricevono argomenti in input e restituiscono un output.

# Caratteristiche:
#	• Ha un indirizzo di partenza memorizzato in una label
#	• Riceve uno o più argomenti
#	• Svolge un calcolo
#	• Ritorna un risultato
#	• Continua la sua esecuzione dall'istruzione seguente a
#	  quella che l'ha chiamata

# Registri importanti per le procedure:
#	• $a0/$a3 => registri argomento per il passaggio dei parametri
#	• $v0/$v1 => registri valore per la restituzione dei valori calcolati
#	• $ra	 => registro contenente l'indirizzo di ritorno per tornare
#				al punto del programma dove la funzione è stata chiamata

# Istruzioni necessarie:
#	• jal etichetta		Jump And Link
#	  .Memorizza nel registro $ra la posizione dell'istruzione
#	   successiva alla chiamata di funzione (dove riprendere
#	   l'esecuzione une volta finita la funzione)
#	  .Modifica il PC per iniziare l'esecuzione del corpo della funzione

#	• jr $ra				Jump to Register
#	  .Salta all'indirizzo contenunto nel registro (ritorna
#	   al punto dove la funzione è stata chiamata)

# Riepilogo passaggi per chiamata di procedura:
#	1) Programma chiamante (detto anche semplicemente "chiamante") inserisce
#		i parametri da passare nei registri $a0/$a3.
#	2) Chiamante utilizza l'istruzione " jal X " per saltare alla procedura
#		X (detta anche "chiamata") memorizzando in $ra l'indirizzo della
#		riga successiva.
#	3) X esegue le operazioni e memorizza i risultati in $v0-$v1.
#	4) X restituisce il controllo al chiamante con l'istruzione jr $ra.

# La chiave di volta delle procedure è quindi il PC (Program Counter) il 
# quale ricordiamo essere un registro che memorizza l'indirizzo dell'istruzione
# in esecuzione. (andrebbe più propriamente chiamato "instruction address register")

# L'istruzione jal salva semplicemente in $ra PC + 4.

# Nel caso si abbia bisogno di più registri per passare o ritornare valori, la
# struttura dati ideale per copiare il contenuto dei registri è lo STACK (pila).
# Lo stack utilizza un puntatore per tenere traccia dell'ultimo valore inserito,
# esso prende il nome di STACK POINTER ed è memorizzato neln registro $sp.
# Ricordiamo che lo STACK decresce verso l'HEAP (che al contrario cresce verso
# lo STACK), zona dove vengono memorizzati i dati dinamici (tramite "malloc" in 
# C o "new" in Java), il che significa che lo STACK POINTER diminuirà all'aggiunta
# di nuovi dati, aumentando la dimensione dello STACK, e aumenterà alla loro rimozione,
# diminuendo di consequenza la dimensione dello STACK.
# Ovviamente la dimensione dell'incremento o del decremento dello STACK POINTER
# dipende dalla dimensione dei dati che vengono memorizzati (word +/-4, half +/-2 ecc)

# Esiste anche un secondo puntatore, il FRAME POINTER ($fp) che, a differenza dello 
# STACK POINTER (usato per puntare l'ultimo elemento inserito nello stack), punta
# al primo elemento elemento salvato durante una data procedura. E' quindi statico
# e non cambia durante la procedura (a  differenza dello SP).

# Vengono spesso usate due parole onomatopeiche per definire il trasferimento di dati
# tra registri e STACK:
#	• push	-	Inserimento di dati nello STACK
#	• pop	-	Estrazione di dati dallo STACK

#		ESEMPIO
# Eseguire l'operazione f = (g + h) - (i + j) con l'utilizzo di procedure

.globl main
.data
	g:	.word	45
	h:	.word	32
	i:	.word	26
	j:	.word	30
#	f sarà uguale a 21
	
	useless:  .asciiz "ciao"
	vittoria: .asciiz "21 vittoria grande baldoria"

.text

		
	main:
		# Poniamo per esempio che i 3 registri che useremo nella procedura
		# contengano già dei valori che non possiamo perdere
		
		lw 	 $t0, useless
		li 	 $t1, 4123
		li 	 $s0, 0xf3e1
		
		# Prepariamo i valori che ci servono al passaggio per argomento
		
		lw 	 $a0, g
		lw 	 $a1, h
		lw 	 $a2, i
		lw 	 $a3, j
		
		# Prima di chiamare la procedura salviamo nello stack i valori che
		# non vogliamo perdere
		
		addi $sp, $sp, -12		# Aggiorniamo lo SP per far spazio a 3 word
		sw	 $t0, 8($sp)
		sw	 $t1, 4($sp)
		sw	 $s0, 0($sp)
		
		jal		example
		
		# Dopo aver eseguito la procedura, restituisco a t0, t1, s0 i valori
		# precedenti alla chiamata
		
		lw	 $t0, 8($sp)
		lw	 $t1, 4($sp)
		lw	 $s0, 0($sp)
		
		move $s1, $v0				# Sposto il valore ritornato in un nuovo registro
		beq  $s1, 21, exit			# Uso un controllo per uscire dal programma (sempre vero)
		
#		j 	 exit					# (scommentate se volete mettere mano al codice)
		
	example:
		add  $t0, $a0, $a1			# (g + h)
		add  $t1, $a2, $a3			# (i + j)
		sub  $s0, $t0, $t1			# f = (g + h) - (i + j)
		
		add	 $v0, $s0, $zero		# Salvo il valore di s0 per ritornarlo
		
		jr $ra
	
	exit:
		li	 $v0, 4
		la	 $a0, vittoria
		syscall

		
# Nell'esempio precedente abbiamo posto il caso in cui dovessimo utilizzare
# dei registri già occupati da altri valori, da dover salvare e ripristinare.

# In realtà MIPS mette a disposizione 18 registri, divisi in due gruppi 
# per ridurre il numero di registri da salvare in memoria:

#	• Temporary 		$t0/$t9	
#		.10 registri temporanei che non vengono salvati in caso di chiamata 
#		  a procedura (non sono quindi protetti da eventuale modifica)

#	• Saved		 	$s0/$s7	
#		.8 registri da salvare, il cui contenuto deve essere preservato in
#		  caso di chiamata a procedura (se vengono utilizzati dalla procedura
#		  il loro contenuto deve essere prima salvato)








