#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include <fcntl.h>

char code[70];

int main(){

    int (*yuawn)() = (int(*)())code;

    puts("Give me your shellcode:");
    fflush(stdout);
    
    read( 0 , code , 70 );

    yuawn();

    return 0;
}