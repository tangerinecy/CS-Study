최대한 깊이 내려간 뒤, 더이상 깊이 갈 곳이 없을 경우 옆으로 이동.

예) 길 찾기에서 최대한 한 방향으로 갈 수 있을 때까지 갔다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서 그 갈림길부터 다른 방향으로 탐색 진행하는 방식.

1. 모든 노드를 방문하고자 하는 경우에 이 방법 선택
2. BFS보다 조금 더 간단
3. BFS보다 느림.

### 시간복잡도

V: 정점의 개수, E: 간선의 개수

- 인접 행렬 : O(V^2)
- 인접 리스트 : O(V+E)

stack 또는 재귀함수 사용.

### 코테 예제
https://school.programmers.co.kr/learn/courses/30/lessons/43165

### 코드

```python
#각 노드의 연결 정보를 2차원 리스트로 표현
graph = []

visited = [False] * 9

def dfs (graph, cur_node):
	visited[cur_node] = True
	print(cur_node, end= ' ')

	for node in graph[cur_node]:
		if not visited[node]:
			dfs(graph, node)

dfs(graph, 1, visited)
```

### 참고자료

[[이것이 코딩 테스트다 with Python] 18강 DFS 알고리즘](https://freedeveloper.tistory.com/372)
