#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <iostream>
#include <thread>
#include <windows.h>
#include <ctime>
using namespace std;

char map[10][10] = {{'.','.','.','.','.','.','.','.','.','.',},
            {'.','.','.','.','.','.','.','.','.','.',},
            {'.','.','.','.','.','.','.','.','.','.',},
            {'.','.','.','.','.','.','.','.','.','.',},
            {'.','.','.','.','.','.','.','.','.','.',},
            {'.','.','.','.','.','.','.','.','.','.',},
            {'.','.','.','.','.','.','.','.','.','.',},
            {'.','.','.','.','.','.','.','.','.','.',},
            {'.','.','.','.','.','.','.','.','.','.',},
            {'M','.','.','.','.','.','.','.','.','.',}};

int Mposition = 0;
int bananaCount = 0;

void task1(clock_t start) {
    while ((clock() - start)/(double) CLOCKS_PER_SEC <= 30) {
        char key = _getch();
        if (key == 'a' && Mposition != 0) {
            map[9][Mposition-1] = 'M';
            map[9][Mposition] = '.';
            Mposition--;
        } else if (key == 'd' && Mposition != 9) {
            map[9][Mposition+1] = 'M';
            map[9][Mposition] = '.';
            Mposition++;
        }
    }
}
void task2(clock_t start) {
    char type[] = {'/', '/', '/', '/', 'O'};
    srand(time(NULL));
    while ((clock() - start)/(double) CLOCKS_PER_SEC <= 30) {
        int randPos = rand()%10;
        int randType = rand()%5;
        char newRow[] = {'.','.','.','.','.','.','.','.','.','.'};
        newRow[randPos] = type[randType];
        
        if(map[8][Mposition] == '/')
            bananaCount++;
        else if (map[8][Mposition] == 'O')
            bananaCount = 0;
        
        for (int i = 8; i>0; i--) {
            memcpy(map[i], map[i-1], sizeof(map[i-1]));
        }
        memcpy(map[0], newRow, sizeof(newRow));
        Sleep(250);
    }
}
int main() {
    COORD coord;
	coord.X = 0;
	coord.Y = 1;
    system("cls");
    clock_t start = clock();
    thread t1(task1, start);
    thread t2(task2, start);
    while ((clock() - start)/(double) CLOCKS_PER_SEC <= 30) {
        SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
        for (int i = 0; i < 10; i++) {
            for (int j=0; j<10; j++) {
                printf("%c", map[i][j]);
            }
            printf("\n");
        }
        printf("You scored: %d points\n", bananaCount);
        int time = 30 - (clock() - start)/(double) CLOCKS_PER_SEC;
        printf("Time left: %2d\n", time);
        printf("Press a to move left and d to move right\n");
        printf("Get the banana (/) to earn scores\n");
        printf("Avoid the bomb (O) or you will lose all your scores\n");
    }
    t1.join();
    t2.join();
    return 0;
}