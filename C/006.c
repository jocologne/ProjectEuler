
/*Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum*/

#include <stdio.h>

int main(void)
{
	long long sumofsquares = 0;
	long long sum = 0;
	int lim = 100;
	int i = 1;

	while (i <= lim)
	{
		sumofsquares += (i * i);
		i++;
	}
	i = 1;
	while (i <= lim)
	{
		sum += i;
		i++;
	}
	long long result = (sum * sum) - sumofsquares;
	printf("%lld", result);
}