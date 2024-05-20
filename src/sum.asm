; Add two numbers and store the results

; Clear registers
MOVE $0 $1
MOVE $0 $2
MOVE $0 $3

; Load numbers from memory
LW $0 $1 0
LW $0 $2 1

; Perform addition
ADD $1 $2 $3

; Store result back to memory
SW $0 $3 2

; Decrement the result and store again
DEC $3
SW $0 $3 3
