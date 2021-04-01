flag_checker:
        push    rbp
        mov     rbp, rsp
        mov     DWORD PTR [rbp-4], edi
        xor     DWORD PTR [rbp-4], 133337
        sar     DWORD PTR [rbp-4], 3
        add     DWORD PTR [rbp-4], 1337
        sub     DWORD PTR [rbp-4], 137
        mov     edx, DWORD PTR [rbp-4]
        mov     eax, edx
        add     eax, eax
        add     eax, edx
        mov     DWORD PTR [rbp-4], eax
        cmp     DWORD PTR [rbp-4], 1128648
        jne     .L2
        mov     eax, 1
        jmp     .L3
.L2:
        mov     eax, 0
.L3:
        pop     rbp
        ret
.LC0:
        .string "Enter the secret number: "
.LC1:
        .string "%d"
.LC2:
        .string "Correct number :D"
.LC3:
        .string "Wrong number :p"
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     edi, OFFSET FLAT:.LC0
        mov     eax, 0
        call    printf
        mov     eax, DWORD PTR [rbp-4]
        mov     esi, eax
        mov     edi, OFFSET FLAT:.LC1
        mov     eax, 0
        call    __isoc99_scanf
        mov     eax, DWORD PTR [rbp-4]
        mov     edi, eax
        call    flag_checker
        mov     DWORD PTR [rbp-8], eax
        cmp     DWORD PTR [rbp-8], 0
        je      .L5
        mov     edi, OFFSET FLAT:.LC2
        call    puts
        jmp     .L6
.L5:
        mov     edi, OFFSET FLAT:.LC3
        call    puts
.L6:
        mov     eax, 0
        leave
        ret