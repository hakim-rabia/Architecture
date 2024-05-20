; Recursive Fibonacci
; Computes the nth Fibonacci number where n is stored at the first memory address
; Result is stored back at the second memory address

; Load n
LW $0 $a0 0

; Call recursive Fibonacci function
JAL @fibonacci

; Store result
SW $0 $v0 1

J @End

; Recursive Fibonacci function
@fibonacci
    ; Base case: if n < 2, return n
    SLTI $a0 $a1 2
    BEQ $a0 $0 @recursive_case

    JR $ra

@recursive_case
    ; Recursive case: fib(n-1) + fib(n-2)
    ; Calculate fib(n-1)
    ADDI $a0 $a0 -1
    JAL @fibonacci
    MOVE $v1 $v0

    ; Calculate fib(n-2)
    ADDI $a0 $a0 -1
    JAL @fibonacci
    ADD $v0 $v1 $v0

    JR $ra

@End
