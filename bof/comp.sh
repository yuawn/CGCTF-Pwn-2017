#!/bin/bash

gcc -m32 -mpreferred-stack-boundary=2 -fno-stack-protector bof.c -o ./home/bof