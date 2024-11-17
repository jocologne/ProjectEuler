
//Find the sum of all the multiples of 3 or 5 below 1000.

#include <stdio.h>

int main (void)
{
	unsigned int result;
	unsigned int n;

	n = 1;
	result = 0;
	while (n < 1000)
	{
		if (n % 3 == 0 || n % 5 == 0)
			result += n;
		n++;
	}
	printf("RESULT=%d\n", result);
}
