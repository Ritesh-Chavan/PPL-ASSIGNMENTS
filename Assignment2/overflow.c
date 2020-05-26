#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void overflow(){
	printf("Hijacked\n");
} 


void function1(char *str){
	char buffer[5];
	strcpy(buffer, str);
}

void main(int  argc, char *argv[]){
	if(argc ==1){
		exit(0);
	}
	function1(argv[1]);
	printf("Everything Worked Fine.\n");

}



// gcc -g -fno-stack-protector -z execstack -o overflow overflow.c
// x/16xw $rsp
// x/1xw $rbp
//run $(perl -e 'print "A" x 13 . "\xca\x46\x55\x55\x55\x55\x00\x00"')
