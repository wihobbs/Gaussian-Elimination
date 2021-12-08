// Copyright 2021 William Hobbs
// Reduced Row Echelon Form program
// takes CLI of n, m, numbers
// returns n, m, numbers of the reduced matrix

#include <stdio.h>
#include <stdlib.h> // using atoi
#include <assert.h>

int main(int argc, char* argv[]) {
    assert(argc >= 2); // you need at least an n and m value, even if they are 0
    int n = atoi(argv[0]);
    int m = atoi(argv[1]);
    int matrix[n*m];
    for(int i = 2; i < argc; i++) {
        matrix[i-2] = atoi(argv[i]);
    }
}

int* rref(int n, int m, int* matrix[]) {
    int sol[n*m];
    return sol;
}