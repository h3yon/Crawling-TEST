# 변수, 자료형, 조건문, 반복문, 기타 라이브러리

a = 2
b = 3
print(a + b) # 5

# 문자열 더하기

first_name = 'bumkyu'
last_name = 'lee'

print(first_name + last_name) #bumkyulee

# 숫자 + 문자열

print(a + first_name) # error
print(str(a) + first_name) # 2bumkyu

# list
a_list = ['사과', '감', '배']
b_list = ['영희', '철수']

print(b_list[0])

# 딕셔너리

a_dict = {'name':'bob', 'age':24}
print(a_dict['name']) #bob

a_dict['height'] = 178
print(a_dict)

a_dict['fruits'] = a_list
print(a_dict['fruits'][0])


age = 24
if age > 20:
    print('성인입니다')
    print('성인입니다2')
else:
    print('청소년입니다')

# 리스트 예제

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count = 0

for fruit in fruits:
    if fruit == '사과':
        count += 1

print(count) #2

# 딕셔너리 예제

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    print(person['age'])# 20, 38, 7, 17, 27

# 문자열 쪼개기, 바꾸기

myemail = 'spart@naver.com'
# result = myemail.split('@')[1].split('.')[0]

result = myemail.replace('naver', 'gmail')

print(result)