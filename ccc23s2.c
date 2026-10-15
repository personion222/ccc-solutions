#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int m;
	char buf[1024];

	fgets(buf, 1024, stdin);

	m = atoi(buf);

	printf("%d\n", m);
}
