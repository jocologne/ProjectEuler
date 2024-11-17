
/*Find the sum of the even-valued terms of  Fibonacci 
sequence whose values do not exceed four million*/

#include <stdio.h>

int main (void)
{
	unsigned int result;
	unsigned int temp;
	unsigned int a = 1;
	unsigned int b = 2;

	result = 2;
	while ((a + b) < 4000000)
	{
		if ((a + b) % 2 == 0)
			result += (a + b);
		temp = b;
		b = (a + b);
		a = temp; 
	}
	printf("RESULT= %i\n", result);
}
