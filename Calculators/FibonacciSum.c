#include <stdio.h>

int fibonacci(int index) {
	int count = 0;
	int p1 = 0;
	int p2 = 1;
	int sum = 0;

	while(count < index) {
		sum += p2;
		int temp = p2;
		p2 = p1 + p2;
		p1 = temp;
		count++;
	}

	return sum;
}


int main() {
	int index;

	printf("Enter a number to calculate the sum of the Fibonacci sequence to that index: ");
	scanf("%d", &index);

	printf("\nSum: %d", fibonacci(index));

	return 0;
}
