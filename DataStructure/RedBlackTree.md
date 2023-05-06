### Red-Black Tree

<aside>
💡 이진 탐색 트리(BST)의 단점을 개선하기 위한 자료구조!

+ 자가 균형 이진 탐색 트리 (스스로 balancing)

</aside>

![img.png](img.png)

- 모든 노드는 `**RED**` or **`BLACK`**
- 루트 노드 = `**BLACK**`
- 리프 노드 (NIL; 자료를 갖지 않고 트리의 끝을 나타내는 노드) = **`BLACK`**
    - 따라서 **`RED`** 노드의 자식은 **`BLACK`** = No Double Red
- 임의의 노드에서 자손 nil 노드까지 가는 경로에서 **`BLACK`**의 수는 같음
- BST의 worse-case 시 단점 개선 → 모든 경우에 O(logN)

[Red/Black Tree Visualization](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)