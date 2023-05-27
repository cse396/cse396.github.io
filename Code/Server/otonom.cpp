#include <Python.h>
#include <stdio.h>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <unistd.h>
#include <sys/wait.h>
#include <pthread.h>

using namespace std;

void* func1(void*);
void* func2(void*);
void callforward();

int main(int argc, char* argv[])
{
	
		//int yön 1
		
		pthread_t thread1 , thread2;
		
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
		int distance = 10;
		//char temp = "\n";
		//wait(NULL);
		int pid = fork();
		if (pid == 0){
			system("sudo python Control.py");
			}
		else{
			wait(NULL);
		while(distance  >= 15){
		
				ifstream inFile;
				inFile.open("distance.txt");
				inFile >> distance;
				sleep(0.5);
				inFile.close();
			
		}			
			
		}

			
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

void callforward(){
		
	Py_Initialize();
	PyObject* pModule = nullptr;
	PyObject* pFunc = nullptr;

	
    // Import the 'test' module
    pModule = PyImport_ImportModule("Control");
    if (pModule == nullptr) {
        PyErr_Print();
        return;
    }

    // Get a reference to the 'test_Ultrasonic_otonom' function
    pFunc = PyObject_GetAttrString(pModule, "call_forward");
    if (pFunc == nullptr || !PyCallable_Check(pFunc)) {
		if(PyErr_Occurred() ) {
			PyErr_Print();
		}
        
        return;
    }

    // Create arguments for the function call
    PyObject* pArgs = PyTuple_New(0);


    // Call the function with arguments
    PyObject* pResult = PyObject_CallObject(pFunc, pArgs);
    
    if (pResult == nullptr) {
		PyErr_Print();
        return;
    }

    // Cleanup
    Py_DECREF(pResult);
    Py_DECREF(pArgs);
    Py_DECREF(pFunc);
    Py_DECREF(pModule);


    Py_Finalize();
}
