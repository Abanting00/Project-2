#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
	int total = 10;
	int child = -1;
	int status;

	printf("How many times do we run the test? ");
	scanf("%d", &total);

	char *param1[] = {"python3", "sort.py", NULL};
	char *param2[] = {"wc","-w","wrong.txt",NULL};

	for(int i = 0; i < total && child != 0; i++){
		child = fork();

		if(child == 0){
			execvp(param1[0],&param1[0]);
			printf("ERROR on EXECVP");
		}else{
			wait(&status);
			// Added a sleep function for readability
			sleep(.01);
		}

	}

	if( access("wrong.txt", F_OK ) != -1 ) {
    	child = fork();

    	if(child == 0){
			printf("------\nTotal Number of Errors\n");
    		execvp(param2[0], &param2[0]);
    		printf("ERROR on EXECVP\n");
    	}
    	wait(&status);
	} else {
	   	printf("------\nPassed All the Tests\n");
	}

	return 0;
}
