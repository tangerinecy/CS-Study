# SQL Injection(SQL 삽입/주입 공격)이란?
해커에 의해 조작된 SQL 문을 주입하고 실행되게 하여 데이터베이스가 비정상적인 동작을 하도록 조작하는 행위.  
공격이 쉬운 데에 비해, 공격 당할 시 피해가 크다.  
  
2017년 여기어때에서 발생한 개인정보 유출 사건도 SQL Injection 공격에 의한 것이었다.

# 공격 방법
## 1. 인증 우회(Authentication Bypass)  
보통 로그인할 때, 아이디와 비밀번호를 input 창에 입력하게 된다.  
예:
```sql
SELECT * FROM USER WHERE ID = 'abc' AND PASSWORD = '1234';
```
SQL injection 공격은 input 창에 비밀번호를 입력함과 동시에 다른 쿼리문을 함께 입력하는 것이다.  
비밀번호 창에 입력하는 값:  
```
1234' OR '1' = '1;
```
SQL 문:  
```sql
SELECT * FROM USER WHERE (ID = 'abc' AND PASSWORD = '1234') OR '1' = '1';
```
이렇게 쿼리 문이 바뀌게 되어 WHERE '1' = '1'이 만족하여 모든 정보를 출력하게 된다.  
영상 예시:  
[면접관이 SQL Injection에 대해 설명해보라고 한다면?](https://youtu.be/OUGrSB0CAxs)  
[SQL Injection](https://youtu.be/bIoGQ04biDg)  

## 2. Error Based SQL Injection  
SQL 쿼리에 고의적으로 오류를 발생시켜, 출력되는 에러의 내용을 통해 데이터베이스의 정보(Table, Column 등)를 찾아낸다.  
[SQL Injection 취약점(2)_Error Based Injection](https://byounghee.tistory.com/148)  

## 3. Union Based SQL Injection  
여러 개의 쿼리문에 대한 결과를 통합해서 하나의 테이블로 보여주는 UNION을 사용하여 원하는 쿼리문을 실행하도록 한다.  

## 4. Blind SQL Injection
- Boolean Based Blind SQL Injection  
   데이터베이스가 에러 메시지를 출력하지 않고, True/False 값만을 보여줄 때,
   SQL 쿼리문을 삽입한 후, 참/거짓 값을 통해 정보를 알아내는 공격이다.  

- Time Based SQL  
   데이터베이스의 네트워크 지연시간을 통해 정보를 알아내는 방법이다.  
   SLEEP() 등을 삽입하여, 응답 시간의 차이를 통해 참/거짓 여부를 판별할 수 있다.  
   예: 
   ![image](https://user-images.githubusercontent.com/111646902/241375042-ae571a79-39b5-4666-9aa5-59f04a8718fb.png)  
   위의 쿼리문에서 LENGTH(DATABSE()) = 1일 경우에 SLEEP을 수행한다.  
   1을 조작하여 응답 시간을 비교하여 SLEEP이 수행됐을 때의 값을 통해, 데이터베이스의 이름의 길이를 알아낼 수 있다.  


# 방어 방법
## 1. input 값을 받을 때, 특수문자 여부 검사하기(필터링)  
검증 로직을 추가하여 미리 설정한 특수 문자들이 들어왔을 때 요청을 막아낸다.  
예: [SQL Injection 대응 방안](http://blog.plura.io/?p=6056)  
   1-1. MySQL의 경우 mysqli_real_esacpe_string() 함수를 사용하여, SQL에서 특별한 의미를 갖는 문자들을 escape하게 한다.

## 2. SQL 서버 오류 발생 시, 해당하는 에러 메시지 감추기
일반 사용자는 view로만 접근 가능하도록 하는 등, 원본 데이터베이스 테이블에는 접근 권한을 높여, 일반 사용자는 에러를 볼 수 없도록 만든다.  
  
## 3. prepareStatement 사용하기  
prepareStatement를 사용하면, 사용자의 input 값이 쿼리와 별도로 서버로 전송되어 사용자가 입력한 구문이 쿼리로 실행될 수 없다.  
서버는 쿼리 템플릿이 모두 분석된 이후 실행 시점에서 사용자 입력값을 사용한다. 바인딩된 매개변수는 쿼리 문자열로 삽입되지 않으므로 escape할 필요가 없다.  
SELECT 처리 과정:  
![image](https://user-images.githubusercontent.com/111646902/241371927-eac157ee-ad4e-4953-8d05-20abc8fedb6e.png)  
일반적인 Statement를 사용할 경우 parse부터의 모든 과정을 수행한다.  
Prepared Statement를 사용할 경우 parse 과정을 최초 1번만 수행하고 이후에는 생략한다. parse 과정을 모두 거친 후에 생성된 결과는 메모리 어딘가에 저장 해두고 필요할 때마다 사용한다.  
사용자로부터의 입력값인 바인딩 데이터는 SQL 문법이 아닌 내부의 인터프리터나 컴파일 언어로 처리하기 때문에 문법적인 의미를 가질 수 없다. 따라서 쿼리로 실행되지 않는다.  
  
Statement:  
```sql
String query = "SELECT * FROM products WHERE category = '"+ input + "'";
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery(query);
```
Prepared Statement:  
```sql
PreparedStatement statement = connection.prepareStatement("SELECT * FROM products WHERE category = ?");
statement.setString(1, input);
ResultSet resultSet = statement.executeQuery();
```
[코드 출처](https://qh5944.tistory.com/156)

# 참고 자료
[SQL Injection 이란? (SQL 삽입 공격)](https://noirstar.tistory.com/264)  
[SQL Injection 취약점(2)_Error Based Injection](https://byounghee.tistory.com/148)  
[SQL Injection 총정리](https://gomguk.tistory.com/118)  
[SQL Injection 취약점과 대응 방법](https://qh5944.tistory.com/156)
