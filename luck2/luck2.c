#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include <fcntl.h>


int main(){
    puts( "Revenge of luck :((((" );
    fflush(stdout);

    int magic = 0 , input = 0;
    
    magic = 0x12345678;

    read( 0 , &input , 0x10 ); // input your password

    if( input == 0xfaceb00c &&  magic == 0xdeadbeef) {

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