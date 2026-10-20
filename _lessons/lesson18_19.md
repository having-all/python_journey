# 클래스, 객체

## 1. 클래스(class)
    1) 실세계의 것을 모델링해 속성(attribute)과 동작(method)를 갖는 데이터타입
        - 현실 세계의 다양한 사물을 클래스로 표현 가능, 일종의 '설계도'
        - 속성을 필드(filed), 멤버 변수(member variable)이라고도 함
```python
class Car:
    # 자동차의 속성(색성, 속도 등) 일종의 변수 선언
    color = " "
    speed = 0
    # 자동차의 동작(속도올리기, 속도내리기)
    def upSpeed(self, value):
        # 구현 코드
    def downSpeed(self, value):
        # 구현 코드
```

    2) 파이썬에서 string, list, dict 등이 모두 클래스로 구현된 것
```python
a = [1, 2, 3, 4]
a.append(5)
print(a) 
# 출력결과: [1, 2, 3, 4, 5]
```
    3) 다루고자 하는 데이터(변수)와 연산(함수)를 하나로 캡슐화(encapsulation)


## 2. 객체
    1) 클래스로 생성되어 구체화된 것
        - 객체를 instance라고 함
    2) 파이썬에서 string, list, dict 등이 모두 클래스로 구현된 객체
    3) 클래스가 instance화 되어 메모리에 상주하는 상태
    4) 클래스가 붕어빵틀이라면, 객체는 실제로 찍어낸 붕어빵이라고 비유 가능
        - 한 클래스로부터 여러 개의 객체를 찍어낼 수 있음
    5) 파이썬은 객체지향 프로그램 언어(OOP; Object Oriented Programming)
        - 데이터를 객체로 취급하여 프로그램에 반영한 것
        - 객체와 객체의 상호작용으로 프로그램이 동작
        - 코드의 재사용성 높음, 직관적인 코드분석 가능, 개발 및 디버깅 속도 향상

## 3. 객체 생성하기
    1) 객체를 생성하기 위해서는 객체의 모체가 되는 클래스를 미리 선언해야 함
    2) 생성자 (init함수)
        - __init__(self)
        - 인스턴스를 생성하면 무조건 호출되는 메소드, 동시에 변수의 값을 초기화
            - init은 initialize의 약자
            - 코드도 간결해지고 변수에 초기값을 대입하는 것을 잊어버리는 것을 방지
        - 객체가 생성될 때 자동으로 호출됨
        - init 앞뒤로 언더바 2개씩 있음
            - self: 클래스 자기 자신을 가리킴, 메소드 안에서 속성에 접근하기 위해 필요함
            - 메소드 안에서 속성에 접근할 필요가 없다면 self 생략 가능
        - self 외에 별도의 매개변수를 사용하지 않는 생성자를 기본 생성자라고 함
                - 매개변수가 있는 생성자
            - 생성자도 다른 메소드처럼 매개변수를 사용할 수 있다
            - 여러 다른 객체를 생성할 때 매개변수 값으로 속성 초기화 가능


```python
class Car:
    color = " "
    speed = 0

    def __init__(self):
        self.color = '빨강'
        self.speed = 0

    def upSpeed(self, value):
        # 구현 코드
    def downSpeed(self,value):
        # 구현 코드

myCar = Car()
myCar.upSpeed(30)
```


```python
class Car:
    color = " "
    speed = 0

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def upSpeed(self, value):
        # 구현 코드
    def downSpeed(self, value):
        # 구현 코드

myCar = Car('빨강', 10)
myCar2 = Car('파랑', 20)
print("자동차 1의 색상은 %s이며, 현재 속도는 %dkm/h" % (myCar.color, myCar.speed))
```

    자동차 1의 색상은 빨강이며, 현재 속도는 10km/h
    

## 4. 메소드(method)
    1) 멤버함수, 객체.함수명()으로 호출
    2) 해당 객체의 속성에 대한 연산 수행


```python
class Car:
    # 자동차의 속성(색상, 속도 등)
    color = " "
    speed = 0

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    # 자동차의 동작(속도올리기, 속도 내리기)
    def upSpeed(self, value):
        self.speed += value
    def downSpeed(self, value):
        self.speed -= value 

myCar = Car('빨강', 10)
myCar.upSpeed(30)
myCar2 = Car('파랑', 20)
print("자동차 1의 색상은 %s이며, 현재속도는 %dkm/hr" % (myCar.color, myCar.speed))
print(f"자동차 1의 색상은 {myCar.color}이며, 현재속도는 {myCar.speed}km/hr")
```

    자동차 1의 색상은 빨강이며, 현재속도는 40km.hr
    자동차 1의 색상은 빨강이며, 현재속도는 40km.hr
    

## 요약 정리

| 단계 | 작업 | 형식 | 예시 |
|---|---|---|---|
| 1단계 | 클래스 생성 | `class 클래스이름:`<br>`# 필드 선언`<br>`# 메소드 선언` | `class Car:`<br>&nbsp;&nbsp;`speed = 0`<br>&nbsp;&nbsp;`def upSpeed(self, value):` |
| 2단계 | 객체, 인스턴스 생성 | 객체 = 클래스이름() | myCar() |
| 3단계 | 필드나 메소드 사용 | `인스턴스.필드이름 = 값`<br>`인스턴스.메소드()` | `myCar.color = '빨강' `<br>`myCar.upSpeed(30)`|

## 5. 클래스 상속(inheritance)
    1) 기존 클래스의 속성과 메소드를 그대로 물려받는 새로운 클래스를 만드는 것
    2) 기존 클래스에 기능을 추가하거나 변경하여 새로운 클래스 정의 가능
    3) 코드 재사용 가능 ex) 자동차 -> 승용차, 트럭 클래스 상속
    4) 기존 클래스는 Parent, Super, Base 클래스로 분류
    5) 상속받는 클래스는 Child, Sub, Derived 클래스라고 부름


```python
# 예시) Car 클래스를 상속 받는 Sedan, Truck 클래스 생성

class Car:
    color = " "
    speed = 0

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def upSpeed(self, value):
        self.speed += value
    def downSpeed(self, value):
        self.speed -= value

# Car 클래스를 상속 받은 Sedan 클래스
# 좌석 수의 속성 추가
class Sedan(Car):
    seatNum = 0
    def getSeatNum(self):
        return self.seatNum

# Car 클래스를 상속 받은 Truck 클래스
# 용적 속성 추가
class Truck(Car):
    capacity = 0 
    def getCapacity(self):
        return self.capacity

myCar = Car('빨강', 10)
sedan = Sedan('노랑', 40)
truck = Truck('흰색', 100)
sedan.upSpeed(50)
truck.downSpeed(30)
sedan.seatNum = 5
truck.capacity = 500

print(f"Sedan은 {sedan.color}색이고, 속도는 {sedan.speed}km/hr이며, 좌석수는 {sedan.seatNum}개이다")
print(f"Truck은 {truck.color}색이고, 속도는 {truck.speed}km/hr이며, 용적은 {truck.capacity}이다")
```

    Sedan은 노랑색이고, 속도는 90km/hr이며, 좌석수는 5개이다
    Truck은 흰색색이고, 속도는 70km/hr이며, 용적은 500이다
    

## 6. 메소드 오버라이딩(overriding)
    1) 부모 클래스의 메소드를 하위 클래스에서 재정의하는 것
    2) 자식 클래스는 메소드를 상속받았기 때문에 다시 메소드를 생성할 필요 없음
    3) 자식 클래스는 메소드의 내용을 수정해야 한다면 메소드를 다시 만들 수 있음
    4) 자식 클래스의 객체로 호출시, 재정의된 메소드가 호출됨


```python
# Car 클래스를 상속받은 Sedan 클래스의 속도에 대한 메소드 재정의
# Sedan의 upSpeed 메소드의 속도제한 재정의

class Car:
    color = " "
    speed = 0

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def upSpeed(self, value):
        self.speed += value
    def downSpeed(self, value):
        self.speed -= value

class Sedan(Car):
    seatNum = 0
    def getSeatNum(self):
        return self.seatNum
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed =150

sedan = Sedan('노랑', 50)
sedan.upSpeed(200)       #upSpeed를 200을 했지만 overriding에 의해 속도 150까지로 제한
sedan.seatNum = 5
print(f"Sedan은 {sedan.color}색이고, 속도는 {sedan.speed}km/hr이며, 좌석수는 {sedan.seatNum}개이다")

```

    Sedan은 노랑색이고, 속도는 150km/hr이며, 좌석수는 5개이다
    

## 7. 용어 정리

| 용어 | 설명 |
|---|---|
| overwrite(덮어쓰기) | `*한 구현을 다른 구현으로 완전히 **교체**하는 경우(replace, over)`<br>` *기존 값은 **파괴, 무효화**됨` |
| override(재정의하기) | `*상속받은 메소드의 내용을 **변경**하는것(change, modify, customize, take over)`<br>` *부모 메소드를 해치지 않고 자손 클래스에 맞게 수정한 다른 메소드 구현`<br>` *메소드명, 매개변수, 반환타입이 모두 같아야 함` |
| overload | `*이름만 같고 완전히 다른 메소드를 **새로 정의**하는 것`<br>` *매개변수의 개수나 데이터 타입이 달라야함`<br>` *같은 이름의 메소드를 여러 개 가질 수 있음`<br>` *기능이 같은데 매개변수만 다를 경우 메소드의 이름을 각자 정의할 필요 없음` |

