
/*the smallest positive number that is divisible by all of 
the numbers from 1 to 20*/

#include <stdio.h>

int main (void)
{
	long long num = 1;
	int i = 1;
	int r = 1;
	int limite = 20;

	while (r)
	{
		printf("%lld\n", num);
		i = 2;
		r = 0;
		while (i <= limite)
		{
			if (num % i != 0)
			{
				r = 1;
				break;
			}
			i++;
		}
		num++;
	}
}
