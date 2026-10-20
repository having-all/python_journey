# 함수
- 특정 기능을 하는 코드 블럭(묶음)
- 주어진 입력(input)에 대해 의도된 출력(output)을 전달하는 역할
- 반복적으로 호출해서 사용 가능
- 내장함수(built-in function): 파이썬 내부에 이미 정의(구현)되어 있는 함수
- 직접 필요에 따라 함수를 만들 수 있음

# print() 함수
- 값을 출력하는 함수
- ','로 여러 변수를 나열하면 같은 줄에 한 칸 띄어쓰기 후 출력
- print() 함수가 없어도 코드 마지막에 변수를 두면 값이 출력됨


```python
print('Hello World!')
print('Hello', 'World!')
a = 'Hello World!'
print(a)

```

    Hello World!
    Hello World!
    Hello World!
    

# print() 함수 서식 지정
- %d : 정수(decimal)
- %f : 실수(float)
- %c : 문자 한 글자(character)
- %s : 한 글자 이상의 문자열(string)


```python
print("200+300") # 문자로 인식
print(200+300)  # 숫자로 인식하여 계산 값 출력
```

    200+300
    500
    


```python
print("%d %d %f" % (100, 200, 3.14)) # %를 기준으로 오른쪽 값이 대입됨
print("%5d" % 100)  # 5칸 확보 후 오른쪽 정렬
print("%-5d" % 100) # 5칸 확보 후 왼쪽 정렬
print("%05d" % 100) # 5칸 확보 후 0으로 채움
print("%c" % 'A')   # 문자 출력
print("%s" % 'Hello World!') # 문자열 출력

```

    100 200 3.140000
      100
    100  
    00100
    A
    Hello World!
    

# 문자열 함수
1. 문자열은 여러 가지 기능을 가진 함수를 내장하고 있음
2. 문자열은 객체임, "함수명()" 구조를 활용해 함수를 호출한 것
3. 문자열 함수 종류
    1) 대소문자 변환
    - upper(): 소문자를 모두 대문자로 변환
    - lower(): 대문자를 모두 소문자로 변환
    - title(): 각 단어의 제일 앞 글자만 대문자로 변환
    2) 문자열 찾기
    - count(): 찾을 문자열이 몇 개 들었는지 개수 세기
    - find(): 문자열이 몇 번째 위치하는지 인덱스 알려줌
    - index(): find()와 같은 기능
    - startswith(): 찾을 문자열로 시작하면 True, 그렇지 않으면 False 반환
    - endswitch(): 찾을 문자열로 끝나면 True, 그렇지 않으면 False 반환
    3) 문자열 공백 제거, 추가, 변경
    - replace(): 문자열 내의 특정 문자열을 새 문자열로 치환
    - strip(): 문자열의 앞뒤 공백 제거(문자열 중간 공백은 제거 x)
    4) 문자열 분리, 결합
    - split(): 문자열을 특정 문자(delimeter)로 분리하여 리스트로 반환
    - join(): 문자열을 합쳐줌
    5) 문자열 동적 지정
    - format(): 문자열 내 특정 값을 변수화하여 동적으로 문자열 생성



```python
text = 'Today is raining'
text.upper() # 대문자로 변환
```




    'TODAY IS RAINING'




```python
text.lower() # 소문자로 변환
```




    'today is raining'




```python
text.title() # 각 단어의 제일 앞 글자만 대문자로 변환
```




    'Today Is Raining'




```python
text.count('i') # 'i'의 개수 세기기 => 3개
```




    3




```python
text.find('r') # 'r' 몇 번째에 위치하는지 알려줌
```




    9




```python
text.replace('raining', 'sunny') # raining -> sunny로 변환
```




    'Today is sunny'




```python
text.split(' ') # 문자열을 나눔
```




    ['Today', 'is', 'raining']




```python
# 문자열을 포맷팅하기
temperature = 25
prob = 70
text = '오늘 기온:{}도, 강수 확률: {}%'.format(temperature, prob)
print(text)
```

    오늘 기온:25도, 강수 확률: 70%
    

# 기타 자주 쓰이는 함수들
- sum(): 리스트, 튜플 등을 입력하면 전체 아이템의 합을 계산
- range(): 점수를 입력하면 (0, 정수)로 이루어 지는 지정된 범위의 값 변환
- len(): 리스트, 튜플 등을 입력하면 아이템의 개수를 세주는 기능
- int(): 정수로 변환
- float(): 실수로 변환
- str(): 문자열로 변환


```python
a = [1, 2, 3, 4, 5]
print(sum(a)) # a 안의 모두 수의 합: 15
print(list(range(0, 10))) # 0~9까지의 수를 list로 생성: 0부터 시작해서 10개의 수를 생성
print(len(a)) # a 안의 수의 개수
print(int('10'))  # 문자열을 실수로 변환한 뒤 정수로 변환
print(float('10')) # 문자열을 실수로 변환
print(str(10.2)) # 숫자를 문자열로 변환
```

    15
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    5
    10
    10.0
    10.2
    
