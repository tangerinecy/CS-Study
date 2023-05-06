# 힙 정렬
  
> ### 개념
**힙**이란?
-  완전이진트리 기반 자료구조
- 여러 개의 값들 중에서 가장 큰 값이나 가장 작은 값을 빠르게 찾아내도록 만들어진 자료구조
- key(부모노드) ≥ key(자식노드) 조건을 항상 성립
- 힙의 종류 
    - 최대 힙 (max heap)
    - 최소 힙 (min heap)
    ![image](https://user-images.githubusercontent.com/76865900/231247773-5f854038-d346-48d5-b49b-9b12d86e9094.png)


**힙정렬은?**
- 최대 힙이나 최소 힙의 특성을 활용하여 정렬하는 알고리즘
- 여기선 최대 힙을 기준으로 설명

> ### 기본 원리와 동작 예시
- 최대 힙을 구성
![image](https://user-images.githubusercontent.com/76865900/236623441-6fb96e39-2146-4e6a-993f-c4014c138e4f.png)
![image](https://user-images.githubusercontent.com/76865900/236623478-ab444dcf-2561-4987-b873-bdf1f8036b09.png)

- 최대 힙을 구성
- 현재 힙 루트는 가장 큰 값이 존재함. 루트를 힙의 마지막 원소와 교환, 힙의 사이즈 하나 줄임
- 힙의 사이즈가 1보다 크면 위 과정 반복
- 정렬된 원소를 제외하고 최대 힙에 원소가 1개 남으면 정렬을 종료한다.

> ### 소스 코드 (Python)
- 일반적인 방식
 ```python
array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

# 1. 상향식: 특정 노드를 기준으로 위로 올라감
def heap_sort(array):
    n = len(array)
    # heap 구성
    for i in range(n):
        c = i
        while c != 0:
            r = (c-1)//2
            if (array[r] < array[c]):
                array[r], array[c] = array[c], array[r]
            c = r
            print(array)
    # 크기를 줄여가면서 heap 구성
    for j in range(n-1, -1, -1):
        array[0] , array[j] = array[j], array[0]
        r = 0
        c = 1
        while c<j:
            c = 2*r +1
            # 자식 중 더 큰 값 찾기
            if (c<j-1) and (array[c] < array[c+1]):
                c += 1
            # 루트보다 자식이 크다면 교환
            if (c<j) and (array[r] < array[c]):
                array[r], array[c] = array[c], array[r]
            r=c
            print(array)
    print(array)
heap_sort(array)
``` 

> ### 성능 평가
- 시간 복잡도
    - **힙**의 데이터 저장 및 삭제 시간 복잡도 : O(logzN)
    - **힙 정렬**의 시간 복잡도 : O(Nlog2N) 
        - 정렬대상의 수가 n개라면, 총 n개의 데이터를 삽입 및 삭제해야 하므로 n을 곱해야함

> ### 장단점
- 장점 
    - 추가적인 배열이 필요하지 않다.( in-palce algorithm, 병합정렬보다 효율적 )
    - 항상 nlogn을 보장
    - 이론상 퀵,병합 정렬보다 우위에 있다.
    - max 또는 min 값을 구할 때 시간 복잡도는 O(1)이다.
- 단점 
    - 일반적으로 속도만 비교하자면 퀵이 평균적으로 더 빠르다. 그래서 잘 사용하지 않음.
 
### 시간 복잡도에서 로그 밑을 버리고 표기해도 되는 이유
---
- 컴퓨터가 이진수 시스템을 사용하기 때문에, 로그는 밑을 대부분 2로 사용함

### 출처
---
- 윤성우의 열혈 자료 구조
- https://good-potato.tistory.com/m/50
- https://seanpark11.tistory.com/68 (소스 코드 출처)
- https://gyoogle.dev/blog/algorithm/Heap%20Sort.html
### 그 외 추천 자료
- https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/
- https://deok2kim.tistory.com/178
