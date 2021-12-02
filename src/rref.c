// Copyright 2021 William Hobbs
// Reduced Row Echelon Form program

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    // Part One
    FILE* input = fopen("data.txt", "r");
    int count, i;
    while(!feof(input))
    {
        fscanf (input, "%d", &i);
        count++;
    }
    int numbers[count];
    i = 0;
    rewind(input);
    while(!feof(input))
    {
        fscanf(input, "%d", &numbers[i]);
        i++;
    }
    
    fclose(input);
    int count_of_less_than = 0;
    for (int i = 0; i < count; ++i)
    {
        if (numbers[i+1] > numbers[i]) {
            count_of_less_than++;
        }
    }
    printf("%d", count_of_less_than);
    // Part 1 answer: 1602
    // Part 2
    int sliding_window[count];
    for (int i = 0; i < count - 2; ++i) {
        sliding_window[i] = numbers[i+2] + numbers[i+1] + numbers[i];
    }
    printf("%d", sliding_window[2000]);
    count_of_less_than = 0;
    for (int i = 0; i < count - 2; ++i)
    {
        if (sliding_window[i+1] > sliding_window[i]) {
            count_of_less_than++;
        }
    }
    printf("%d", count_of_less_than);
    // Part 2 Answer: 1633
}