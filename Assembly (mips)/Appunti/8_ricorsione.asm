
		# ARCHITETTURA DEGLI ELABORATORI #

				 # RICORSIONE #

# Dicasi "FUNZIONE RICORSIVA" quella funzione che per risolvere un dato
# problema, lo scompone in sottoproblemi e richiama sé stessa su di essi.
# Il procedimento si ripete sui sottoproblemi e continua fino al
# raggiungimento di un CASO BASE.

.globl main

.data
	prompt: .asciiz "Inserire un numero intero per ottenerne il fatoriale:\n"
.text
	main:
		li 	 	$v0, 4
		la 	  	$a0, prompt
		syscall
		li 	  	$v0, 5
		syscall
		move	$a0, $v0
		
#		j 	f_iterativo
		la		$ra, exit		# per questa ricorsione faccio non faccio partire ra da 0 per
		j 	f_ricorsivo			# evitere di chiudere il programma una volta finite le ricorsioni
		
		
	f_iterativo:
		subi	$sp, $sp, 4
		sw		$a0, 0($sp)
		
		li		$v0, 1
		while:
			blez	$a0, exit
			mul		$v0, $v0, $a0
			subi	$a0, $a0, 1
			j		while
			

	f_ricorsivo:
		blez	$a0, CasoBase
		
		PassoRicorsivo:
			# salvo i dati nello stack
			subi	$sp, $sp, 8
			sw		$ra, 0($sp)
			sw		$a0, 4($sp)
			
			# decremento il valore ricevuto in input ed eseguo la ricorsione
			subi	$a0, $a0, 1
			jal		f_ricorsivo
			
			# recupero i dati dallo stack
			lw		$a0, 4($sp)
			lw		$ra, 0($sp)
			addi	$sp, $sp, 8
			
			# eseguo la moltiplicazione del fattoriale
			mul		$v0, $v0, $a0
			# ritorno all'ultima chiamata ricorsiva o chiudo il programma(in questo caso vado su exit)
			jr		$ra
			
		CasoBase:
			addi	$v0, $0, 1
			jr		$ra
		
		
	exit:
		move    $a0, $v0
		li 		$v0, 1
		syscall
			