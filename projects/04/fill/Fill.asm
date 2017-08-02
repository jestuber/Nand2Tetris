// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
// screen is 256x512 pixels

// Put your code here.
	// initialze current state variable
	@ONOFF
	M = 0

(START)
	@KBD
	D = M // D = current key press
// Listen for non-zero keyboard code
	@BLACK
	D;JNE // if D != 0 goto BLACK
	@WHITE
	0;JMP // goto WHITE if no key is pressed

(BLACK)
	
	@ONOFF // check if already black
	D = M
	@START
	D;JLT // if @ONOFF is negative it's already black, no need to draw again

	@i
	M = 0			// i = 0
	@SCREEN
	D = A
	@address
	M = D			// address = 16384 (base address of the Hack screen)
	@ONOFF
	M = -1 // set ONOFF to black
	@LOOP
	0;JMP // goto LOOP

(WHITE)

	@ONOFF // check if already white
	D = M
	@START
	D;JEQ // if @ONOFF is 0 it's already black, no need to draw again

	@i
	M = 0			// i = 0
	@SCREEN
	D = A
	@address
	M = D			// address = 16384 (base address of the Hack screen)
	@ONOFF
	M = 0 // set ONOFF to white
	@LOOP
	0;JMP // goto LOOP

(LOOP)
   @i
   D = M
   @8191
   D = D - A
   @START
   D;JGT		// if i > n goto START

   @ONOFF
   D = M
   @address
   A = M		// writing to memory using a pointer
   M = D		// -1 for black, 0 for white
 
   @i
   M = M + 1	// i = i + 1
   @address
   M = M + 1	// address = address + 1
   @LOOP
   0;JMP		// goto LOOP