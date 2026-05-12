# 컨테이너 자료형 > 자료형
# container data type
# 컨테이너 자료형은 많은 데이터를 효율적으로 관리하기 위해 사용을함

# 대표적인 예로 list(리스트), tuple(튜플), dictionary(딕셔너리)
'''
ex) fruit 1 '사과'   (과일)
    fruit 2 '포도'   (과일)
    fruit 3 '복숭아' (과일)
    tool 1 '연필'    (도구)
    tool 2 '칼'      (도구)
'''
# 위와같이 사과,포도,복숭아는 과일이라는 카테고리로 
# 연필과 칼은 도구라는 카테고리로 다음과 같이 묶을수있음
'''
fruit['사과', '포도', '복숭아']
tool ['연필', '칼']
'''
# ex) 쇼핑목록, mp3 음원리스트, 학급 학생이름 을 예시로 들수가 있음

# list --------------------------------------
# ex) country (한국, 미국, 일본, 중국)
#     country 라는 리스트의 길이는 4이다 (길이란 내부에있는 데이터의 수를 뜻함)
# 리스트를 선언할때에는 대괄호( [] )를 사용하며 쉼표( , )를 구분자로 사용함




'''
기초 데이터 타입
num = 10 
num 이라는 변수 안에 10이라는 메모리가 직접담김

참조 데이터 타입
fruits[사과, 포도, 메론]

fruits 이라는 변수안에 사과, 포도, 메론이 직접담기는게아닌
사과, 포도, 메론이 담긴주소를 가르침
ex) 기초 데이터 타입 = 등산시 정상에 있는 바위
    참조 데이터 타입 = '정상까지 ?m 남음'을 나타내는 이정표 

fruit = [사과, 포도, 메론]    
fruit = [과자, 음료, 사탕]
지정하면 사과, 포도, 메론 데이터가 사라지는것이 
아닌 주소만 과자,음료, 사탕 주소로 바뀜  
↕↕↕↕↕↕↕↕↕↕그러나↕↕↕↕↕↕↕↕↕↕
fruit = [사과, 포도, 메론] 을 지정했는데
fruit = '수박' 을 덮어씌우면
fruit = '수박' 이 되고 [사과, 포도, 메론]은 삭제됨
''' 

# fruits = ['사과','수박', '포도', '참외', '자두']   # 길이가 5인 리스트
# print(f'fruits= {fruits}')

# 리스트와 데이터
'''
리스트에 포함되는 데이터는 어떤 자료형이든 상관이 없음
정수, 실수, 문자열이 하나의 리스트로 묶일 수도 있음
'''

# any = [1, '한글', 3.14 ]
# print(any)
# 위와 같이 하나의 리스트에 다양한 데이터 타입을 넣을 수 있는 것은
# 파이썬과 자바스크립트뿐임. 자바는 안됨

# any = [1, '한글', 3.14 ]
# print(f'any = {any}')
# print(f'type of any: {type(any)}')


# ex) 다음 회의 참석자 명단을 리스트로 선언하고, attendList 변수에 담을것
# attendList = ['이순철', '김병헌', '김민우', '박찬호', '김민태']


# how to 리스트 아이템 조회
# 특정 아이템 조회
# 인덱스      0   ,  1   ,   2   ,    3  ,   4
# fruits = ['사과','수박', '포도', '참외', '자두']
# print(fruits[1],fruits[2])
# 리스트에 존재하지 않는 인덱스를 참조하면 인덱스에러가 출력

# numbers = [1, 2, 3, 4, 5, 6 , 7, 8, 9]
# print(f'numbers: {numbers}')
# print(f'numbers length: {len(numbers)}')     # len() 아이템의 갯수를 알려줌
                                               # length 의 약자
           
# # 첫번째 데이터 조회
# numbers = [1, 2, 3, 4, 5, 6 , 7, 8, 9]
# print(f'numbers: {numbers[0]}')

# # 마지막 데이터 조회
# numbers = [0, 1, 2, 3, 4, 5, 6 , 7, 8, 9]
# print(f'numbers: {numbers[9]}')              # 인덱스에서 마지막 데이터는 길이 -1임

# str = 'heiksahgh2s91bxb109sud1sdsbhxz902h'         # 몇 자 인지 모름
# print(len(str))                                    # len 을 사용하여 34자임을 확인


# Quiz) 입력한 글자 수 확인 및 출력
'''
사용자가 입력한 메시지를 받아 입력받은 문자열의 길이를 출력
'''
# msg = input('문자 메시지를 입력하세요.')          # 스페이스바 공백도 1개의 문자열로 취급
# print(f'입력하신 메시지의 길이는 {len(msg)} 자 입니다.')

# 리스트 전체 데이터 조회
balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
'''
# print(f'{balls[0]}')
# print(f'{balls[1]}')
# print(f'{balls[2]}')
# print(f'{balls[3]}')
# print(f'{balls[4]}')
가능은하나 리스트가 많아질수록 쓰기가 힘들어짐
'''
# for 문 을 이용함
# balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
# for idx, item in enumerate(balls):                         # for 변수 in 을 이용하여 출력 
                                                             # enumerate 함수는 인덱스값을 뽑음
#     print(f'item: {item}, index: {idx}')
      
# # while 문 을 이용함
# balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
# i=0
# while i< len(balls):
#     print(f'item: {balls[i]}, index: {i}')
#     i += 1

# Quiz) 다음 리스트에서 마지막 인덱스 값을 출력하는 프로그램
# sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer']
# leng = len(sports) -1                                                # leng 은 ()sports 의 아이템 갯수) -1
# print(f'index: {leng}')                                              # 출력:   4    (인덱스 값을 출력함) 
# print(sports[leng])                                                  # 출력: soccer (마지막 인덱스에 해당한 데이터를뺌)


# Quiz) 다음 리스트에서 'python' 문자열의 인덱스 값을 출력하는 프로그램
# language = ['c', 'c#', 'python', 'java']
# for idx,str in enumerate(language):
#     if str == 'python':
#         print(f'python idx: {idx}')

# language = ['c', 'c#', 'python', 'java']
# targetIdx = language.index('python')         # targetIdx 는 index 함수(파이썬검색) 하여 바로할당
# print(f'targetIdx: {targetIdx}')             # 출력: targetIdx: targetIdx


# 아이템 기존 리스트에 삽입
# 리스트 마지막에 삽입
# sports = ['football', 'baseball', 'vollyball']    # 기존 리스트
# print(f'sports:{sports}')                         # 출력: sports:['football', 'baseball', 'vollyball']
# print(f'sports length: {len(sports)}')            # 출력: sports length: 3
# sports.append('basketball')                       # 리스트 마지막에'baskerball'을 삽입
# print(f'sports: {sports}')                        # 출력: sports: ['football', 'baseball', 'vollyball', 'basketball']
# print(f'sports length: {len(sports)}')            # 출력: sports length: 4



#Quiz) 취미 추가하기
'''
취미를 저장할 리스트 정의후 사용자가 입력한 취미가 추가되는 프로그램
'''
# hobbies = []                                  # 리스트 정의
# Hobby = input('취미를 입력하세요')            # 추가할 문구 입력
# hobbies.append(Hobby)                         #hobbie 에 Hobby 를 추가함
# print(f'hobbies: {hobbies}')                  #출력: hobbie: 입력문구

# hobbies = []
# flag = True
# while flag:
#     hobby = input('취미를 입력하세요')
#     hobbies.append(hobby)
#     print(f'hobbies{hobbies}')
#     select = int(input('1.취미추가 2.종료'))
#     if select == 2:
#         flag = False
#     print(f'총 개수: {len(hobbies)}')


# 특정 위치에 아이템 삽입
# 리스트의 원하는 위치에 아이템을 삽입할때는 inser() 함수를 이용

# countries = ['korea','japan','china']             # 리시트 정의
# countries.insert(1, 'usa')                        # inser(인덱스위치, '넣을항목')
# print(f'countries: {countries}')                  # 출력: insert 한 항목 포함


# Quiz) 1부터 10까지 숫자중 누락된 숫자 추가하기   
# numbers = [1,2,3,4,5,7,8,9]          # 6, 10 누락
# numbers.insert(5, 6)                 # 5번 인덱스에 6을 추가
# print(f'numbers: {numbers}')         # 출력
# numbers.append(10)                   # 마지막에 10을 추가
# print(f'numbers: {numbers}')         # 출력


# 리스트 연결하기
# 리스트에 또 다른 리스트를 연결할 때는 extend() 함수를 사용합니다.

# list1 = [1,2,3]
# print(f'list1: {list1}')         

# list2 = [10,20,30]
# print(f'list2: {list2}')

# list1.extend(list2)                    # 리스트1에 리스트 2를 붙임
# print(f'list1: {list1}')                # 리스트2는 저장이 그대로 유지됨


# list3 = list1 + list2 
# print(f'list1: {list1}')  
# print(f'list2: {list2}')  
# print(f'list3: {list3}')  


# 리스트 아이템 삭제하기
# 리스트 마지막 아이템 삭제하기

# sports = ['football', 'baseball', 'vollyball', 'basketball']
# print(f'sports: {sports}')
# sports.pop()                          #pop() 맨뒤를 삭제함 괄호안에 숫자를 기입시 해당 인덱스번호를 삭제함
# print(f'sports: {sports}')


# sports = ['football', 'baseball', 'vollyball', 'basketball']
# print(f'sports: {sports}')
# del sports[2]                         # del 을이용하여 2번자리의 인덱스를 삭제함
# print(f'sports: {sports}')


# Quiz) sports 리스트에서 'volleyball'을 삭제하는 프로그램
# sports = ['football', 'baseball', 'vollyball', 'basketball']
# vollyBallsIdx  = sports.index('vollyball')
# sports.pop(vollyBallsIdx)
# print(f'sports: {sports}')


































































































































