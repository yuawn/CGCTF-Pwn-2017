#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

void you_cant_see_me(){
    int magic = 1;
    system("echo Oh no~~~~~~~");
    if( magic ) return;
    system("sh");
}

int main(){
    char buf[20];
    puts( "Welcome to CGCTF 2017" );
    fflush(stdout);
    read( 0 , buf , 0x20 );

    return 0;
}