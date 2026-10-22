# Python Journey 🚀
> 파이썬 마스터를 향한 공부 기록 블로그

🔗 **블로그 주소:** https://having-all.github.io/python_journey/

## 📚 목차
# python_journey

AI 파이썬 교재(7장)를 따라 공부하며 개념 정리와 연습 코드를 모아 두는 저장소입니다.

## 목차

| 장 | 주제 | 핵심 키워드 | 노트 | 진도 |
| --- | --- | --- | --- | --- |
| 1장 | 변수와 데이터 타입 | print, f-string, int·float·str·bool, 연산자 | [notes](01_variables/notes.md) | ⬜ |
| 2장 | 자료구조 | 리스트, 튜플, 딕셔너리, 집합 | [notes](02_data_structures/notes.md) | ⬜ |
| 3장 | 조건문 | if·elif·else, in, and·or·not, 삼항 연산자 | [notes](03_conditionals/notes.md) | ⬜ |
| 4장 | 반복문 | for, range, enumerate, zip, while, break·continue, 컴프리헨션 | [notes](04_loops/notes.md) | ⬜ |
| 5장 | 함수 | def, 매개변수, return, 기본값, 람다 | [notes](05_functions/notes.md) | ⬜ |
| 6장 | 클래스와 객체지향 | class, `__init__`, self, 상속, 오버라이딩 | [notes](06_classes/notes.md) | ⬜ |
| 7장 | 파일 입출력과 예외처리 | open, with, csv, try·except·finally, raise | [notes](07_files_exceptions/notes.md) | ⬜ |
| 부록 | 자주 만나는 에러 | 에러 메시지 읽는 법, VS Code 환경 문제 | [notes](appendix_errors/notes.md) | ⬜ |

진도 표시: ⬜ 시작 전 · 🟨 공부 중 · ✅ 완료

## 폴더 구성

```text
python_journey/
├── 01_variables/
│   ├── notes.md          개념 정리
│   └── practice.ipynb    연습 코드
├── 02_data_structures/
├── 03_conditionals/
├── 04_loops/
├── 05_functions/
├── 06_classes/
├── 07_files_exceptions/
├── appendix_errors/
├── .vscode/settings.json
├── .gitignore
└── README.md
```

## 노트 작성 틀

각 장의 `notes.md`는 아래 순서로 씁니다.

1. **한 줄 요약**: 이 장을 한 문장으로
2. **내가 이해한 것**: 교재 문장이 아니라 내 말로
3. **헷갈렸던 것**: 틀린 코드, 에러 메시지, 해결 방법
4. **코드**: 직접 실행해 본 예제

## 실행 환경

- Python 3.12 (uv 가상환경 `.venv`)
- VS Code + Jupyter 확장

다른 컴퓨터에서 환경 다시 만들기:

```
uv venv --python 3.12
uv pip install -r requirements.txt
```
