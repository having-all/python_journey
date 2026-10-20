# 조건문

## 1. 조건문(condition)
    1) 특정 조건을 만족하는 경우에만 수행할 작업이 있을 때 사용
    2) 조건문 식은 boolean으로 표현(참, 거짓)
    3) if, elif, else 키워드 사용
    4) 들여쓰기로 종속 코드 구분
    5) 실행 코드가 여러 줄이면 정확하게 들여쓰기 필요

## 2. 조건문 예시
    1) if else 문
        - if 조건이 True이면 if 블록을 수행
        - False이면 else 블록을 수행
    2) if elif else 문
        - 조건이 여러 개일 경우 다음 조건을 elif 블록에 명시

## 3. 중첩 조건문(nested condition)
    1) 조건문은 중첩하여 작성 가능
    2) if문 안에 if 문이 들어 갈 수 있음
    3) 중첩은 깊이(depth)와 유사한 개념, depth의 제한은 없음


```python
# 짝수, 홀수 판별하는 함수 만들기
def test_num(a):
    if a % 2 == 0:
        print('짝수입니다.')
    else:
        print('홀수입니다.')
test_num(4)
```

    짝수입니다.
    


```python
# 자격증 과정 합격 여부 판별 함수
def license_pass(score):
    if score >= 80:
        print('합격입니다.')
    else:
        print('불합격입니다.')
license_pass(60)

```

    불합격입니다.
    


```python
# 두 수를 입력해서 큰 값을 출력하는 함수를 만드시오.
def compare_number(a, b):
    if a > b :
        return a
    elif a < b:
        return b
    else:
        return a
compare_number(3, 7)
```




    7




```python
# 나이를 체크하는 함수를 만드시오
# 미성년자와 성인을 구분하고, 입장 가능 여부를 Yes No로 반환하시오

def age_check(age):
    if age >= 18:
        return 'Yes'
    else:
        return 'No'

age = 40
age_check(age)
```




    'Yes'




```python
# 윤년 판별 프로그램을 함수로 만드시오
# 윤년은 태양년에 맞추기 위해 4년에 한 번씩 윤날(2월 29일)을 추가하는 해
# 윤년의 조건 : 4의 배수이면서 100의 배수는 아닌 해, 단 400의 배수는 다시 윤년으로 인정된다
# 4, 8, 12, ..., 100(제외), 104, ..., 200(제외), 400, 800

def determine_leap_year(year):
    if (year % 4 == 0) & (year % 100 != 0) | (year % 400 == 0):
        return print(f'{year}년은 윤년입니다.')
    else:
        return print(f'{year}년은 윤년이 아닙니다.')

year = 400
determine_leap_year(year)

```

    400년은 윤년입니다.
    


```python
# 메뉴 이름을 입력하면 메뉴판 가격 알려주는 함수를 만드시오
# 떡볶이는 8000원, 만두는 6000원, 라면은 5000원, 그 외 다른 메뉴가 들어오면 "해당 메뉴는 팔지 않습니다" 출력

def cost(menu):
    if menu == '떡볶이' :
        print('8000원')
    elif menu == '만두' :
        print('6000원')
    elif menu == '라면' :
        print('5000원')
    else:
        print('해당메뉴는 팔지 않습니다.')

cost('떡볶이')
cost('순대')
```

    8000원
    해당메뉴는 팔지 않습니다.
    


```python
# 중첩 조건문

# 학점 판별기

def grade(score):
    if score >= 90:
        if score >= 95:
            grade = 'A+'
        else:
            grade = 'A0'
    elif score >= 80:
        if score >= 85:
            grade = 'B+'
        else:
            grade = 'B0'
    elif score >= 70:
        if score >= 75:
            grade ='C+'
        else:
            grade = 'C0'
    elif score >= 60:
        if score >= 65:
            grade = 'D+'
        else:
            grade = 'D0'
    else:
        grade = 'F'

    return grade

print(grade(92))
print(grade(40))
```

    A0
    F
    
