#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include <fcntl.h>

char name[70];

int main(){

    int (*yuawn)() = (int(*)())name;

    puts("Give me your shellcode:");
    fflush(stdout);
    
    scanf("%s" , name);

    yuawn();

    return 0;
}