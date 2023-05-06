## LinkedList  

LinkedList (연결 리스트)

데이터와 포인트로 구성된 노드 간의 연결을 이용하여 리스트를 구현한 자료구조.
![image](https://user-images.githubusercontent.com/76094329/236622993-13b7940b-0fda-436c-9e4c-0c6a016db3fe.png)  

Head 는 리스트의 처음을 나타낸다.
각 노드는 데이터와 다음 노드를 가리키는 Next 포인터로 구성되어있다.  
각 노드는 next 포인터를 사용하여 다음 노드와 연결된다.  
마지막 노드는 null을 가리켜 리스트의 끝을 나타낸다.  

### 연결 리스트의 특징  
노드의 next 부분에 다음 노드의 위치를 저장함으로써 선형적 데이터 자료구조를 가진다.  
특정 위치의 데이터 탐색을 위해서는 첫 노드부터 순차 검색만 가능하다.  
배열과 달리 주소 연결을 통해 삽입 삭제가 가능하므로 효율적이다.  

### 연결 리스트의 장점  
크기가 가변적이다  
삽입 및 삭제가 쉽다.  

### 연결 리스트의 단점  
요소에 접근하기 위해서는 첫 번째 노드부터 순차적으로 접근해야만 한다.  
포인터를 위한 축 메모리 공간이 필요하다.  



## 연결 리스트의 종류  

### 단순 연결 리스트 
  
![image](https://user-images.githubusercontent.com/76094329/236624762-433426e9-a380-4fb1-aba1-c7e632cc5f3b.png)  

### 이중 연결 리스트  
  
![image](https://user-images.githubusercontent.com/76094329/236624767-98af149a-8494-47b9-a3f4-205d83b4dfd0.png)  

### 원형 연결 리스트  
  
![image](https://user-images.githubusercontent.com/76094329/236624771-119fddec-f63a-465d-8cec-1115c328de9a.png)  



## Array & ArrayList & LinkedList  
### Array  
- 사이즈가 정적이다  
- element 삽입, 삭제가 비효율적  
  
### ArrayList  
- 사이즈가 동적이다
- element 삽입, 삭제가 비효율적  
  
### LinkedList  
- element 삽입, 삭제가 효율적이다 (각 노드가 자신의 다음 순서만을 가리키므로, 포인터만 바꿔주면 됨)  
- 데이터 조회 시 첫 번째 노드부터 모두 확인해야 한다  



