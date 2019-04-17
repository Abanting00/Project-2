#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
	int TOTAL = 10;
	int child = -1;
	int status;

	char *param1[] = {"python3", "sort.py", NULL};
	char *param2[] = {"cp","original.dat.txt","datafile.dat.txt",NULL};

	for(int i = 0; i < TOTAL && child != 0; i++){
		child = fork();

		if(child == 0){
			execvp(param1[0],&param1[0]);
		}else{
			wait(&status);

			child = fork();
			if(child == 0){
				execvp(param2[0],&param2[0]);
			}
			wait(&status);
		}

	}

	return 0;
}