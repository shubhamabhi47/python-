// #pyramid pattern of stars

// n = int(input("How many rows do you want in your pyramid? "))

// for i in range(1, n + 1):
//     # Printing spaces to center align the stars
//     print(" " * (n - i), end="")
//     # Printing stars
//     print("*" * (2 * i - 1))
// #include<stdio.h>

int main()
{
	int n;
	printf("Input the number of row:");
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		for (int blankspace = n - i; blankspace >= 0; blankspace--)
		{
			printf(" ");
		}
		for (int star = 1; star < 2 * i; star++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
