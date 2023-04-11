# 퀵 정렬
  
> ### 개념
- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 병합 정렬과 마찬가지로 '분할 정복(divide and conquer)'에 근거하여 만들어진 정렬 방법
    - 정렬 과정을 반씩 줄여나가는 과정을 포함함 
- 평균적으로 매우 빠른 정렬의 속도를 보이는 알고리즘
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘

> ### 기본 원리와 동작 예시
- left: 정렬 대상의 가장 왼쪽 지점을 가리키는 이름
- right: 정렬 대상의 가장 오른쪽 지점을 가리키는 이름
- pivot: 피벗이라 발음하고 중심점, 중심축의 의미를 담고 있음, 정렬을 진행하는 데 필요한 일종의 '기준'
- 기본적인 퀵정렬은 첫번째 데이터를 기준 데이터(Pivot)으로 설정함

![image](https://user-images.githubusercontent.com/76865900/231230252-36032e47-ec50-44a2-afd7-b96818f28c6b.png)

    - 교차되는 상황 : left > right 


> ### 소스 코드 (Python)
- 일반적인 방식
 ```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8] 
def quick_sort(array, start, end) : 
	if start >= end : #원소가 1개인 경우 종료
		return
	pivot = start #피벗은 첫번째 원소
	left = start+1
	right = end
	while(left <= right) : 
		#피벗보다 큰 데이터를 찾을 때까지 반복
		while(left <= end and array[left] <= array[pivot]) : 
			left += 1
		#피벗보다 작은 데이터를 찾을 때까지 반복
		while(right > start and array[right] >= array[pivot]) : 
			right -= 1
		if(left > right) : #엇갈렸다면 작은 데이터와 피벗을 교체
			array[right] , array[pivot] = array[pivot], array[right] 
		else : 
			array[left], array[right] = array[right], array[left] 
	quick_sort(array, start, right-1)
	quick_sort(array, right+1, end)
	
quick_sort(array, 0, len(array)-1 )
print(array)
``` 
- 파이썬의 장점을 살린 방식
 ```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8] 
def quick_sort(array) : 
	#리스트가 하나 이하의 원소만을 담고 있다면 종료
	if len(array) <= 1 : 
		return array
	pivot = array[0] #피벗은 첫번째 원소
	tail = array[1:] #피벗은 제외한 리스트
	
	left_side = [x for x in tail if x<=pivot] #분할된 왼쪽 부분
	right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
	
	#분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
	return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))
```
    - 개인적 의문 : 각 회차에서 원소별로 이동 위치는 전의 로직이랑 달라질 수도(순서가 반대로) 있을 것 같다
    - 근거 : 이전 로직은 (인덱스 기준으로) 오른쪽은 내림차순으로 비교했는데 for문을 돌면 오름차순으로 탐색할 수밖에 없음

> ### 성능 평가
- 시간 복잡도
    - 평균의 경우 : O(NlogN)
    - 최악의 경우 : O(N^2)
        - 이미 정렬된 배열에 대하여 첫번째 원소를 피벗으로 삼을 때 퀵정렬 수행하면 최악의 시간 복잡도 갖게 됨
        -ex) [1, 2, 3, 4, 5, 6, 7, 8, 9] > 첫번째 원소를 피벗으로 삼을 때 배열이 둘로 나뉘지 않고 1부터 8까지 피벗이 되어 정렬 과정을 거치게 됨
    - 전체 데이터를 기준으로 중간에 해당하는 값을 피벗으로 결정할 때 좋은 성능을 보이게 됨

- 시간복잡도 증명 과정  
![image](https://user-images.githubusercontent.com/76865900/231230793-ff1abaf6-e0a1-4898-85fa-69a2a59331ba.png)
    - 피벗이 결정되면 left는 오른쪽으로 right는 왼쪽으로 이동을 시작함 
    - 해당 이동은 left와 right가 역전될 때까지 진행 
    - 이동의 과정에서 피벗과의 비교를 매번 수반하므로, 하나의 피벗이 제자리를 찾아가는 과정에서 발생하는 비교연산의 횟수는, 데이터의 수에 해당하는 n이라고 할 수 있음 (피벗으로 인해 n-1의 비교연산이 이루어지지만 상수 차이는 무시)
    - n개의 비교가 수행되는 분할이 몇 단계에 걸쳐서 이루어지는지 확인해야 함
        - ex) 총 31개 데이터 대상으로 퀵정렬 진행, 피벗이 중간값으로 결정되는 이상적인 경우 가정
        - 31개의 데이터는 15개씩 둘로 나뉘어 총 2조각이 됨 <- 1차 나뉨
        - 이어서 각각 7개씩 둘로 나뉘어 총 4조각이 됨 <- 2차 나뉨
        - 이어서 각각 3개씩 둘로 나뉘어 총 8조각이 됨 <- 3차 나뉨
        - 이어서 각각 1개씩 둘로 나뉘어 총 16조각이 됨 <- 4차 나뉨
    - 둘로 나뉘는 횟수를 k라고 할때, 데이터의 수 n과의 관계는 ?
        - k = log2n
        - 따라서 퀵정렬의 비교연산 횟수는 nlog2n (k*n = nlog2n)
    - 최악의 경우 과정
        - 둘로 나뉘는 횟수 k 와 데이터의 수 n의 관계
        - k = n 
        - 따라서 O(n^2)

> ### 장단점
- 장점 
    - =O(nlog2n)의 복잡도를 갖는 다른 정렬 알고리즘과 비교했을 때도 평균적으로 가장 빠른 정렬 속도를 가지고 있음
    - 이동횟수가 상대적으로 적고, 병합정렬과 같이 별도의 메모리 공간을 요구하지 않기 때문
- 단점 
   - 정렬된 리스트에 대해서는 퀵정렬의 불균형 분할에 의해 오히려 수행시간이 더 많이 걸린다.
    - 퀵정렬의 불균형 분할을 방지하기 위하여 피벗을 선택할 때 더욱 리스트를 균등하게 분할할 수 있는 데이터를 선택한다.
(예를들어 리스트내의 몇 개의 데이터 중에서 크기 순으로 중간 값을 피벗으로 선택한다.)
 

### 출처
---
- 윤성우의 열혈 자료 구조
- 이코테 2021 정렬 알고리즘 (https://www.youtube.com/watch?v=KGyK-pNvWos&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=4)
- https://velog.io/@hanrimjo/%ED%80%B5-%EC%A0%95%EB%A0%AC-quick-sort-ssk6a2oba9
