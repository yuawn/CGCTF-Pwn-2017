#!/bin/bash

gcc -m32 -mpreferred-stack-boundary=2 -fno-stack-protector luck.c -o ./home/luck