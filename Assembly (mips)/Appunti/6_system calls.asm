
		# ARCHITETTURA DEGLI ELABORATORI #

		  		 # System Calls #

# Le System Calls permettono di comunicare con il sistema operativo
# per fargli eseguire un determinato comando in base ad un parametro
# che viene passato al registro $v0.

# INPUT:
#	• $v0				operazione richiesta
#	• $a0.. $a2, $f0 	eventuali parametri

# OUTPUT:
#	• $v0, $f0		 	eventuale risultato


#	  ISTRUZIONE	   CODE
# | print int		 |	1	|
# | print float		 |	2	|
# | print double	 |	3	|
# | print string	 |	4	|
# | read int		 |	5	|
# | read float		 |	6	|
# | read double		 |	7	|
# | read string		 |	8	|
# | sbrk*			 |	9	|
# | exit**			 |	10	|
# | print char		 |	11	|
# | read char		 |	12	|
# | open file		 |	13	|
# | read from file	 |	14	|
# | write to file	 |	15	|
# | close file		 |	16	|
# | exit2***		 |	17	|
# | time****		 |	30	|
# | sleep(millisec.) |	32	|
# | print int in hex |	34	|
# | print int in bin |	35	|
# | print int as uns |	36	|
# | random int		 |	41	|
# | random float	 |	43	|
# | random double	 |	44	|

#    * alloca dati nella memoria heap (area dei dati dinamici che cresce verso lo stack)
#   ** termina l'esecuzione
#  *** termina l'esecuzione con un valore
# **** millisecondi passati dal 1 gennaio 1970

# Per altro consultare:
# https://courses.missouristate.edu/kenvollmar/mars/help/syscallhelp.html


	#	# ##### #	  #		#####
	#	# #		#	  #		#   #
	##### ####	#	  #		#   #
	#	# #		#	  #		#   #
	#	# #####	##### #####	#####

	#	# #####	####  #		####   ##
	#	# #   #	#   # #		#	#  ##
	# #	# #   #	####  #		#	#  ##
	 ###  #   #	#  #  #		#	# 
	 # #  #####	#   # #####	####   ##

.globl main

.data
	string: .asciiz "Hello world!"
	
.text
	main:
		li $v0, 4
		la $a0, string
		syscall


