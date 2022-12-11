#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

char * arr[305];
int sizes[305];

int score(char c){
    if ('A' <= c && c <= 'Z'){
        return (int) c - 'A' + 27;
    } else{
        return (int) c - 'a' + 1;
    }
}

int findCommonInLine(int index){
    int size = sizes[index];
    for(int i = 0; i < size / 2; i++){
        for(int j = size / 2; j < size; j++){
            if(arr[index][i] == arr[index][j]){
                return score(arr[index][i]);
            }
        }
    }
    assert(0);
}

int findCommonBetween3Lines(int index){
    for(int i = 0; i < sizes[index]; i++)
        for(int j = 0; j < sizes[index + 1]; j++)
            for(int k = 0; k < sizes[index + 2]; k++)
                if(arr[index][i] == arr[index + 1][j] 
                && arr[index + 1][j] == arr[index + 2][k])
                    return score(arr[index][i]);
    assert(0);
}

int main(){

    int p1 = 0;
    int p2 = 0;
    char * line = NULL;
    size_t size = 0;
    int i;
    for(i = 0; getline(&line, &size, stdin) != -1; i++){
        size = strlen(line);
        arr[i] = (char *) malloc(size);
        sizes[i] = size;
        strcpy(arr[i], line);
    }
    free(line);
    
    for(int j = 0; j < i; j++)
        p1 += findCommonInLine(j);
    
    for(int j = 0; j < i; j+=3)
        p2 += findCommonBetween3Lines(j);
    
    for(int j = 0; j < i; j++)
        free(arr[i]);
    

    printf("%d\n", p1);
    printf("%d\n", p2); 

    return 0;
}