
		# ARCHITETTURA DEGLI ELABORATORI #

				# ISTRUZIONI_pt3 #


.globl main

.data

.text

main:

			    	#########	
 			    	# SALTO #
 			    	#########

# Abbiamo 2 tipi di salto:
#	• Condizionato (branch) - in base ad una certa condizione spostiamo
#					 avanti o indietro il PC (Program Counter)
#			.if, else

#	• Incondizionato (jump) - salta in un punto senza condizioni
#			.while



# 				SALTI CONDIZIONATI:  (per chiari motivi di flusso instabile, gli esempi saranno commentati)

#	• beq  (branch on equal)
#	beq $s0, $s1, Else		# vai a Else (etichetta contenente un indirizzo) se s0 == s1

#	• bne  (branch on not equal)
#	bne $s0, $s1, Else		# vai a Else se s0 != s1

#	• blez (branch on less or equal than 0)
#	blez $t0, Else			# se t0 <= 0 salta all'Else

#	• bge (branch on greater or equal than 0)
#	bge $t0, $t1, Else		# se t0 >= t1 salta all'Else

#	• bltz (branch on less than 0)
#	bltz $t0, Else			# se t0 < 0 salta all'Else

#	• bgtz (branch on greater than 0)
#	bgtz $t0, Else			# se t0 > 0 salta all'Else


#			ASSEGNAMENTI CONDIZIONATI: (tutti i controlli settano il registro a 1 se veri altrimenti a 0

#	• slt   (set if less than)
#	slt	$s0,$s1,$s2

#	• slti  (set if less than immediate)
#	slti $s0,$s1,10

#	• seq   (set if equal)
#	seq $t1, $t2, $t3

#	• sge   (set if grater or equal)
#	sge $t1, $t2, $t3


#			  SALTI INCONDIZIONATI:

#	• j   	(jump unconditionally)
#		.Salta all'indirizzo della costante
#	j C

#	• jal   	(jump and link)
#		.Salta all'indirizzo della procedura (funzione) e
#		 contemporaneamente salva l'indirizzo dell'istruzione 
#		 successiva a quella di salto nel registro $ra
#		.Consente di spezzare il flusso di esecuzione, eseguire
#		 una funzione e (quando la funzione, che vedremo in
#		 seguito, arriva a $ra) riprendere dall'istruzione
#		 successiva a quella dove era stato eseguito il salto
#	jal func

#	• jr   	(jump register unconditionally)
#		.Utillizzato alla fine di una procedura per ritornare
#		 al punto dove la funzione era stata chiamata
#func:
#	jr $ra


