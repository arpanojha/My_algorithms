#include "stdio.h"
#include "stdlib.h"
#define row 10
//undirected unweighted graph on a sparse matrix

int print_connection(int k[row][row],int r){
  for(int i=0;i<r;i++){
    for(int j=0;j<r;j++)printf("%d\t",k[i][j]);
    printf("\n");
  }
  return 1;
}

/*error code :
   0 already conneted
   1 connetion made
   2 out of bounds
  */
int add_connection(int k[row][row],int *r,int i,int j){
  if(k[i][j]==1)return 0;
  if(i<*r &&j<*r&&i!=j){
    k[i][j]=1;
    k[j][i]=1;
    return 1;
  }
  else{
    return 2;
  }
  return 1;
}

int delete_connection(int k[row][row],int *r,int i,int j){
  if(k[i][j]==0)return 0;
  if(i<*r &&j<*r&&i!=j){
    k[i][j]=0;
    k[j][i]=0;
    return 1;
  }
  else{
    return 2;
  }
  return 1;
}

int initialize_k(int *r,int i, int j){
  if(*r>i&&*r>j)return 1;
  if(i>j)*r = i+1;
  else *r=j+1;
  printf("Value of r changed to %d ",*r);
  return 1;
}


int main(){
  static int k[row][row];
  int r = 0;
  int choice =0;
  int i,j;
//  memset(k.connector,0,100);
  while(1){
    printf("Enter choice\n");
    printf("1.Print connections\n");
    printf("2.Add connection\n");
    printf("3.Check connection\n");
    printf("4.Delete connection\n");
    printf("5.Exit\n");
    scanf("%d",&choice);
    if(choice > 4 || choice <0)break;
    switch(choice){
      case 1: print_connection(k,r);
              break;
      case 2: printf("\nEnter connections to be added ,current max value is 10:  ");
              scanf("%d %d",&i,&j);
              initialize_k(&r,i-1,j-1);
              add_connection(k,&r,i-1,j-1);
              break;
      case 3:printf("\nEnter nodes to check connection ,current max value is 10:  ");
             scanf("%d %d",&i,&j);
             printf("%d \n",k[i-1][j-1]);
             break;
      case 4:printf("\nEnter connections to be deleted ,current max value is 10:  ");
              scanf("%d %d",&i,&j);
              delete_connection(k,&r,i-1,j-1);
              break;
      default: printf("Illegal choice");
    }
  }
  return 0;
}
