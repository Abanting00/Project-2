#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
	int TOTAL = 200;
	int child = -1;
	int status;

	char *param1[] = {"python3", "sort.py", NULL};

	for(int i = 0; i < TOTAL && child != 0; i++){
		child = fork();

		if(child == 0){
			printf("i:%d Child\n",i);
			execvp(param1[0],&param1[0]);
			return 0;
		}else{
			printf("i: %d Parent\n",i);
			wait(&status);
		}

	}

	return 0;
}
