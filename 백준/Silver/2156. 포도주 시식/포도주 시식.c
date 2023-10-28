#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int max(int a, int b);
int main(void) {
	int numberofGlass;
	int drinkPrevious = 0, notdrinkPrevious = 0, restPrevious = 0;
	scanf("%d", &numberofGlass);
	for (int i = 0; i < numberofGlass; i++) {
		int drinkCurrent;
		int drinkNext, notdrinkNext, restNext;
		scanf("%d", &drinkCurrent);
		drinkNext = notdrinkPrevious + drinkCurrent;
		notdrinkNext = restPrevious + drinkCurrent;
		restNext = max(drinkPrevious, max(notdrinkPrevious, restPrevious));
		drinkPrevious = drinkNext;
		notdrinkPrevious = notdrinkNext;
		restPrevious = restNext;
	}
	printf("%d\n", max(drinkPrevious, max(notdrinkPrevious, restPrevious)));
	return 0;
}

int max(int a, int b) {
	if (a > b)
		return a;
	return b;
}