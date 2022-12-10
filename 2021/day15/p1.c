#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct state {
    int i;
    int j;
    int cost;
    struct state *next;
} state;

typedef struct queue {
    struct state *head;
    struct state *tail;
} queue;

typedef struct pair {
    int first;
    int second;
} pair;


void push(queue *q, int i, int j, int cost){
    state *s = (state*) malloc(sizeof(state));
    s->i = i;
    s->j = j;
    s->cost = cost;
    s->next = NULL;
    if (q->tail != NULL){
        q->tail->next = s;
    }
    q->tail = s;
    if (q->head == NULL){
        q->head = s;
    }
}

void init(queue *q){
    q->head = NULL;
    q->tail = NULL;
}

state* pop(queue *q){
    state *s = (state*) malloc(sizeof(state));
    if (q->head == NULL){
        return NULL;
    }
    s = q->head;
    if(q->head->next != NULL){
        q->head = q->head->next;
    } else{
        q->head = NULL;
        q->tail = NULL;
    }
    return s;
}

int main(){
    int dim = 100;

    int graph[dim][dim];
    int cost[dim][dim];

    FILE *file = fopen("input.in", "r");

    char line[dim+2];
    
    int rowIndex = 0;
    while( fgets( line, dim+2, file) != NULL){
        for(int i = 0; i < dim; i++){
            graph[rowIndex][i] = (int) line[i] - '0';
            cost[rowIndex][i] = INT_MAX;
        }
        rowIndex++;
    }   
    fclose(file);
    
    queue *q = (queue*) malloc(sizeof(queue));
    init(q);
    push(q, 0, 0, 0);
    
    while (1){
        state *s = pop(q);
        if (s == NULL){
            break;
        }
        int i = s->i;
        int j = s->j;
        int c = s->cost;
        if (cost[i][j] <= c){
            continue;
        }
        cost[i][j] = c;
        pair *neighbours = (pair*) malloc(sizeof(pair) * 4); 
        neighbours->first = i+1;
        neighbours->second = j;
        (neighbours+1)->first = i-1;
        (neighbours+1)->second = j;
        (neighbours+2)->first = i;
        (neighbours+2)->second = j+1;
        (neighbours+3)->first = i;
        (neighbours+3)->second = j-1;
        for (int k = 0; k < 4; k++){
            pair *p = (neighbours + k);
            int ii = p->first;
            int jj = p->second;
            if (0 <= ii && ii < dim && 0 <= jj && jj < dim){
                push(q, ii, jj, c + graph[i][j]);
            }
        }
        free(neighbours);
    }
    free(q);
    printf("%d\n", cost[dim - 1][dim - 1] - (graph[0][0] - graph[dim - 1][dim - 1]));
    return 0;
}