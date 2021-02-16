
#include <stdio.h>

int main()
{
    char character;
    printf("Input a letter, digit, or character: ");
    scanf("%c", &character);
    printf("%c's integer equivalent is %d\n\n", character, character);

    printf("%c's integer equivalent is %d\n", 'A', 'A');
    printf("%c's integer equivalent is %d\n", 'B', 'B');
    printf("%c's integer equivalent is %d\n", 'C', 'C');
    printf("%c's integer equivalent is %d\n", 'a', 'a');
    printf("%c's integer equivalent is %d\n", 'b', 'b');
    printf("%c's integer equivalent is %d\n", 'c', 'c');
    printf("%c's integer equivalent is %d\n", '0', '0');
    printf("%c's integer equivalent is %d\n", '1', '1');
    printf("%c's integer equivalent is %d\n", '2', '2');
    printf("%c's integer equivalent is %d\n", '$', '$');
    printf("%c's integer equivalent is %d\n", '*', '*');
    printf("%c's integer equivalent is %d\n", '+', '+');
    printf("%c's integer equivalent is %d\n", '/', '/');
    printf("%c's integer equivalent is %d\n", ' ', ' ');

    return 0;
}
