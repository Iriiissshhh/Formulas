#include <math.h>
#include <stdio.h>
int main()
{
    int a;
    int b;
    int c;
    float area;
    printf("Enter value of a:");
    scanf("%d", &a);
    printf("Enter value of b:");
    scanf("%d", &b);
    printf("Enter value of c:");
    scanf("%d", &c);
    area = 0.5 * (a + b) * c;
    printf("Area of trapezium: %f\n", area);
    return 0;
}