
#include <stdio.h>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <pthread.h>
#include <string>
#include <fcntl.h>

using namespace std;

void* func1(void*);

int main(int argc, char* argv[])
{	
	pthread_t thread1;

	pthread_create(&thread1, NULL , func1 , NULL);
	pthread_join(thread1 , NULL);
	kill(getpid(), -9);
	
	return 0;
}

void* func1(void* arg)
{		
	system("sudo python main.py");
	return NULL;
}
