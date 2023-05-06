# 합병 정렬(Merge Sort)
  
> ### 개념
- 분할 (divide) : 하나의 배열을 같은 크기로 나눔
- 정복 (conquer) : 나뉜 배열들을 정렬
- 결합 (combine) : 다시 하나의 배열로 합치기

> ### 기본 원리
- 8개의 데이터를 동시에 정렬하는 것보다, 이를 둘로 나누어 4개의 데이터를 정렬하는 것이 쉽고, 이들 각각을 다시 한번 둘로 나누어 2개의 데이터를 정렬하는 것이 더 쉽다

![image](https://user-images.githubusercontent.com/76865900/230872411-3d29f95d-d71e-4443-bcce-36400c6959ed.png)

    - 실제로는 더 작게 분할해야 함
    - 데이터가 1개만 남을 때까지 분할 반복
    - 데이터가 2개만 남아도 if문 하나로 간단히 정렬할 수 있지만 데이터가 1개 남으면 그조차도 불필요해지기 때문
- 분할 과정(재귀) / 병합 과정(정렬)
![image](https://user-images.githubusercontent.com/76865900/230872955-c4202b92-85dc-4ae1-83f8-d354da2bccf9.png) 

> ### 소스 코드
- 파이썬의 리스트 slice notation(arr[start:end]) 사용
    - 리스트 slice 시 배열의 복제가 일어나므로 메모리 사용 효율 떨어짐
 ```python
def merge_sort(arr): 
    if len(arr) < 2: # 배열 요소 1개인 경우
        return arr # 정렬 과정 불필요

    mid = len(arr) // 2 # 분할
    low_arr = merge_sort(arr[:mid]) # 왼쪽 리스트
    high_arr = merge_sort(arr[mid:]) # 오른쪽 리스트

    merged_arr = [] # 정렬된 결과 저장 리스트
    l = h = 0 # 각각 분할된 왼쪽/오른쪽 리스트 가리킴
    while l < len(low_arr) and h < len(high_arr): #각 리스트 범위 넘어서지 않는 선에서 비교 수행
        if low_arr[l] < high_arr[h]: # 왼쪽 리스트 값이 오른쪽 리스트 값보다 작을 경우
            merged_arr.append(low_arr[l]) #결과 리스트에 정렬 업데이트
            l += 1 #왼쪽 리스트에서 다음 값 가리킴
        else: # 오른쪽 리스트 값이 크거나 같은 경우 (같은 경우도 if / else 둘 중 한 곳에 포함되어야 함)
            merged_arr.append(high_arr[h]) #결과 리스트에 정렬 업데이트
            h += 1 #오른쪽 리스트에서 다음 값 가리킴
    merged_arr += low_arr[l:] #결과 리스트에 while문에서 비교 수행하지 않은 왼쪽 리스트 나머지 값 업데이트
    merged_arr += high_arr[h:] #결과 리스트에 while문에서 비교 수행하지 않은 오른쪽 리스트 나머지 값 업데이트
    return merged_arr
``` 
- 메모리 최적화 버전
    - 새로운 배열을 매번 생성해서 리턴하지 않고, 인덱스 접근을 이용해 입력 배열을 계속해서 업데이트하면 메모리 사용량 줄일 수 있음 (In-place sort)
 ```python
def merge_sort(arr):
    def sort(low, high): # 분할 과정 (재귀)
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high): # 합병 과정
        temp = [] #정렬된 결과 리스트
        l, h = low, mid

        while l < mid and h < high: # l: 왼쪽 리스트 가리킴 / h: 오른쪽 리스트 가리킴
            if arr[l] < arr[h]: # 왼쪽 요소가 오른쪽 요소보다 작으면
                temp.append(arr[l]) #결과 리스트에 추가
                l += 1 #왼쪽 리스트에서 다음값 가리킴
            else: # 오른쪽 요소가 왼쪽 요소보다 크거나 같으면
                temp.append(arr[h]) #결과 리스트에 추가
                h += 1 #오른쪽 리스트에서 다음값 가리킴

        while l < mid: #왼쪽 리스트 값이 결과 리스트에 모두 업데이트되지 못했다면
            temp.append(arr[l]) #결과 리스트에 추가
            l += 1 
        while h < high: # 위와 동일한 오른쪽 리스트 업데이트 과정
            temp.append(arr[h])
            h += 1

        for i in range(low, high): #배열의 처음~끝
            arr[i] = temp[i - low] # arr 현재 정렬된 리스트 정보로 업데이트 

    return sort(0, len(arr))
```

> ### 성능 평가
- 시간 복잡도
    - 최선의 경우 : O(nlog₂n)
    - 최악의 경우 : O(nlog₂n)
- 시간복잡도 증명 과정  
    코드 中
```python
 while l < len(low_arr) and h < len(high_arr): 
        if low_arr[l] < high_arr[h]: # 핵심이 되는 비교 연산
            merged_arr.append(low_arr[l]) 
            l += 1 
        else: 
            merged_arr.append(high_arr[h]) 
            h += 1 
```
위 그림의 [8, 2, 3, 7, 1, 5, 4, 6] 예시로 가정  
- 병합 1단계 : [8] [2] [3] [7] -> [2,8] [3,7]  
와 같이 하나와 하나가 모여서 둘이 될 때, 비교 연산은 최대 2회 진행됨 (while문 내에 위치한 비교연산의 횟수만 고려해서 1회 진행된다고 가정해도 빅-오 계산에 영향 없음)   
while 구간에서의 비교연산 횟수를 2회로 가정하면 병합 1단계에서 진행되는 비교연산의 횟수는 총 8회
- 병합 2단계 : [1,5] [4,6] -> [1,4,5,6]  
둘과 둘이 모여서 넷이 될 때 다음과 같이 비교가 진행됨
    - 1과 4를 대상으로 비교연산 후 1을 merged_arr로 이동
    - 5와 4를 대상으로 비교연산 후 4를 merged_arr로 이동
    - 5와 6를 대상으로 비교연산 후 5를 merged_arr로 이동
    - 마지막으로 남은 6을 merged_arr로 이동하기 위한 if-else문에서의 비교 연산  
비교연산 횟수 최대가 되고 그 수가 4가 됨
- 정렬 대상인 데이터의 수가 n개일 때, 각 병합의 단계마다 최대 n번의 비교연산이 진행됨
- 데이터의 수가 n개 일 때, 병합 정렬에서 진행되는 최대 비교연산의 횟수는 다음과 같음 (k: 병합 과정의 횟수)
     - k = log2N
- 따라서 병합 정렬의 비교연산에 대한 빅오는 **O(nlog2n)**
- 이동 연산에 대하여 이동이 두가자 경우에 발생함
    - 임시 배열에 데이터를 병합하는 과정
    - 임시 배열에 저장한 데이터 전부를 원위치로 옮길 때
    - 비교 연산 횟수의 2배에 해당하는 이동연산이 이루어짐
- 이동연산 횟수는 최악, 평균, 최선의 경우에 상관없이
    - 2nlog2n 
- 따라서 이동연산에 대한 빅-오는 **O(nlog2n)**  (숫자2는 상수이므로 무시할 수 있음) 

> ### 장단점
- 장점 
    -  퀵 정렬과 달리 기준값을 설정하는 과정없이 무조건 절반으로 분할하기에 기준값에 따라 성능이 달라지는 경우가 없음
    - 항상 O(N*logN) 이라는 시간복잡도를 가지게 됨
- 단점 
    - 임시배열에 원본 배열을 계속해서 옮겨주며 정렬을 하는 방식이기에 추가적인 메모리가 필요함
    - in place 알고리즘이 아니기 때문에 별도의 메모리 공간이 필요 
    - 만약에 정렬할 데이터의 양이 많은 경우에는 그만큼 이동 횟수가 많아지므로 시간적인 낭비도 많아지게 됨
    - in-place 로 구현할 경우 시간복잡도가 O(n^2)가 됨
 

### 출처
---
- 윤성우의 열혈 자료 구조
-  https://www.daleseo.com/sort-merge/ 
- https://roytravel.tistory.com/37
- https://velog.io/@codenmh0822/%EC%A0%95%EB%A0%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B3%91%ED%95%A9-%EC%A0%95%EB%A0%AC