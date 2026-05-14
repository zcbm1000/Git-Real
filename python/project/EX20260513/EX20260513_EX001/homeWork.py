'''
1. 숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기 [3, 7, 1, 9, 5]      

2. 사용자에게 숫자 입력받아서 1 부터 입력한 숫자까지 합계 출력하기 ( 5 )

3. 리스트에 있는 숫자 중 짝수만 출력하기 [1,2,3,4,5,6]

4. 리스트 숫자를 오름차순 정렬하기 [5,1,7,3]

5. 리스트 숫자를 내림차순 정렬하기 [5,1,7,3]

6. 리스트 안 숫자의 평균 구하기 [10,20,30]

7. 리스트에서 가장 작은 숫자 찾기(min() 사용 금지) 리스트는[20, 15, 10, 30, 25]로 지정

8. 1부터 100까지 숫자 중 3의 배수와 5의 배수 출력하기

9. 사용자가 입력한 숫자를 리스트에 저장하다가 입력하면 종료 후 리스트 출력하기[입력: 3 ,입력: 7, 입력: 2 ,입력: 0]
'''



# # 1. 숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기 [3, 7, 1, 9, 5]     

# numbers = [3, 7, 1, 9, 5]
# largeNum = 0

# for num in numbers:
#     if num > largeNum:
#         largeNum = num

# print(f'리스트 중 가장 큰 수는:{largeNum}')


# # 2. 사용자에게 숫자 입력받아서 1 부터 입력한 숫자까지 합계 출력하기

# inputNum = int(input('숫자를 입력하세요'))                      
# total = 0                       
#                                   
# for num in range(1, inputNum+1):                                    
#     total += num                               
                    
# print(f'1부터 {inputNum}까의 합계 = {total}')                         
        

# # 3. 리스트에 있는 숫자 중 짝수만 출력하기 [1,2,3,4,5,6]

# numbers = [1, 2, 3, 4, 5, 6]

# for evens in numbers:
#     if evens % 2==0:

#         print(f'evens = {evens}')


# # 4. 리스트 숫자를 오름차순 정렬하기 [5,1,7,3]

# numbers = [5,1,7,3]
# numbers.sort(reverse=False)

# print(f'오름차순 정렬: {numbers}')


# # 5. 리스트 숫자를 내림차순 정렬하기 [5,1,7,3]

# numbers = [5,1,7,3]
# numbers.sort(reverse=True)

# print(f'내름차순 정렬: {numbers}')


# # 6. 리스트 안 숫자의 평균 구하기 [10,20,30]

# numbers = [10,20,30]
# average = sum(numbers) / len(numbers)

# print(f'numbers의 평균: {average}')


# # 7. 리스트에서 가장 작은 숫자 찾기(min() 사용 금지) 리스트는[20, 15, 10, 30, 25]로 지정

# numbers = [20, 15, 10, 30, 25]
# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num

# print(f'smallest = {smallest}')


# # 8. 1부터 100까지 숫자 중 3의 배수와 5의 배수 출력하기

# numbers = range(1, 101)

# multiples_3     = []
# multiples_5     = []
# commonMultiples = []

# for num in numbers:
#     if num % 3 == 0 and num % 5 == 0:
#         commonMultiples.append(num)
#         multiples_3.append(num)   
#         multiples_5.append(num)   

#     elif num % 3 == 0:
#         multiples_3.append(num)

#     elif num % 5 == 0:
#         multiples_5.append(num)

# print("3의 배수:", multiples_3)
# print("5의 배수:", multiples_5)
# print("3과 5의 공배수:", commonMultiples)

# 9. 사용자가 입력한 숫자를 리스트에 저장하다가 입력종료 후 리스트 출력하기(도어락가능할지도.)

# inputNum = []

# while True:
#     num = (input('숫자를 입력하세요 (종료: #):'))
#     if num == '#': 
#         break
#     inputNum.append(int(num))
#     print("입력한 숫자:", inputNum)