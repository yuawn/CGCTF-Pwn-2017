#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>


int main(){
    puts( "Integer and String in memory." );
    fflush(stdout);

    int a;

    read( 0 , &a , 4 ); //read 4 byte to int a

    if( a == 878787 ) puts("CGCTF{Did_th4_little_ind1an_b0ther_y0u_87_?}"); // The flag.
    else puts("Bye~");

    return 0;
}