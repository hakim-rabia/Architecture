; Calculate the Greatest Common Divisor (GCD) of two numbers

; Load numbers
LW $0 $a0 0
LW $0 $a1 1

; Initialize
MOVE $0 $v0

@LoopBegin
BEQ $a1 $0 @LoopEnd

; Division
DIV $a0 $a1 $t0 
MOVE $a0 $a1
MOVE $a1 $v0

J @LoopBegin
@LoopEnd

; Store result
SW $0 $a0 2

J @End

@End
