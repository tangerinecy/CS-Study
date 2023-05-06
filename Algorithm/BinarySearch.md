# Binary Search : 이분 탐색

### Binary Search (이분 탐색)

- 탐색 범위(배열)를 절반으로 줄여가며 대상을 찾는 알고리즘
- 알고리즘 성립을 위해 `**배열의 정렬이 반드시 필요**`
- 입력 데이터가 많거나 (ex. 1000만 개 이상), 탐색 범위의 크기가 클 때 효과적 (ex. 1000억 이상)
- 시간 복잡도 : O(log n)

### 이분 탐색 vs. 순차 탐색

- 이분 탐색 : 탐색 범위를 절반으로 줄여가며 탐색; O(log n)
- 순차 탐색 : 앞에서부터 차례대로 탐색; O(n)

### 동작 순서

1. mid 값 설정 : start(시작 idx)와 end(마지막 idx) 사의의 중간 값 (소수점 이하는 생략)
2. mid와 target(찾으려는 대상) 비교
    1. mid > target인 경우 → end를 mid-1로 설정 (mid보다 작은 범위 탐색 시작)
    2. mid < target인 경우 → start를 mid+1로 설정 (mid보다 큰 범위 탐색 시작)
3. mid = target이 될 때까지 반복

### 소스 코드_Python

- 재귀함수 ver.

```python
def binary_search (arr, target, start, end):
  
		if start > end:
        return None

    mid = (start + end)// 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)
```

- 반복문 ver.

```python
def binary_search (arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
    
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return None
```