#!/bin/bash

gcc -m32 -mpreferred-stack-boundary=2 -fno-stack-protector bof2.c -o /home/yuawn/challenges/pwn/bof2/home/bof2