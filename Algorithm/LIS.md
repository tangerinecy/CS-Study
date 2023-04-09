주어진 배열에서 만들 수 있는 부분 수열 중에서,

각 원소가 이전 원소보다 크다는 조건을 만족하는 그 길이가 최대인 부분 수열.

예제)

[ 7, **2**, **3**, 8, **4**, **5** ] → 해당 배열에서는 [2,3,4,5]가 LIS로 답은 4

### 시간 복잡도

Dynamic Programming 이용: O(N^2)

Binary Search 이용: O(NlogN)

### Code

- DP 이용

![[https://4legs-study.tistory.com/106](https://4legs-study.tistory.com/106)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/94349218-f771-4086-845c-557de8065293/Untitled.png)

[https://4legs-study.tistory.com/106](https://4legs-study.tistory.com/106)

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
그림 출처: https://4legs-study.tistory.com/106 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f4383d1a-1291-4ad1-a23d-c2a76792dd60/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/83dac057-9cf3-48ed-94d0-d0bee7c5401f/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a69af9ac-a1cc-4134-9d21-098a3cafcff9/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/67d1c548-6e30-4b70-8b9e-05e94d31e10a/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cc7c5926-bf74-449d-962b-eeed8d42a04b/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6e01d8c7-19cd-4d72-bdf7-7e301dc8361e/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/799ef20f-a7b7-4357-8147-6f8fe3d66c77/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/315fd2af-6e60-4f0e-bb27-16845664da5b/Untitled.png)

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
