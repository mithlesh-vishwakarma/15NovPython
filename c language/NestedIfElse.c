#include<stdio.h>
int main()
{
    int math, physics, chemistry,total, subTotal;
    printf("Enter the value of math, physics and chemistry: ");
    scanf("%d %d %d", &math, &physics, &chemistry);

    // check if the marks are greater than or equal
    if (math >=60 && physics >= 55 && chemistry >= 50)
    {
        total = math + physics + chemistry;
        subTotal = math + physics;

        printf("Total marks: %d\n", total);
        printf("Subtotal marks (math + physics): %d\n", subTotal);

        // check if the student has passed
        if (total >= 180 && subTotal >= 140)
        {
            printf("The student has passed.\n");
        }
        else
        {
            printf("The student has failed.\n");
        }
    }
    else
    {
        printf("Invalid marks entered, failed not eligible\n");
    }
    

    return 0;

}