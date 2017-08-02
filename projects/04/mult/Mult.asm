// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// while (R1 >= 0) add R0 to R2, R1--
	@R2
	M=0 // R2=0
(LOOP)
	@R1
	D=M // D=R1
	@END
	D;JLE // if R1<=0 goto end
	@R0
	D=M // D=R0
	@R2
	M=D+M // R2=R0+R2
	@R1
	M=M-1 // i--
	@LOOP
	0;JMP

// End program with endless loop
(END)
	@END
	0;JMP