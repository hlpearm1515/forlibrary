# forlibrary
텍스트 기반 데이터를 전처리하기위한 파이썬 라이브러리입니다.
욕설 필터링, 단어 빈도수 세기, 맞춤법 검사, 띄어쓰기 확인 - 이 전처리 기능을 가지고 있습니다.

## 프로젝트 소개

- 텍스트 전처리 라이브러리
- 기능:

1.욕설 필터링: replace모드는 문장에 있는 욕설을 골라 순화한 단어로 바꿔주는 기능이고, star모드는 문장에 있는 욕설을 별표(*)로 바꿔주는 기능입니다.
2.단어 빈도수 세기: 문장에서 쓰인 단어들의 얼마나 쓰였는지 숫자로 보여주는 기능입니다.
3.맞춤법 검사: 문장에서 맞춤법이 틀린 곳을 고치고, 고친 문장을 보여주는 기능입니다. 
4.띄어쓰기 확인: 문장에서 띄어쓰기가 틀린 곳을 고치고, 고친 문장을 보여주는 기능입니다.

## 설치방법
```python
pip install Word-Processing-tot
```
다음 명령어를 통해 라이브러리를 설치할 수 있습니다.

## 기능별 예제
1. frequency

```python
from convertion.frequency import count_word_frequency
sentence = "오늘은 정말 좋은 날이다. 오늘도 좋은 하루였으면 좋겠다!"
freq = count_word_frequency(sentence)
print(freq)
```
2. spacing checker

```python
from convertion.spacing_checker import correct_spacing
text = "그일은최선을다할만큼가치가있다고할만하다 한번에끝내고싶다 알수있다"
fixed = correct_spacing(text)
print("원문 :", text)
print("교정 :", fixed)
```
3. spell checker

```python
# (Levenshtein) 모듈 설치 필요
from convertion.spell_checker import SimpleSpellChecker
dictionary = [
    "파이썬",
    "공부",
    "재밌다",
    "하고",
    "싶다",
    "오늘",
    "날씨",
    "좋다"
]
checker = SimpleSpellChecker(dictionary
sentence = "파이선 공보 재밋다 하구 싶다 옽늘 날씨 조타"
print("원본 문장:")
print(sentence)
corrected = checker.check_sentence(sentence)
print("\n교정된 문장:")
print(corrected)
```
4. badwords

```python
from swear_filter import clean_text

text = "야 너 진짜 병신이냐 시발 왜그래"
print(clean_text(text, mode="replace"))
print(clean_text(text, mode="star"))
```

## API 상세설명
1. 단어 빈도수 세기
함수정의:
```python
count_word_frequency(sentence: str) -> collections.Counter[str]
```
기능: 문장 안에서 한글/영어/숫자로 이루어진 단어를 추출하고, 각 단어가 몇 번 등장했는지 빈도수를 계산해 반환합니다. 영문자는 모두 소문자로 변환하여 처리합니다.

2. 띄어쓰기 교정
함수정의:
```python
correct_spacing(text: str) -> str
```
기능: 문장에서 틀리는 띄어쓰기 패턴을 교정합니다.

3. 맞춤법 교정
함수정의:
```python
check(self, word: str) -> str
```
기능: 입력한 단어가 사전에 있으면 그대로 반환하고, 없으면 Levenshtein 거리를 이용해 가장 비슷한 단어 한 개를 반환
주의사항: pip install python-Levenshtein 필요

4. 욕설 단어 처리
함수정의:
```python
clean_text(text: str, mode: str) -> str
```
기능: 입력 문장에서 욕설을 탐지하여 두 가지 방식 중 하나로 치환합니다.
- mode="replace": 욕설을 미리 정의된 순화된 단어로 바꿉니다.

- mode="star": 욕설의 길이에 맞게 별표(*)로 치환합니다.

