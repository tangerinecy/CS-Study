주어진 배열에서 만들 수 있는 부분 수열 중에서,

각 원소가 이전 원소보다 크다는 조건을 만족하는 그 길이가 최대인 부분 수열.

예제)

[ 7, **2**, **3**, 8, **4**, **5** ] → 해당 배열에서는 [2,3,4,5]가 LIS로 답은 4

### 시간 복잡도

Dynamic Programming 이용: O(N^2)

Binary Search 이용: O(NlogN)

### Code

- DP 이용

```python
arr = [] #주어진 배열
dp = [1 for i in range(len(arr))] #배열의 각 원소까지 가능한 최장증가부분수열의 크기를 정의함

for i in range(len(arr)):
	for j in range(i):
		if arr[i] > arr[j]:
			dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
```

- Binary Search 이용

```python
import bisect

x = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))
```

### 참고자료

[최장 증가 수열 (LIS, Longest Increasing Subsequence)](https://4legs-study.tistory.com/106)

[가장 긴 증가하는 부분 수열(LIS) 완전 정복 - 백준 파이썬](https://seohyun0120.tistory.com/entry/가장-긴-증가하는-부분-수열LIS-완전-정복-백준-파이썬)
