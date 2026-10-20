## 🐍 Quiz 1 — 조건에 맞는 숫자 합계 구하기
다음 리스트에서 짝수이면서 10보다 큰 숫자들의 합계를 구하는 함수 `sum_even()`을 작성하세요.
조건
- `for` 반복문과 `if` 조건문을 사용하세요.
- 조건을 만족하는 숫자들의 합계를 return으로 반환하세요.
- `sum()` 내장함수는 사용하지 마세요.


```python
numbers = [3, 8, 12, 15, 20, 7, 18, 5]

def sum_even(numbers):
    total = 0
    for i in numbers:
        if i > 10:
            total += i
    return total

print(sum_even(numbers))
```

    65
    

## 🐍 Quiz 2 — 함수 + 조건문
다음은 학생의 점수를 전달받아 합격 여부를 반환하는 함수입니다.  
아래 조건에 맞게 `check_pass()` 함수를 완성하세요.  
조건
- 점수가 60점 이상이면 "합격"을 반환합니다.
- 점수가 60점 미만이면 "불합격"을 반환합니다.
- `if`, `else`, `return`을 사용하세요.


```python
def check_pass(score):
    if score >= 60:
        return "합격"
    else:
        return "불합격"


print(check_pass(85))
print(check_pass(45))
print(check_pass(60))
```

    합격
    불합격
    합격
    
