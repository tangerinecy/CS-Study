# 기본적인 데이터베이스 용어
![image](https://user-images.githubusercontent.com/111646902/241367564-9573fc69-3d51-45e6-b2bb-f2a923dee36c.png)  
# Key란? 
데이터베이스에서 검색 정렬시 Tuple을 구분할 수 있는 기준이 되는 attribute 또는 attribute의 집합.  
## 최소성과 유일성 
- 유일성  
하나의 키값으로 레코드를 식별할 수 있는 성질.  

- 최소성  
키를 구성하는 최소로 필요한 속성들로만 키를 구성하는 성질.  

# Key 종류
## 예시 
| 고객ID | 이름 | 생년월일 | 수입 |
| --- | --- | --- | --- |
| 1 | 홍길동 | 990101 | 100 |
| 2 | 김지수 | 980703 | 200 |
| 3 | 이수진 | 990101 | 200 |
| 4 | 김철수 | 020201 | 150 |

## Super Key (슈퍼키)
**유일성을 만족하지만 최소성은 만족하지 않는 Key.**  
 
위의 예시에서 '고객ID', '이름'은 유일성을 만족한다.  
'생년월일', '수입'은 각각으로는 유일성을 만족하지 못 한다.  
하지만, '생년월일'과 '수입'을 묶으면 유일성을 만족한다.  
이렇게 어떤 속성끼리 묶든 중복값이 안 나오고 서로 구별만 할 수 있으면 슈퍼키가 될 수 있다.  

## Candidate Key (후보키)
**유일성과 최소성을 모두 만족하는 속성들의 부분 집합.**  
슈퍼키들 중 최소성도 만족하는 Key.  
기본키가 될 수 있는 후보들.  
 
위의 예시에서 '고객ID', '이름'만 유일성과 최소성을 모두 만족한다.  

## Primary Key (기본키)
**후보키 중 선택한 Main Key.**  
**Null 값을 가질 수 없다.**  
기본키로 선택된 속성은 동일한 값이 들어갈 수 없다.  

하나의 테이블에는 기본 키를 1개만 지정할 수 있다.  

후보키 중 하나이므로, **유일성과 최소성 모두 만족.**  
 
위의 예시에서 '고객ID'를 기본 키로 설정할 수 있다.  
나중에 테이블에 동일한 이름의 다른 고객의 정보를 추가할 수 있다.  

## Alternate Key (대체키)
**후보키 중 기본키를 제외한 나머지 키.**  
 
위의 예시에서는 '이름'이 된다.  

## Foreign Key (외래키)
**다른 릴레이션의 기본키를 참조하는 속성의 집합.**  
 
예를 들어, 위의 예시를 '고객 정보' 테이블이라고 하자.  
각 고객의 계좌 번호에 대한 정보인 '계좌 정보' 테이블에서 '고객 정보' 테이블을 참조한다고 하자.  
'계좌 정보' 테이블에서는 attribute로 '고객 ID', '계좌 번호'가 있을 때, 이 '고객 ID'는 '고객 정보' 테이블의 기본 키인 '고객 ID'를 참조하는 외래키이다.  
![image](https://user-images.githubusercontent.com/111646902/241260426-30c3d454-82b9-4164-a348-d2538cee9d78.png)  
 

![image](https://user-images.githubusercontent.com/111646902/241260720-203543fe-917d-42a9-bf4e-dfe66eb92977.png)  

# 참고자료
[데이터베이스 키 종류 정리](https://inpa.tistory.com/entry/DB-%F0%9F%93%9A-%ED%82%A4KEY-%EC%A2%85%EB%A5%98-%F0%9F%95%B5%EF%B8%8F-%EC%A0%95%EB%A6%AC)  
[CS-Study](https://github.com/devFancy/2023-CS-Study/blob/main/DB/db_key.md)  
[tech-interview](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Computer%20Science/Database/%5BDB%5D%20Key.md)  
[TCP School](http://tcpschool.com/mysql/mysql_intro_relationalDB)  