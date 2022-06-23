
		# ARCHITETTURA DEGLI ELABORATORI #

			 # ISTRUZIONI (intro) #

# Tutte le istruzioni base che il processore può eseguire,
# fanno parte dell'ISA (Instruction Set Architecture).
	
# Tipi di istruzioni:
# 	• Logico/Aritmetiche
#	• Trasferimento dati
# 	• Salti (condizionati e incondizionati)
#	• Gestione delle eccezioni/interrupt


# Prima di proseguire definiamo alcuni concetti chiave 
# propedeutici alla comprensione delle istruzioni.


			  ####################
			  # RAPPRESENTAZIONE #
			  # DELLE ISTRUZIONI #
			  ####################
		  
# Ci sono diversi tipi di formati di rappresentazione, al momento
# ne vedremo 3:
#	• Formato R-TYPE (tipo-registro), per operazioni logico/aritm.
# 	• Formato I-TYPE (tipo-immediato), per operazioni di
#	   trasferimento dati, operazioni immediate e salti condizionati.
#	• Formato J-TYPE (tipo-jump), per salti non condizionati.

#                  FORMATO R-TYPE
#   ————————————–––––––––––––––––––––––––––
#  |  OP  |  RS  |  RT  |  RD  | SHAMT | FUNCT |  -> campi (field)
#   ————————————–––––––––––––––––––––––––––
#	6 bit  5 bit  5 bit	 5 bit  5 bit	6 bit

# Campi: (singole parti che compongono l'istruzione)
# 	• OP		- (Operation Code) Operazione base dell'istruzione,
#			   dove si specifica il "genere di operazione".
#	• RS    - Registro contenente il primo operando sorgente.
#	• RT    - Registro contenente il secondo operando sorgente.
#	• RD    - Registro di destinazione (riceve il risultato
#			  dell'operazione).
#	• SHAMT - (Shift Amount) Numero di posizioni di scorrimento.
#	• FUNCT - Seleziona una specifica variante dell'operazione
#			  base definita dall'opcode. (es. aritm - addizione)


#                  FORMATO I-TYPE
#   ————————————–––––––––––––––––––––––––––
#  |  OP  |  RS  |  RT  | costante o indirizzo |
#   ————————————–––––––––––––––––––––––––––
#	6 bit  5 bit  5 bit	 		16 bit


#                  FORMATO J-TYPE
#   ————————————–––––––––––––––––––––––––––
#  |  OP  |  		  indirizzo  			   |
#   ————————————–––––––––––––––––––––––––––
#	6 bit  		 		26 bit



				##################
				#     MODI DI    #
				# INDIRIZZAMENTO #
				##################
				
# In questa sezione vediamo vari modidi indirizzamento i dati:
#	• IMPLICITO
#		 ——————
#		|  opcode  |
#		 ——————
#	  .Sorgente/destinazione fissa (destinato al 
#	   funzionamento di base della cpu)
#	  .0 accessi alla memoria

#	• IMMEDIATO
#		 ——————–––––––––––––
#		|  opcode  | operando |
#		 ————————————–
#	  .Valore costante codificato nell'istruzione stessa
#	  .0 accessi alla memoria

#	• DIRETTO
#		 ——————––––––––––
#		|  opcode  | adress |
#		 ———————————
#	  .Nell'istruzione contenuto indirizzo di memoria
#	  .1 accesso alla memoria

#	• INDIRETTO
#		 ——————––––––––––
#		|  opcode  | adress |
#		 ———————————
#	  .Nell'istruzione contenuto un indirizzo che fa riferimento
#	   ad un secondo indirizzo in memoria (es. puntatori)
#	  .2 accessi alla memoria

#	• A REGISTRO
#		 ——————–––––––––––––
#		|  opcode  | registro |
#		 ————————————–
#	  .Si opera all'interno dei registri
#	  .0 accessi alla memoria

#	• A REGISTRO INDIRETTO
#		 ——————–––––––––––––
#		|  opcode  | registro |
#		 ————————————–
#	  .Il registro contiene un indirizzo di memoria
#	  .1 accesso alla memoria

#	• CON SPIAZZAMENTO(OFFSET)
#		 ——————–––––––––––––––––––––––––––––
#		|  opcode  | reg. (+) Offset/Immed. |
#		 ————————————–––––––––––––––––
#	  .Il registro contiene un indirizzo, al quale sommare
#	   l'offset(costante), per accedere alla memoria
#	  .1 accesso alla memoria



				################
				# ARCHITETTURA #
				#	  MIPS	   #
				################

# 3 CPU:
#	• CPU (comprende l'ALU)
#	  .32 registri da 32 bit
#	  .Ha accesso alla memoria

#	• COPROC. 0
#	  .Stato del programma
#	  .Errori ed eccezioni

#	• COPROC. 1 (calcoli in virgola mobile)
#	  .32 registri da 32 bit utilizzabili vome 16 da 64 bit
#	  .Ha accesso alla memoria



			    ###############
			    # FORMATI DEL #
			    #  COPROC. 1  #
			    ###############

# ne vedremo 3:
#	• Formato FR-TYPE (tipo-registro float)
#	  .Senza accesso alla memoria
#	  .Istruzioni della FPU (Floating-Point Unit)

# 	• Formato FI-TYPE (tipo-float immediato)
#	  .Load/Store
#	  .Salti condizionati

#                  	FR-TYPE
#   ————————————–––––––––––––––––––––––––––
#  |  OP  |  RS  |  RT  |  RD  | SHAMT | FUNCT |
#   ————————————–––––––––––––––––––––––––––
#	6 bit  5 bit  5 bit	 5 bit  5 bit	6 bit

#                  	FI-TYPE
#   ————————————–––––––––––––––––––––––––––
#  |  OP  |  RS  |  RT  | costante o indirizzo |
#   ————————————–––––––––––––––––––––––––––
#	6 bit  5 bit  5 bit	 		16 bit





.data

.text
