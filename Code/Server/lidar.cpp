
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
void* func2(void*);
void* func3(void*);

int main(int argc, char* argv[])
{	
	pthread_t thread1 , thread2 , thread3;

	pthread_create(&thread1, NULL , func1 , NULL);
	pthread_create(&thread2, NULL , func2 , NULL);
	pthread_create(&thread3, NULL , func3 , NULL);

	pthread_join(thread1 , NULL);
	pthread_join(thread2 , NULL);
	pthread_join(thread3 , NULL);

	return 0;
}


void* func1(void* arg)
{		
	system("sudo python sonic.py");
	return NULL;
}
void* func2(void* arg)
{
	system("sudo python sonic2.py");
	return NULL;
}
void* func3(void* arg){
	system("sudo python lidar_servo.py");
	return NULL;
}
