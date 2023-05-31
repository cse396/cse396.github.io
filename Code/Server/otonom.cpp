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

/*
 * for i in range(4):
            p[i][0]=(p[i][0]-self.point[i][0])/50
            p[i][1]=(p[i][1]-self.point[i][1])/50
            p[i][2]=(p[i][2]-self.point[i][2])/50
        for j in range(50):
            for i in range(4):
                self.point[i][0]+=p[i][0]
                self.point[i][1]+=p[i][1]
                self.point[i][2]+=p[i][2]
 * */

void* func1(void*);
void* func2(void*);

int main(int argc, char* argv[])
{	
	pthread_t thread1 , thread2;
	int check = mkfifo(write_path,0666);
	pthread_create(&thread1, NULL , func1 , NULL);
	pthread_create(&thread2, NULL , func2 , NULL);

	pthread_join(thread1 , NULL);
	pthread_join(thread2 , NULL);

	//sağa/sola dön
	//10 adım
	//sağa döndüyse dola,sola döndüyse sağa
	//eğer engel yoksa devam
	//engel varsa ilk döndüğü tarafa 
	//10 adım içinde engele rastlarsa
	//180 derece ters tarafa
	//aynı işlemleri diğer yöne yapcak
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
