#include <stdio.h>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <unistd.h>
#include <sys/wait.h>
#include <pthread.h>
#include <cstring>
#include <fcntl.h>
const char * write_path = "pythonfifo.txt";
using namespace std;
#define MAX_BUF 20

void* func1(void*);
void* func2(void*);

int main(int argc, char* argv[])
{
    pthread_t thread1 , thread2;

    pthread_create(&thread1, NULL , func1 , NULL);
    pthread_create(&thread2, NULL , func2 , NULL);

    pthread_join(thread1 , NULL);
    pthread_join(thread2 , NULL);

    return 0;
}


void* func1(void* arg)
{		
    system("python3 move.py");
	return NULL;
}

void* func2(void* arg)
{
    int fd;

    printf("Opened\n");
    fd = open(write_path, O_RDWR);
    printf("%d\n",fd);
    char buf[20] = "forward";
    write(fd, buf, strlen(buf));

    return NULL;
}
