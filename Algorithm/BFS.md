현재 정점에 연결된 가까운 점들부터 탐색

1. 최단 거리,  경로 구해야 하는 문제에 주로 사용.

### 시간복잡도

V: 정점의 개수, E: 간선의 개수

- 인접 행렬 : O(V^2)
- 인접 리스트 : O(V+E)

queue 사용.

코테 예제)

[](https://school.programmers.co.kr/learn/courses/30/lessons/1844)

```python
from collections import deque

#각 노드의 연결정보를 2차원 리스트로 표현
graph = []
visited = [False] * 9

def bfs (graph, cur_node, visited):
	queue = deque([cur_node])
	visited[cur_node] = True
	while queue:
		v = queue.popleft()
		print(v, end = ' ')
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

bfs(graph, 1, visited) #첫 번째 노드부터 시작
	
```

참고자료:

[DFS, BFS의 설명, 차이점](https://velog.io/@lucky-korma/DFS-BFS의-설명-차이점)

[[이것이 코딩 테스트다 with Python] 19강 BFS 알고리즘](https://freedeveloper.tistory.com/373)
