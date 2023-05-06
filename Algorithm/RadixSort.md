# Radix Sort : 기수 정렬

### Radix Sort (기수 정렬)

- 낮은 자릿수부터 비교하여 정렬
- 비교 연산 수행 x → 정렬 속도 빠름
- 추가적인 메모리 공간을 필요로 함
- 자릿수가 없는 것(ex. 부동 소수점)은 정렬 불가능
- 시간 복잡도 : O(d * (n + b))
    - d는 정렬할 숫자의 자릿수, b는 10 (k와 같으나 10으로 고정되어 있다.)

### 동작 순서

- ex) 1의 자리 기준 정렬 → 10의 자리 기준 정렬 → 100의 자리…
1. 0~9까지 Bucket 준비 (Queue)
2. 1의 자리에 해당하는 숫자를 기준으로 알맞은 Bucket에 넣기
    - 50 → 0번쨰, 53 → 3번째,
3. Bucket 0부터 9까지 차례대로 데이터를 가져오기
4. 10의 자리에 해당하는 숫자로 다시 2번 반복

### 소스 코드_Python

```python
from collections import deque

def radix_sort (arr):
  
		buckets = [deque() for _ in range(10)]

    max_val = max(nums)
    Q = deque(nums)
    cur_ten = 1

    while max_val >= cur_ten:
        while Q:
            num = Q.popleft()
            buckets[(num // cur_ten) % 10].append(num)

        for bucket in buckets:
            while bucket:
                Q.append(bucket.popleft())

        cur_ten *= 10

    return list(Q)
```