# 반복문

1. 반목문(loop)
    1) 반복적인 작업을 가능하게 해주는 도구
    2) 반복문이 없으면 코드는 엄청나게 길어질 것(비효율적)
    3) 코드에서 가장 많이 사용하는 구문 중 하나
    4) for 문, while 문
        - for 문: 횟수가 정해져 있을 때
        - while 문: 조건이 정해져 있을 때

2. while 문
    1) 특정 조건을 만족할 때
    2) 반복을 멈추게 하는 장치가 필요
        - 무한 루프에 빠지지 않게 주의
        - break: loop를 중단할 때 사용하는 제어문
            - 보통 조건문과 함께 사용
            - 탈출 이후에는 while 이후의 코드를 수행
        - continue: 남은 코드 블록은 건너뛰고 반복문의 처음으로 돌아감
        - 해당 아이템을 건너뛰고 싶을 때 사용
    3) while 문의 조건을 참일 경우, while 코드 블록 계속 수행

3. for 문
    1) 특정 횟수를 반복해야 할 때
    2) 리스트, 문자열 등 아이템을 하나씩 순회하면서 반복 가능
    3) for 문에서도 특정 조건일 때 break 사용 가능

4. 중첩 반복문
    1) 반목문도 중첩하여 사용 가능
    2) 반복문 블록 코드 안에 또 반복문이 등장, 무한히 중첩 가능



```python
# while문을 이용해 1부터 7까지 출력하는 코드를 짜시오.
i = 1
while i < 8:
    print(i)
    i += 1
```

    1
    2
    3
    4
    5
    6
    7
    


```python
# 1부터 10까지 합 구하기
total = 0
for i in range(1, 11):
    total += i
print(total)
```

    55
    


```python
# 0부터 100까지 7의 배수의 합계
seven = 0

for i in range(101):
    if i % 7 == 0:
        seven += i
print(seven)
```

    735
    


```python
# 1부터 100까지의 합을 구하되 3의 배수는 건너뛰고 더하는 코드를 짜시오.

three = 0

for i in range(1, 101):
    if i % 3 != 0:
        three += i
print(three)
```

    3367
    


```python
# 1부터 100까지의 합에서 최초로 1000 이상이 되는 위치를 계산하는 코드를 짜시오
num = 0
i = 1
while num < 1000:
    num += i
    if num >= 1000:
        break
    i += 1
print(i)
```

    45
    


```python
# 문자열을 거꾸로 출력하는 프로그램을 for문을 이용하여 만드시오.
# i는 0, 1, 2, 3, 4, 5
# 인덱스는 5, 4, 3, 2, 1, 0

text = '파이썬전문가'
sorted_text =''
for i in range(len(text)):
    sorted_text += text[len(text) - i -1]
    print(sorted_text)

```

    가
    가문
    가문전
    가문전썬
    가문전썬이
    가문전썬이파
    


```python
# 중첩 반복문

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i, '*', j, '=', i*j, end="  ")
    print()
```

    2 * 1 = 2  2 * 2 = 4  2 * 3 = 6  2 * 4 = 8  2 * 5 = 10  2 * 6 = 12  2 * 7 = 14  2 * 8 = 16  2 * 9 = 18  
    3 * 1 = 3  3 * 2 = 6  3 * 3 = 9  3 * 4 = 12  3 * 5 = 15  3 * 6 = 18  3 * 7 = 21  3 * 8 = 24  3 * 9 = 27  
    4 * 1 = 4  4 * 2 = 8  4 * 3 = 12  4 * 4 = 16  4 * 5 = 20  4 * 6 = 24  4 * 7 = 28  4 * 8 = 32  4 * 9 = 36  
    5 * 1 = 5  5 * 2 = 10  5 * 3 = 15  5 * 4 = 20  5 * 5 = 25  5 * 6 = 30  5 * 7 = 35  5 * 8 = 40  5 * 9 = 45  
    6 * 1 = 6  6 * 2 = 12  6 * 3 = 18  6 * 4 = 24  6 * 5 = 30  6 * 6 = 36  6 * 7 = 42  6 * 8 = 48  6 * 9 = 54  
    7 * 1 = 7  7 * 2 = 14  7 * 3 = 21  7 * 4 = 28  7 * 5 = 35  7 * 6 = 42  7 * 7 = 49  7 * 8 = 56  7 * 9 = 63  
    8 * 1 = 8  8 * 2 = 16  8 * 3 = 24  8 * 4 = 32  8 * 5 = 40  8 * 6 = 48  8 * 7 = 56  8 * 8 = 64  8 * 9 = 72  
    9 * 1 = 9  9 * 2 = 18  9 * 3 = 27  9 * 4 = 36  9 * 5 = 45  9 * 6 = 54  9 * 7 = 63  9 * 8 = 72  9 * 9 = 81  
    


```python
# 5줄에 계단 식으로 별을 출력하는 코드를 짜시오. 왼쪽정렬로 첫 번째 줄에는 별이 1개, 2번째 줄에는 별이 2개, ...
b = '*'

for i in range(1, 6):
    print(b*i)
    
```

    *
    **
    ***
    ****
    *****
    


```python
# 대각선으로 별을 출력하는 코드를 짜시오.

for i in range(5):
    print(" " * i + "*")

```

    *
     *
      *
       *
        *
    


```python
symptoms = ['발열', '기침', '두통']
patients = ['김환자', '이환자']

for symptom in symptoms:
    print(f" 증상확인: {symptom}")

for patient in patients:
    print(f" 환자 확인: {patient}")
```

     증상확인: 발열
     증상확인: 기침
     증상확인: 두통
     환자 확인: 김환자
     환자 확인: 이환자
    


```python
# 병동 환자 리스트 출력

ward = [
    {'name':'김환자', 'age':65, 'bp':150},
    {'name': '이환자', 'age': 45, 'bp': 120},
    {'name': '박환자', 'age': 72, 'bp': 162},
]    

for patient in ward:
    print(f" {patient['name']}({patient['age']}세) - 혈압: {patient['bp']}")
```

     김환자(65세) - 혈압: 150
     이환자(45세) - 혈압: 120
     박환자(72세) - 혈압: 162
    


```python
temperatures = [36.5, 37.2, 38.1, 36.8]

number = 0
for temp in temperatures:
    number += 1
    print(f"{number}번째: {temp}℃")
```

    1번째: 36.5℃
    2번째: 37.2℃
    3번째: 38.1℃
    4번째: 36.8℃
    


```python
# 혈압 정상, 이상 분류: 정상혈압(90~139)
# 120mmHg → ✅ 정상
# 145mmHg → ⚠️ 이상

bp_list = [120, 145, 88, 130, 162, 118]

for bp in bp_list:
    if bp >= 90 and bp < 140:
        print(f" {bp}mmHg → ✅ 정상")
    else:
        print(f" {bp}mmHg → ⚠️ 이상")
```

     120mmHg → ✅ 정상
     145mmHg → ⚠️ 이상
     88mmHg → ⚠️ 이상
     130mmHg → ✅ 정상
     162mmHg → ⚠️ 이상
     118mmHg → ✅ 정상
    

# enumerate() 순서 번호와 값을 함께
- 리스트를 순화할 때 **번호와 값을 동시에** 가져옵니다.


```python
# 번호를 직접 세는 번거로운 방법
index = 0
for name in patients:
    print(index + 1, name)
    index += 1

# enumerate()로 간결하게
for num, name in enumerate(patients, 1):
    print(num, name)
```

    1 김환자
    2 이환자
    1 김환자
    2 이환자
    

---
### 🟢  처방전 번호 + 중요도 표시 ⭐⭐
> 📌 **사용 개념:** `enumerate()` + `if` 조건

번호를 붙이되, 3번 이상 약물에는 `★ 중요` 표시를 추가하세요.

```
출력 예시:
1. 아스피린
2. 타이레놀
3. ★ 중요  항생제
4. ★ 중요  인슐린
```



```python

medications = ["아스피린", "타이레놀", "항생제", "인슐린", "혈압약"]

for num, med in enumerate(medications, 1):
    if num >= 3:
        print(f"{num}. ★ 중요  {med}")
    else:
        print(f"{num}. {med}")

```

    1. 아스피린
    2. 타이레놀
    3. ★ 중요  항생제
    4. ★ 중요  인슐린
    5. ★ 중요  혈압약
    
