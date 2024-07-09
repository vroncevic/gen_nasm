;
; @brief   full_simple
; @version 1.0.2
; @date    2024-07-09
; @company None, free software to use 2024
; @author  Vladimir Roncevic <elektron.ronca@gmail.com>
;

; Constant for marking std out operation
%define STDOUT 1

; Constants for marking syscall ids
%define SYS_WRITE 1
%define SYS_EXIT  60

section .data
    msg db "Hello, World", 10, 0 ; 10 - represents new line '\n', 0 - end
    len dq 13                    ; Length of message

section .text
    global _start

_start:
    ; syscall request service from kernel (write to stdout)
    mov rax, SYS_WRITE   ; Syscall id for write
    ; ----------------------------------------------------------------------
    mov rdi, STDOUT      ; Prepared stdout file descriptor
    mov rsi, msg         ; Address of message
    mov rdx, qword [len] ; Count of bytes
    syscall

    ; syscall request service from kernel (exit from program)
    mov rax, SYS_EXIT ; Syscall id for exit
    ; ----------------------------------------------------------------------
    xor rdi, rdi      ; Error code (0 marks there was no error)
    syscall

