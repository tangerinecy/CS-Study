### Red-Black Tree

이진 트리의 단점

1. B-Tree
- 하나의 노드에 많은 정보를 가질 수 있음
- 두 개 이상의 자식을 가질 수 있음
- 트리의 균형 자동 맞추는 로직 有
- 노드 : key & data
- data : disk block -> 포인터 될 수 있음

<aside>
규칙
  노드의 자료수가 N이면, 자식 수는 N+1이어야 함
  각 노드의 자료는 정렬된 상태여야함
  루트 노드는 적어도 2개 이상의 자식을 가져야함
  루트 노드를 제외한 모든 노드는 적어도 M/2개의 자료를 가지고 있어야함
  외부 노드로 가는 경로의 길이는 모두 같음.
  입력 자료는 중복 될 수 없음
</aside>

2. B+Tree 
- 데이터의 빠른 접근을 위해 인덱스 역할을 하는 비단말 노드가 추가로 존재
- index & leaf 노드로 분리되어 저장
- 노드 : key
- data : 모두 leaf 노드에 존재(add & delete 모두 여기에서 이루어짐)