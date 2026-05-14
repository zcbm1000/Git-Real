

# dictionary(딕셔너리)
'''
딕셔너리(dictionary)는 리스트와 함께 파이썬 프로그램에서 많이 사용하는 컨테이너 자료형입니
다. 리스트가 인덱스를 이용하여 아이템을 참조한다면, 딕셔너리는 인덱스 대신 키(key)를 이용하
여 아이템을 참조(관리)합니다. 
'''

# 딕셔너리는 키(key) 와 값(value)로이루어져잇음
# 딕셔너리는 인덱스대신 키를이용함.
# 리스트의 인덱스는 자동생성이나 딕셔너리의 키는 직접입력해야함.
# 3개의 사물함이있음 (값은 사물함이된)
# 3개의 사물함에는 각 맞는 열쇠가 있음(key)
# 1번 열쇠는 1번 사물함만 열수있음

# 딕셔너리 정의
# 딕셔너리는 {} 이용함 | 리스트는 [] | 튜플은 ()

# 키 값은 절대! 중복 되면 안된다.
# 밸류 값은 상관 없음.

# #      |   키   밸류 |   키   밸류 |   키   밸류 |   키   밸류 |  키   밸류 |
ages = {'박찬호': 48, '박지성': 40, '박세리': 50, '이승열': 43, '박지성': 50}
# print(f'ages: {ages}')
# print(f'ages type: {type(ages)}')

# scores = {
# 'c/c++'  : 'A', 
# 'java'   : 'B+',
# '네트워킹': 'C',
# '보안'    : 'A+',
# '해킹'    : 'F',
# '시스템'  : 'C+'
# }

# print(f'scores: {scores}')


# 리스트, 튜플, 딕셔너리

# listVar = [3, 3.15, 'hell']
# print(f'listVar: {listVar}')

# tupleVar = [3, 3.15, 'hell']
# print(f'tupleVar: {tupleVar}')

# dictVar = {
#     '홍길동': 10,
#     '박찬호': '열살',
#     '박세리': 3.14
# }
# print(f'dictVar: {dictVar}')


# listVar1 =[1, 2, 3]
# listVar2= [1, 2, 3, listVar1]

# print(f'listVar1: {listVar1}')       # listVar1: [1, 2, 3]                  
# print(f'listVar2: {listVar2}')       # listVar2: [1, 2, 3, [1, 2, 3]]  
# print(listVar2[3][1])                # listvar2[1, 2, 3, [1, 2, 3]] 에있는 
#                                      # 인덱스값 3 [listVar1] 이 나오는데 그중 인덱스값 1을
#                                      # 출력하면 listVar1[1, 2, 3] 중 인덱스 1은 2가 됨
# print(type(listVar2[3]))             # type 은 list
# print(type(listVar2[3][1]))          # type 은 int


dicts ={
    'name' : '박찬호',
    'age'  : 20,
    'addr' : '대전 중구',
    'hobby': ['축구', '농구', '배구']
}
print(f'dicts: {dicts}')
''' 출력하면 다음과 값이 같음 
dicts: {'name': '박찬호', 'age': 20, 'addr': '대전 중구', 'hobby': ['축구', '농구', '배구']}
'''

print(dicts['hobby'][1])       # ['축구', '농구', '배구'] 에 있는 인덱스 값 1을 출력  | 농구 출력































































































































































































































































