
#include <stdio.h>

int main()
{
    // A constant indicating the value of pi
    const float pi = 3.14159;

    float radius = 0;

    printf("Enter the radius of the circle: ");
    scanf("%f", &radius);

    printf("Diameter of the cicle is %f\n", 2 * radius);
    printf("Circumference of the cicle is %f\n", 2 * pi * radius);
    printf("Area of the cicle is %f\n", pi * radius * radius);

    return 0;
}
