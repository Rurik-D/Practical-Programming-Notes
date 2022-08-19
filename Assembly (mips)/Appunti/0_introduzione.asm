
		# ARCHITETTURA DEGLI ELABORATORI #

				# INTRODUZIONE #
		
		
					#######			
					# CPU #
					#######
			
# La Central Processing Unit è formata da:
# 	• Unità di elaborazione Aritmetico/Logica (ALU)
#		.Fa solo calcoli
#		.Non ha uno stato interno

#	• La Control Unit
#		.Coordinare tutte le azioni necessarie per 
#		 l'esecuzione di una istruzione o insiemi di istr.

#	• I Registri
#		.A uso generale e speciale
#		.Consentono manipolazione di istruzioni, dati,
#		 indirizzi, risultati

#	• Il Bus di comunicazione con la Memoria
#	• Il Bus di comunicazione con le Perifieriche (in/out)


                #################
                # CPU DELLA IAS #
                #    MACHINE    #
                #################
			
# L'IAS machine fu il primo computer digitale costruito 
# dall'Institute for Advanced Study di Princeton nel 1951.

# Aveva una memoria da 1000 word da 40 bit ciascuna.
# Ciascuna word conteneva 2 istruzioni.

# Componenti della sua CPU:
#	• MBR (Memory Buffer Register)
#		.Riceve/manda dati dalla/alla memoria

#	• MAR (Memory Address Register)
#		.Indica l'indirizzo della locazione di memoria RAM
#		 in cui si andrà a leggere/scrivere un dato

#	• PC  (Program Counter)
#		.Registro contente l'indirizzo dell'istruzione 
#		 in esecuzione

#	• IR  (Instruction Register)
#		.Riceve l'istruzione da eseguire

#	• IBR (Instruction Buffer Register)
#		.Memorizza temporaneamente la seconda istruzione
#		 della word

#	• AC  (Accumulatore)
#		.Per i risultati parziali dei caloli della ALU

#	• MQ  (Multiplier Quotient)
#		.Per i risultati parziali dei caloli della ALU


                    ########
                    # MIPS #    -> (Milion Instructions Per Second)
                    ########

# Il MIPS è un'architettura di tipo RISC: (Reduced Instruction Set Computer)
#    • Istruzioni di dimensione fissa
#        .Fetch(vedi dopo) della successiva senza decodifica della prec.
#    • Istruzioni di formato uniforme
#        .Per semplificare la fase di decodifica
#    • Operazioni ALU solo tra registri
#        .Senza accesso a memoria
#    • Molti registri interni
#        .Per i risultati parziali senza accessi alla memoria
#    • Modi di indirizzamento semplici
#        .Con spiazzamento, 1 solo accesso a memoria
#        .Durata fissa della istruzione
#        .Conflitti semplici
#    • Istruz. semplici => pipeline più veloce

# Le istruzioni sono tutte a 32 bit.
# BYTE(8 bits), HALFWORD (2 bytes), WORD (4 bytes).
# Un carattere (tradotto in ascii) richiede un byte di spazio.
# Un intero può richiedere da un byte fino ad un'intera word.


	             ############
                 # REGISTRI #
                 ############
			
# I registri consentono l'accesso veloce dei dati.
# Nel MIPS gli operandi devono essere contenuti nei registri per poter eseguire
# delle operazioni.

# Abbiamo 32 registri divisi in gruppi, ogni registro è preceduto da $.
# 2 formati per usare i registri:
#	• Usando il numero del registro, da $0 a $31
#	• Usando i nomi equivalenti, $t1, $sp ecc..

# I registri speciali "lo" e "hi", vengono utilizzati dall'assembler per i
# risultati parziali di moltiplicazioni e divisioni, direttamente indirizzabili
# nel programma.
# Il contenuto è accessibile tramite l'istruzione speciale mfhi/mflo
# ("move from Hi" e "move from Lo").

# ______________________________________________________________________________
#   0    -    $zero
#	 .Contiene sempre il valore 0

#   1	 -    $at        -    Assembler Temporary
#	 .Riservato all'assembler per la gestione di costanti molto lunghe

#  2/3   -    $v0/$v1    -    Values
#	 .Risutlati e valutazione di espressioni

#  4/7   -    $a0/$a3    -    Arguments
#	 .Argomenti da passare alle procedure

#  8/15  -    $t0/$t7    -    Temporaries
#	 .Variabili temporanee

#  16/23 -    $s0/$s7    -    Saved Values
#	 .Variabili da salvare

#  24/25 -    $t8/$t9    -    Temporaries
#	 .Altri registri temporanei

#  26/27 -    $k0/$k1
#	 .Riservati per l'uso da parte del interrupt/trap handler

#  28    -    $gp        -    Global Pointer
#	 .Per gestire dati dinamici non locali

#  29    -    $sp        -    Stack Pointer			   	
#	 .Memorizza l'indirizzo dell'ultimo dato aggiunto nello STACK,
#	  per chiamate nidificate e variabili locali

#  30    -    $fp        -    Frame Pointer
#	 .Valore che individua la posizione dei registri salvati e delle
#	  variabili locali di una data procedura

#  31    -    $ra        -    Return Address 
#	.Serve per tornare all'esecuzione del del programma dopo la 
#	 chiamata di una procedura
# ______________________________________________________________________________


# Non preoccupatevi se le cose non sono chiare, ogni argomento verrà ripreso in seguito

                    ###########
                    # MEMORIA #
                    ###########
			
# I contenuti delle locazioni di memoria possono rappresentare sia
#  istruzioni che dati.
# La memoria è vista come un unico grande ARRAY UNIDIMENSIONALE di bytes.
# Un indirizzo di memoria costituisce un indice all'interno dell'array.
# MIPS utilizza un indirizzamento al byte, cioè l'indice punta ad un
#  byte di memoria.
# Byte consecutivi hanno indirizzi consecutivi.
# Indirizzi di word consecutive differiscono di un fattore 4 
#  (8bit * 4 = 32bit).

# Organizzazione logica della memoria:
	#---------------------------# 0x7fffffff
	#      D    Stack    D      #
	#---------------------------# <- SP 0x7ffffffc (decresce verso il Data Segment)
	#                           #
	#      Spazio Libero        #
	#                           #    (i dati dinamici crescono verso lo Stack,
	#---------------------------# <- GP 0X10008000  il GP viene impostato con un indirizzo
	#    U Dati Dinamici U 	    #    che rende facile l'accesso ai dati)
	#---------------------------# Data Segment
	#    Dati Statici(.data)    #
	#---------------------------# 0x10000000
	#                           #
	#  Programma Utente(.text)  # -> dove l'utente scrive il codice
	#                           # 
	#---------------------------# <- PC 0x00400000 (Program Counter)  
	#   Riservato al Kernel     #
	#---------------------------#

# STACK:
#  Struttura dati contenente una coda di tipo "last-in-first-out",
#  (ultimo-inserito-primo-estratto) utilizzata per salvare il
#  contenuto dei registri.


                ######################
                # FASI DI ESECUZIONE #
                #  DI UN'ISTRUZIONE  #
                ######################
		
# FETCH - Caricamento di una istruzione.
#    (Dalla posizione idicata dal Program Counter)
# DECODIFICA - Riconoscimento dell'istruzione.
#    (La Control Unit attiva le parti funzionali necessarie)
# LOAD - Caricamento di eventuali argomenti.
#    (A seconda dei modi di indirizzamento)
# ESECUZIONE dell'istruzione.
#    (in genere da parte dell'ALU)
# STORE - salvataggio del risultato.
#    (In memoria o in un registro)
# AGGIORNAMENTO DEL PROGRAM COUNTER.
#    (contemporaneamente ad altre fasi)



.globl main  # indicates start of code (first instruction to execute)
	
.data        # variable declarations follow this line

.text        # instructions follow this line	

main:
