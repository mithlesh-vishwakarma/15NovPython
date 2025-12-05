#include<stdio.h>
int main()
{
int i,j;
for(i=1;i<=9;i++){
  for(j=1;j<=9;j++){
    if(i==5 || j==5 ){
    printf("*");
    }else if(i==9 && j<=5){
      printf("*");
    }else if(i==1 && j>=5) {
      printf("*");
    }else if(j==9 && i>=5){
      printf("*");
    }else if(j==1 && i<=5){
      printf("*");
    }else
    {
      printf(" ");
    }

    printf(" ");
  }

  printf("\n");
  }


  

return 0;
}





/*output 


  1 2 3 4 5 6 7 8 9
1 *       * * * * *
2 *       * 
3 *       *
4 *       *
5 * * * * * * * * * 
6         *       *
7         *       *
8         *       *
9 * * * * *       *




*/