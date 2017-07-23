#!/bin/bash

gcc -m32 -mpreferred-stack-boundary=2 -fno-stack-protector bof3.c -o /home/yuawn/challenges/pwn/bof3/home/bof3