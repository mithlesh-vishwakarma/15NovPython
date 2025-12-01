//Write a program to display traffic light meaning (red, yellow, green) using switch. 

#include<stdio.h>
int main(){
    char trafficLight;
    
    printf("Enter traffic light color (R,r for Red, Y,y for Yellow, G,g for Green): ");
    scanf(" %c", &trafficLight);
    
    switch(trafficLight){
        case 'R':
        case 'r':
            printf("Stop! The light is Red.\n");
            break;
        case 'Y':
        case 'y':
            printf("Caution! The light is Yellow.\n");
            break;
        case 'G':
        case 'g':
            printf("Go! The light is Green.\n");
            break;
        default:
            printf("Invalid input! Please enter R, Y, or G.\n");
    }
    
    return 0;
}