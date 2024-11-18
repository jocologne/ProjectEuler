#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int m_sqrt(int n)
{
	int i = 1;
	while (i * i <= n)
	{
		if (i * i == n)
			return i;
		i++;
	}
	return (0);
}

int hip(int a, int b)
{
	int resp = (a * a) + (b * b);
	return (m_sqrt(resp));
}

int main(void)
{
	int n = 1000;
	int lim = 500;
	int a = 1;
	int c;
	int per;
	int *arr = (int*) calloc(n, sizeof(int));
	while (a < lim)
	{
		int b = a;
		while (b < lim)
		{
			c = hip(a, b);
			if (c)
			{
				printf("%d_%d_%d\n", a, b, c);
				per = (a + b + c);
				if (per < n)
					arr[per]++;
			}
			b++;
		}
		a++;
	}
	int i = 0;
	int max = 0;
	int resp = 0; 
	while (i < n)
	{
		if (arr[i] > max)
		{
			max = arr[i];
			resp = i;
		}
		i++;
	}
	printf("Perimetro %d aparece %d vezes.\n", resp, max);
	free(arr);
	return 0;
}
