# 함수가 필요한 이유
- 자주 쓰는 코드를 계속 복사 & 붙여넣기하기 번거로움
- 특정 기능을 하는 코드를 묶어두면 훨씬 코드가 깔끔해짐
- 테스트 코드를 통해 에러나 오류를 디버깅하기 쉬엄


```python
# 정사각형의 넓이를 계산: 가로 * 높이
def area_square(width, height):
    result = width * height
    return result

a = area_square(5, 8) # 가로 6, 높이 8의 정사각형 넓이 구하기
print(a)

# 원의 넓이을 계산 : 반지름 * 원주율(3.14)
def circle(radius, pi):
    result = radius * pi
    return result

b = circle(3, 3.14) # 반지름 3인 원의 넓이 구하기
print(b)
```

    40
    9.42
    

# 함수 생성 방법
1. 함수 구조    

```python
def 함수명(파라미터1, 파라미터2, ...., 파라미터 n):
    구현 코드
    return 출력 값
```

- 파라미터, 인자(parameter, argument): 함수에 입력(input)으로 전달하는 값
- 파라미터는 필요하지 않을 수도 있고 여러 개가 필요할 수도 있다
- 함수도 함수의 파라미터로 전달 가능
- 함수의 파라미터에 기본값(default)을 지정할 수 있다
- 구현 코드(body): 함수가 해당 기능을 수행하는 부분
- return: 함수의 출력값을 반환하는 키워드, 함수의 종료를 명시
    - return만 존재하면 None qksghks
    - return이 없는 경우, 함수 코드 블록이 종료되면 종료로 간주, None 반환
    - 복수 값 반환 가능, 여러 개 변수에 반환 값 대입 가능
- 함수명: 함수 이름만 봐도 어떤 기능을 하는지 알 수 있어야 한다.
    - 예시) count_a(X), count_studnets(O)

2. 함수의 사용(호출)
- 함수명(파라미터1, 파라미터2, .... , 파라미터n)
- 함수의 이름과 파라미터를 괄호 안에 전달하여 함수를 호출
- 정의된 순서에 따라 파라미터를 전달해야 함



```python
# 함수의 구조
def add(a, b):
    result = a + b
    return result

a = add(30, 40)
print(a) # 위의 함수 적용 값: 70
```

    70
    


```python
# operation 함수 생성(파라미터: x, y)
def operation(x, y):
    a = x + y
    m = x * y
    s = x -y
    return a, m, s

# return a, m, s에 대한 값을 출력
a, b, c = operation (20, 3)
print(a, b, c)

a, b, c = operation (3, 20)
print(a, b, c)
```

    23 60 17
    23 60 -17
    

# 변수의 범위(variable scope)

1. 전역 변수(global variable)
- 가장 상단에 선언되어 코드 긑까지 살아있는 변수

2. 지역 변수(local variable)
- 함수(특정 코드 블록) 안에 선언된 변수
- 함수 안에서만 사용됨 


```python
a = 20 # 전역변수

def func1():
    a = 10 # 지역변수
    print('func1()에서 a의 값:', a)

def func2():
    print('func2()에서 a의 값:', a) # func2()는 a의 값을 지정하지 않았으므로 전역변수 a 값이 출력되어야 함

func1()
func2() 
```

    func1()에서 a의 값: 10
    func2()에서 a의 값: 20
    


```python
# 디폴트 파라미터: 함수의 파라미터에 기본값 지정
# 

def default_parameter(a, b=3, c=1):
    print(a, b, c)

default_parameter(30) # a=30, b와 c는 default 값으로 반환

a = default_parameter(10, 20, 30) # b, c의 값 대신 입력된 20, 30을 사용
a
```

    30 3 1
    10 20 30
    

# 실습과제: 환자 예약 관리 시스템
- 병원에서 환자들의 진료 예약을 관리하는 시스템 작성
- 예약 시간 중복을 방지하고 운영시간을 쳌하는 실무적인 예약 시스템을 구현

# 요구 사항
1. 예약 가능 여부 확인 함수
    - 운영시간 내 예약인지 확인(9~18시)
    - 점심시간 제외(12~13시)
    - 결과를 (가능여부, 상태 키워드) 튜플로 반환
2. 예약 추가 함수
    - 예약 가능하면 예약 리스트에 딕셔너리 형태로 추가
    - 예약 불가능하면 구체적인 실패 이유 반환
    - 결과 메시지를 문자열로 반환
3. 예약 현환 출력 함수
    - 현재 예약된 환자들을 시간순으로 출력
    - 예약 없으면 "예약된 환자가 없습니다." 출력

# 출력 형식
```
=== 예약 처리 결과 ===
김환자 - 10시: 예약 완료
이환자 - 10시: 이미 예약된 시간입니다
박환자 - 12시: 점심시간 (예약 불가)
정환자 - 20시: 운영시간 외 (예약 불가)
최환자 - 14시: 예약 완료

=== 현재 예약 현황 ===
10시: 김환자
14시: 최환자
```



```python
# 운영시간, 점심시간
clinic_info = {
    "operating_hours": (9, 18),  # 운영시간 (9~18시)
    "lunch_break": (12, 13) # 점심시간 (12~13시)
}

# 예약환자
appointments = [
    {"time": 10, "patient": "김환자"},
    {"time": 14, "patient": "최환자"}
]

# 상태 키워드
AVAILABLE = "AVAILABLE"           # 예약 가능
LUNCH_TIME = "LUNCH_TIME"         # 점심시간
OUT_OF_HOURS = "OUT_OF_HOURS"     # 운영시간 외
ALREADY_BOOKED = "ALREADY_BOOKED" # 이미 예약됨
```


```python
# 1. 예약 가능 여부 확인 함수
def check_appointment_availability(hour):
    # 운영시간에 대한 코드
    start, end = clinic_info["operating_hours"]
    if not (start <= hour < end):
        return False, OUT_OF_HOURS
    # 점심시간에 대한 코드
    lunch_start, lunch_end = clinic_info["lunch_break"]
    if lunch_start <= hour < end:
        return False, LUNCH_TIME
    # 예약 가능 여부에 대한 코드
    for appointment in appointments:
        # 이미 예약 환자가 있다면
        if appointment["time"] == hour:
            return False, ALREADY_BOOKED
    # 운영시긴 외, 점심시간, 예약환자가 있지 않다면 예약 가능으로 반환
    return True, AVAILABLE

# 2. 예약 추가 함수
def add_appointment(patient_name, hour):
    is_available, status = check_appointment_availability(hour)

    # 예약 가능하면 예약 리스트에 딕셔너리 형태로 추가
    if is_available:
        appointments.append({"time":hour, "patient": patient_name})
        return f"{patient_name} - {hour}시: 예약완료"
    # 예약 불가능하면 구체적인 실패 이유 반환
    else:
        if status == LUNCH_TIME:
            reason = "점심시간 (예약불가)"
        elif status == OUT_OF_HOURS:
            reason = "운영시간 외 (예약불가)"
        elif status == ALREADY_BOOKED:
            reason = "이미 예약된 시간입니다"
        # 결과 메시지를 문자열로 반환
        return f"{patient_name} - {hour}시: {reason}"


# 3. 예약 현황 출력 함수
def show_appointments():
    if not appointments:
        return
    for appointment in appointments:
        time = appointment["time"]
        patient = appointment["patient"]
        print(f"{time}시: {patient}")


```


```python
# 테스트 데이터
test_requests = [
    ("김환자", 10),  # 정상예약
    ("이환자", 10),  # 중복시간
    ("정환자", 12),  # 점심시간
    ("박환자", 20),  # 운영시간 외
    ("최환자", 14)   # 정상예약
]

# 테스트 실행
print("=== 예약 처리 결과 ===")
for patient_name, hour in test_requests:
    result = add_appointment(patient_name, hour)
    print(result)

print("\n=== 현재 예약 현황 ===")
show_appointments()
```

    === 예약 처리 결과 ===
    김환자 - 10시: 이미 예약된 시간입니다
    이환자 - 10시: 이미 예약된 시간입니다
    정환자 - 12시: 점심시간 (예약불가)
    박환자 - 20시: 운영시간 외 (예약불가)
    최환자 - 14시: 점심시간 (예약불가)
    
    === 현재 예약 현황 ===
    10시: 김환자
    14시: 최환자
    
