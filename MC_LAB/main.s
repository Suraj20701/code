;TW6-SORTING
	AREA MCTW5,CODE,READONLY
			ENTRY					;Mark first instruction to execute
START       MOV R8,#4
			LDR R2,=CVALUE
			LDR R3,=DVALUE
			
LOOP0		LDR R1,[R2],#4
			STR R1,[R3],#4
			SUBS R8,R8,#1
			CMP  R8,#0
			BNE LOOP0
				  
START1  	MOV R5,#3
			MOV R7,#0
			LDR R1,=DVALUE
						 
LOOP    	LDR R2,[R1],#4
			LDR R3,[R1]
			CMP R2,R3
			BLT LOOP2
			STR R2,[R1],#-4
			STR R3,[R1]
			MOV R7,#1
			ADD R1,#4
						  
LOOP2		SUBS R5,R5,#1
			CMP R5,#0
			BNE LOOP
			CMP R7,#0
			BNE START1
				  
L		B L
		
CVALUE DCD 0X44444444,0X11111111,0X33333333,0X22222222
		AREA DATA1,DATA,READWRITE
DVALUE DCD 0X00000000
		END
			
			
;TW5- Logical Instructions
	AREA tw5,CODE,READONLY
		ENTRY
		MOV R0,#0X80000002
		MOV R1,#0X80000011
		MOVS R2,R0,LSR #1
		MOVS R3,R0,LSL #1
		MOVS R4,R0,ASR #1
		MOVS R5,R1,ROR #1
		RRX R6,R0
		AND R7,R0,R1
		ORR R8,R0,R1
		EOR R9,R0,R1
		BIC R10,R0,R1
L		B L
	END
		
		
;TW4-GREATEST IN AN ARRAY
	AREA MAIN, CODE, READONLY
		ENTRY
		MOV R0, #5
		LDR R1, =SVALUE
		LDR R2, =RESULT
		MOV R4, #0
LOOP	LDR R3, [R1], #4
		CMP R3, R4
		BGT SWAP
CONT    SUBS R0, #1
		BNE LOOP
		STR R4, [R2]
		B L		
SWAP    MOV R4, R3
		B CONT			
L	B L
SVALUE DCD 0X11111111, 0X22222222, 0X00000000, 0X55555555, 0X44444444
	AREA MYDATA, DATA, READWRITE
RESULT DCD 0
	END

;TW3-FACTORIAL OF GIVEN NUMBER
	AREA MAIN, CODE, READONLY
		ENTRY
		MOV R0, #3
		MOV R1, #1
LOOP	MUL R1, R0, R1
		SUBS R0, #1
		TEQ R0, #1
		BNE LOOP
L	B L
	END
		




;TW2-ADDITION OF 16-BIT NUMBERS AND STORE RESULT IN MEMORY LOCATION
	AREA MAIN, CODE, READONLY
		ENTRY
		MOV R0, #5
		LDR R1, =SBLOCK
		LDR R2, =RESULT
		MOV R4, #0
LOOP	LDRH R3, [R1], #2
		ADD R4, R4, R3
		SUBS R0, #1
		BNE LOOP
		STRH R4, [R2]
L	 B L
SBLOCK DCW 0X1111, 0X2222, 0X3333, 0X4444, 0X5555
	AREA MYDATA, DATA, READWRITE
RESULT DCW 0
	END




;TW1B - DATA TRANSFER FROM ONE RAM LOCATION TO ANOTHER 16BIT[HALF WORD]
	AREA MAIN, CODE, READONLY
		ENTRY
		MOV R0, #10
		LDR R1, =SBLOCK
		LDR R2, =DBLOCK
GOTO    LDRH R3, [R1], #1
		STRH R3, [R2], #1
		SUBS R0, #1
		BNE GOTO
L	B L
SBLOCK DCW 0X1111, 0X2222, 0X3333,0X4444, 0X5555
	AREA MYDATA, DATA, READWRITE
DBLOCK DCW 0
	END

;TW1B - DATA TRANSFER FROM ONE RAM LOCATION TO ANOTHER 32BIT[WORD]
	AREA MAIN, CODE, READONLY
		ENTRY
		MOV R0, #5
		LDR R1, =SBLOCK
		LDR R2, =DBLOCK
GOTO    LDR R3, [R1], #4
		STR R3, [R2], #4
		SUBS R0, #1
		BNE GOTO
L	B L
SBLOCK DCD 0X11111111, 0X22222222, 0X33333333,0X44444444, 0X55555555
	AREA MYDATA, DATA, READWRITE
DBLOCK DCD 0
	END




		

;TW1A- ACCESS CONTENTS OF REGISTERS

	AREA MAIN, CODE, READONLY
		ENTRY
		MOV R0, #5
		MOV R1, #6
		ADD R2, R0, R1;
L	 B L
	END