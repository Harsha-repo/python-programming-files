#include<stdio.h>
#include<stdlib.h>

int main(){


// int x = 8;
// int* ptr = NULL;
// printf("%p",ptr);
int *ptr = (int*) calloc(10,4);
// int *p = ptr;
ptr++;
free(ptr);


    return 0;
}