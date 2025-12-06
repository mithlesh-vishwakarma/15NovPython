#include<stdio.h>
int main(){

int x,y;
printf("enter the values of x and y");
scanf("%d %d",&x,&y);

if(x>0 && y>0){
  printf("the first quaderant: ");
}else if(x>0 && y<0){
  printf("the fourth quaderant: ");
}else if(x<0 && y>0){
  printf("the second quaderant: ");
}else if(x<0 && y<0){
  printf("the third quaderant: ");
}else{
  printf("the point lies on the axis"); 
}
return 0;
}