#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - holberton function
 * Return: 0
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
/**
 * main - main function
 * Return: 0
 */
int main(void)
{
    pid_t hijo;
	int i= 1;

	while(i < 6)
	{
		hijo = fork();
        if (hijo > 0)
        {
            printf("Zombie process created, PID: %u\n", hijo);
        }
        
        i++;
	}
	infinite_while();
	return (0);
}