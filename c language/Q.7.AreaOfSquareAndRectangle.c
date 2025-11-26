#include<stdio.h>
#include<math.h>

int main(){
    float side, length, breadth;
    float areaOfSquare, areaOfRectangle;

    // Input for square
    printf("Enter the side of the square: \n");
    scanf("%f", &side);

    // Calculate area of square
    areaOfSquare = pow(side, 2);
    printf("Area of Square is: %f\n", areaOfSquare);

    // Input for rectangle
    printf("Enter the length and breadth of the rectangle: \n");
    scanf("%f %f", &length, &breadth);

    // Calculate area of rectangle
    areaOfRectangle = length * breadth;
    printf("Area of Rectangle is: %f\n", areaOfRectangle);

    return 0;



}