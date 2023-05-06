# Count Sort : 계수 정렬

### Count Sort (계수 정렬)

- 값의 빈도를 Count하여 정렬하는 알고리즘
- 데이터 개수가 한정적인 경우에는 정렬 알고리즘 중에서 가장 빠름
- 알고리즘 성립을 위해 정확한 크기(MAX-MIN+1)의 리스트를 선언해야 함
- 리스트가 모두 정수 형태로 표현되어있고, 가장 작은 데이터와 가장 큰 데이터의 차이가 100만 이하일 때 효과적
- 시간 복잡도 : O(N+K) → 데이터 개수 = N, 최댓값 = K
- 공간 복잡도 : O(K  ) → k=배열 크기

### 동작 순서

1. 가장 작은 데이터부터 가장 작은 데이터까지 모두 담을 수 있는 리스트 생성 : 크기 = MAX-MIN+1, 기본 값 0
2. 정렬할 리스트 내의 데이터값과 생성한 리스트에서 일치하는 idx에 해당하는 값 1씩 증가
3. 생성한 리스트 내의 idx 순서대로 부여된 값(count)만큼 반복하여 정렬된 결과 출력

### 소스 코드_Python

```python
def count_sort (arr):
	cnt = [0] * (max(arr) + 1)

	for i in range(len(arr)):
    cnt[arr[i]] += 1

	for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end = ' ')
```