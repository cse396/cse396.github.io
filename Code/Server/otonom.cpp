#include <Python.h>
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
	system("sudo python Control.py");
	return NULL;
		
	return NULL;
}
void* func2(void* arg)
{
	const char* filename = "Ultrasonic.py";
	FILE* fp;

	Py_Initialize();

	fp = fopen(filename, "r");
	if(fp == NULL){
			perror("failed to open file \n");
			
	}

	PyRun_SimpleFileEx(fp , "Ultrasonic.py" , 1);

	Py_Finalize();
	return NULL;
}
