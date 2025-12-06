#include<stdio.h>
int main(){

  for (int i=1; i<=5;i++){

    for (int j=5;j>=i;j--){   // here column is in decreasing order
      printf(" *");  // for print the star on columns with spaces
    }
    printf("\n");  // for change the rows
    
  }

}

/*
output

INverted Right half pyramid
----------------------------
 * * * * *
 * * * *
 * * *
 * *
 *

*/