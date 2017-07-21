#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include <fcntl.h>


int main(){
    puts( "Welcome to CGCTF 2017 :D" );
    fflush(stdout);

    int password = 0 , input = 0;

    unsigned seed;
    seed = (unsigned)time(NULL);
    srand(seed); // random with time seed

    password = random(); // random password
    read( 0 , &input , 0x10 ); // input your password

    if( input == password ) {
        puts( "WOW, Pwn with luck? If not, you are such a good hacker :)" );
        FILE *fd = fopen( "/home/luck/flag.txt" , "r" ); // open flag.txt file
        char flag[48];
        fread( flag , 1 , 48 , fd ); // read the content of flag.txt file into flag[48] buffer
        printf("Here is your flag: %s\n" , flag);
    }
    else{
        puts( "Bad Lucks :(" );
    }

    return 0;
}