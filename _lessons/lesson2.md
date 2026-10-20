--
# 1. 변수(variable)
    1) 정의: 어떤 값을 저장하기 위한 메모리 공간
    2) 변수 선언 규치
       - 변수 이름만 봐도 어떤 변수인지 해석할 수 있어야 함
       - 너무 함축적인 별명은 좋지 않음
       - 영문 대소문자, _(언더바), 숫자를 이용
       - 숫자로 시작하면 안됨
       - 파이썬은 미리 변수를 선언하지 않아도 됨
       - 하지만 코드가 길면 변수를 미리 선언하는 것이 좋음
    3) 예약어(reserved keywords) 피하기
       - python에서 미리 선점한 단어들
       - 예시: for, while, if, elif, class, try, except 등

```python
for = 100 # 예약어는 변수로 사용할 수 없다
```
![예약어를 변수로 쓰면 나는 오류]({{ site.baseurl }}/assets/images/lesson2-reserved-keyword.png)

```python
a = 100
print(a)
# 출력값 100
```

```python
4 == 9
# 출력값 False
```
# 2. 값(value)
    1) 값 할당
    - 변수의 값이 변경되기 위해서는 "="로 대입이 발생해야 함
    2) None: 아무 값을 갖지 않을 때 None gkfekd
    - 일반적으로 변수를 생성할 때
    - 다른 언어에서는 null 등으로 사용됨

```python
temperature = 20
temperature - 10 
temperature # "temperature - 10"을 변수로 지정하지 않았기 때문
a = temperature - 10 # 변수로 지정
a 
print(temperature - 10) # print 함수를 사용
# 출력값: 10
```

```python
count, sum = None, None
print(count, sum)
# 출력값: None None
```

# 3. 주석(comment)
    - 코드 # 뒷부분은 실행되지 않음
    - 메모장 역할, 파이썬은 #를 만나면 코드 실행시 무시
    - 코드의 기능이나 목적, 주의사항 등을 기록하는 용도
    - 주석을 다는 습관도 좋은 코드 관리 방법
