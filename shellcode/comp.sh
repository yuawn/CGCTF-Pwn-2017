#!/bin/bash

gcc -m32 -mpreferred-stack-boundary=2 -fno-stack-protector -z execstack shellcode.c -o /home/yuawn/challenges/pwn/shellcode/home/shellcode