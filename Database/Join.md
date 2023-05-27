# Join
## Join이란?
2개 이상의 테이블이나 데이터베이스를 연결하여 관련된 데이터를 검색하거나 조작하는 데 사용되는 기능.  
Join을 사용하면 관련된 테이블 간의 공통 열을 기준으로 데이터를 결합할 수 있다.  

# Join의 종류
## INNER JOIN
교집합.  
JOIN하는 테이블의 ON절의 조건이 일치하는 결과만 출력한다.  
![image](https://user-images.githubusercontent.com/111646902/241281895-e0af8837-53b3-4acf-85f2-b54b594a73d2.png)  

NATURAL JOIN 사용할 경우, 그리고 INNER JOIN을 사용하면서 ID를 하나만 보이게 SELECT 할 경우.  
![image](https://user-images.githubusercontent.com/111646902/241278090-357971d3-242d-4978-83f8-1b9105a1e8a3.png)  
```sql
SELECT *
FROM TableA
INNER JOIN TableB ON TableA.column = TableB.column;
```

## LEFT OUTER JOIN
기준 테이블값과 조인 테이블과 중복된 값을 보여준다.  
왼쪽 테이블 기준으로 JOIN 한다.  
![image](https://user-images.githubusercontent.com/111646902/241281969-68ce9835-ae1f-4b90-9c20-a0ed6905f54d.png)  
LEFT OUTER JOIN과 NATURAL LEFT OUTER JOIN.  
![image](https://user-images.githubusercontent.com/111646902/241279416-a7f1a5a2-1a1a-46e8-b489-abee09908e44.png)  
```sql
SELECT *
FROM TableA
LEFT OUTER JOIN TableB
ON TableA.column = TableB.column;
```

## RIGHT OUTER JOIN
LEFT OUTER JOIN과 반대로 오른쪽 테이블(조인 테이블) 기준으로 JOIN 한다.  
![image](https://user-images.githubusercontent.com/111646902/241282071-ebd02939-ed0c-41b9-8fcc-5e670e0a735f.png)  
RIGHT OUTER JOIN과 NATURAL RIGHT OUTER JOIN.  
![image](https://user-images.githubusercontent.com/111646902/241280543-f64aad68-8881-41a8-8816-0f288dd3ea6c.png)  
```sql
SELECT *
FROM TableA
RIGHT OUTER JOIN TableB
ON TableA.column = TableB.column;
```

## FULL OUTER JOIN
합집합.  
![image](https://user-images.githubusercontent.com/111646902/241282152-ed1d8624-f6c3-4c2e-9c8c-c635f3e0beb4.png)  

```sql
SELECT *
FROM TableA
FULL OUTER JOIN TableB
ON TableA.column = TableB.column;
```
**대부분의 DB는 FULL OUTER JOIN을 지원하지 않는다. 하지만 간접적으로 구현할 수 있다.**  
```sql
SELECT *
FROM TableA
LEFT JOIN TableB ON TableA.column = TableB.column
UNION
SELECT *
FROM TableA
RIGHT JOIN TableB ON TableA.column = TableB.column;
```
![image](https://user-images.githubusercontent.com/111646902/241282489-863528ac-dd8e-48d0-8c66-454af92f2343.png)  

## CROSS JOIN
모든 경우의 수를 표현해주는 JOIN이다.  
![image](https://user-images.githubusercontent.com/111646902/241283549-97f71133-d31d-4dab-b7db-fca3aa16a87b.png)  
![image](https://user-images.githubusercontent.com/111646902/241283669-ac60d866-3b18-4fcd-b96e-82651a68be6f.png)  
```sql
SELECT *
FROM TableA
CROSS JOIN TableB;
```

## SELF JOIN
자기 자신과 JOIN하는 것이다.  
![image](https://user-images.githubusercontent.com/111646902/241285095-d140acb8-158f-4824-8048-6c8a10481f9f.png)  
![image](https://user-images.githubusercontent.com/111646902/241284006-55774db2-0520-4cac-b8aa-0256ff6b891c.png)  
```sql
SELECT *
FROM A A1, A A2
```
# 참고자료
[테이블 조인(JOIN) - 그림으로 알기 쉽게 정리](https://inpa.tistory.com/entry/MYSQL-%F0%9F%93%9A-JOIN-%EC%A1%B0%EC%9D%B8-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EA%B8%B0%EC%89%BD%EA%B2%8C-%EC%A0%95%EB%A6%AC)  
[CS-Study](https://github.com/devFancy/2023-CS-Study/blob/main/DB/db_join.md)  
[tech-interview](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Computer%20Science/Database/%5BDatabase%20SQL%5D%20JOIN.md)  
KAIST EE477 수업  