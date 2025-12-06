#include<stdio.h>
int main(){

  for (int i=1; i<=6;i++){

    for (int k=1;k<=i;k++){    // this code blocks print spaces in increasing orders columns
      printf(" "); 
      
    }
    for (int j=6;j>=i;j--)  // this code blocks print stars in decreasing orders columns
      {
        printf(" *");
      }


    printf("\n");  // this prints rows lines
    
  }

}

/*
output

Inverted full pyramid
----------------------------
  * * * * * *
   * * * * *
    * * * *
     * * *
      * *
       *

*/