/*Write a program to check whether a character is an alphabet, digit or special
character using else-if ladder.*/

#include<stdio.h>
int main(){
char character;

printf("please enter a character:");
scanf("%c",&character);

if(character>='A'&& character<='Z' || character>='a' && character<='z'){
  printf("the character is albhabet");
}else if(character>='0' && character<='9'){
  printf(" the character is digit");
}else {
  printf("the character is special character");
}
return 0;
}