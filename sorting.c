#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void swap(int *p,int *q)
{
     int temp;
     temp = *p;
     *p = *q;
     *q = temp;

}

 void selection_sort(int arr[],int n){

      int min_idx;

      for(int i=0;i<n-1;i++){
          min_idx=i;
          for(int j=1+i;j<n;j++){
            if(arr[j]<arr[min_idx]){
               min_idx=j;
               swap(&arr[min_idx],&arr[i]);
            }
          }
      }
      for(int i=0;i<n;i++){
         printf("%d ",arr[i]);
    }
    printf("\n");

 }

void bubble(int arr[],int n){
     for(int i=0;i<n;i++){
         for(int j=0;j<n-i;j++){
             if(arr[j]>arr[j+1]){
                swap(&arr[j],&arr[j+1]);
             }
         }
     }
     for(int i=0;i<n;i++){
         printf("%d ",arr[i]);
    }
    printf("\n");
}

void insertion(int arr[],int n){
     for(int i=1;i<n;i++){
         int temp = arr[i];
         int j = i-1;
       if(j>=0){
         while(arr[j] > temp)
          swap(&arr[j],&temp);
          j--;
        }
     
     }
   for(int i=0;i<n;i++){
         printf("%d ",arr[i]);
    }  
 printf("\n");
}


// void merge(int *a,int *b,int *s,int n,int m){
//      int k=0;
     
//      for(int i=0;i< n;i++){
//         for(int j=0;j< m;j++){
//             if(a[i]>b[j]){
//               s[k]=b[j];
//               k++;
//               j++;
             
//             }
            
//              if(a[i]>b[j]){
//               s[k]=a[i];
//               k++;
//               i++;
           
//             }         
//         }
//      }
// }

// void mergesort(int *a,int size){
//      int*s;
//      s = (int *)malloc(size*sizeof(int));
//      if(size<=1){
//      int m;
//      m=size/2;
//      mergesort(a,m);
//      mergesort(a+m,size -m);
//      merge(a,a+m,s,m,size-m);
//      }
//       for(int i=0;i<size;i++){
//          printf("%d ",s[i]);
//     }  
//  printf("\n");
// }

int main(){
    int n;  
    scanf("%d",&n);
    int a[n];
    for(int i=0;i<n;i++){
       scanf("%d",&a[i]);   
    }
 
 bubble(a,n);
 insertion(a,n);
//  mergesort(a,n);
 selection_sort(a,n);
return 0;
}
