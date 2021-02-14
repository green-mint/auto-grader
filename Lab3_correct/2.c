// Syed Asadullah Kashif (CMS: 333516) BSCS 10B

#include <stdio.h>

int main()
{
    float num1, num2, num3;

    printf("Input three different integers: ");
    scanf("%f %f %f", &num1, &num2, &num3);

    float sum = num1 + num2 + num3;

    printf("Sum is %f\n", sum);
    printf("Average is %f\n", sum / 3);
    printf("Product is %f\n", num1 * num2 * num3);

    return 0;
}
