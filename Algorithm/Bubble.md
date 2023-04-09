###버블 정렬 알고리즘 개념  

서로 인접한 두 원소를 검사하여 정렬하는 알고리즘  
인접한 2개의 원소를 비교하여 크기가 순서대로 정렬되어있지 않으면 서로 교환한다.  
이러한 과정을 첫 번째부터 마지막까지 수행하는 것이 1회전  
  
1회전 수행 후: 가장 큰 자료가 맨 뒤로 이동하므로 2회전에서는 맨 끝에 있는 자료는 정렬에서 제외됨   
2회전 수행 후: 끝에서 두 번째 자료까지는 정렬에서 제외됨  
이와 같이 정렬을 1회전 수행할 때마다 정렬에서 제외되는 데이터가 하나씩 늘어난다.   

###버블 정렬(bubble sort) 알고리즘의 특징  
장점  
구현이 매우 간단하다.  
단점  
요소가 가장 왼쪽에서 가장 오른쪽으로 이동하기 위해서는 모든 다른 요소들과 교환되어야 한다.  
특히 특정 요소가 이미 최종 정렬 위치에 있더라도 교환이 일어난다.  
일반적으로 자료의 교환 작업(SWAP)이 자료의 이동 작업(MOVE)보다 더 복잡하기 때문에 버블 정렬은 거의 쓰이지 않는다.  

###버블 정렬(bubble sort)의 시간복잡도
최상, 평균, 최악 모두 일정  
n-1, n-2, … , 2, 1 번 = n(n-1)/2  
교환 횟수  
입력 자료가 역순으로 정렬되어 있는 최악의 경우, 한 번 교환하기 위하여 3번의 이동(SWAP 함수의 작업)이 필요하므로 (비교 횟수 * 3) 번 = 3n(n-1)/2  
입력 자료가 이미 정렬되어 있는 최상의 경우, 자료의 이동이 발생하지 않는다.  
T(n) = O(n^2)  

###코드
```# include <stdio.h>
# define MAX_SIZE 5

// 버블 정렬
void bubble_sort(int list[], int n){
  int i, j, temp;

  for(i=n-1; i>0; i--){
    // 0 ~ (i-1)까지 반복
    for(j=0; j<i; j++){
      // j번째와 j+1번째의 요소가 크기 순이 아니면 교환
      if(list[j]<list[j+1]){
        temp = list[j];
        list[j] = list[j+1];
        list[j+1] = temp;
      }
    }
  }
}

void main(){
  int i;
  int n = MAX_SIZE;
  int list[n] = {7, 4, 5, 1, 3};

  // 버블 정렬 수행
  bubble_sort(list, n);

  // 정렬 결과 출력
  for(i=0; i<n; i++){
    printf("%d\n", list[i]);
  }
}
```


###관련 영상
[https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html](https://www.youtube.com/watch?v=fxuhgRRqYsY)  
  
https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html    
