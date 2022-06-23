
		# ARCHITETTURA DEGLI ELABORATORI #

			   # ISTRUZIONI_pt1 #


			  ##################
 			  # ARITM./LOGICHE #
 			  ##################
.globl main

.data
f: .float 12.4

.text

main:
	l.s $f2, f  # carico nel registro $f2 del coproc. 1 il valore di f (12.4)
	
	

#		 ARITHMETIC:

# 	• addi  (addition immediate)
# 		.Somma immediata di una costante con il valore di un registro
	addi $t0, $zero, 15  # ($t0 = 0 + 15)
	
# 	• add  (addition)
# 		.Somma tra i valori di due registri
	add $t1, $t0, $t0	# ($t1 = 15 + 15)

# 	• add.s  (single precision addition)
# 		.Somma tra razionali in 32 bit
	add.s $f0, $f2, $f2  # ($f0 = 12.4 + 12.4)
	
# 	• add.d  (double precision addition)
# 		.Somma tra razionali in 64 bit
	add.d $f4, $f0, $f2

# 	• addu  (unsigned addition)
# 		.Somma tra numeri senza segno
	addu  $t2, $t0, $t1

# 	• sub  (subtraction)
	subi $t2, $t2, 35

# 	• mul  (multiplication)
	mul $t2, $t2, $t0

# 	• div  (division)
	div $t2, $t1, $t0

# 	• abs  (absolute value)
	subi $t2, $t2 100
	abs $t3, $t2	#il numero binario si inverte e si somma 1

# 	• neg  (negate)
# 		.Nega un numero
	neg $t4, $t0
	neg $t4, $t4
	
	
#		 CONVERSION:
	
# 	• cvt.w.s  (convert from single precision to word)
	cvt.w.s $f4, $f0

# 	• cvt.s.w  (convert from word to single precision)
	cvt.s.w $f5, $f4
	
	
#		 LOGICAL:
	
# 	• and  (and bitwise)
	and $t5, $t2, $t3

# 	• or  (or bitwise)
	or $t6, $t2, $t3
	 
# 	• nor  (nor bitwise)
	nor $t6, $t2, $t3
		 
# 	• sll  (shift left logical)
	sll $s0, $t5, 4
	
# 	• srl  (shift right logical)
	neg $s0, $s0
	srl $s1, $s0, 2

# 	• sra  (shift right arithmetic)
	sra $s2, $s0, 2

# 	• rol  (rotate left)
# 		.Rotazione dei bit in senso anti-orario
	rol $s3, $s1, 2
	
# 	• ror  (rotate right)
# 		.Rotazione dei bit in senso orario
	ror $s4, $s1, 2





