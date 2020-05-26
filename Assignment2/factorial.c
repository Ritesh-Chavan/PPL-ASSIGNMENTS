#include<stdio.h>
#include<stdlib.h>

int factorial(int n){
	if(n == 0 || n == 1)
		return 1;
	else
		return n * factorial(n-1);
}


void main(){
	int n;
	printf("Enter a number.\n");
	scanf("%d", &n);
	printf("Factorial is %d.\n", factorial(n));


}

