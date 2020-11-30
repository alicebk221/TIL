# 파이썬 프로그래밍 기초 DAY1

# 숫자형 연산 예시
# floor division (나눗셈의 몫만 출력)
print(7 // 2) # 결과 : 3

# round (반올림)
print(round(3.141592)) # 결과 : 3
print(round(3.141592, 3)) # 결과 : 3.142

# n승
print(2 ** 3) # 2의 3승, 결과 : 8

# 문자열 포맷팅
year = 2020
month = 6
day = 1
print('오늘은 {}년 {}월 {}일'.format(year, month, day))
date_str = '오늘은 {}년 {}월 {}일'
print(date_str.format(year, month, day+1))

# format 응용 1
print('나는 {}, {}, {}를 좋아한다.'.format('BTS', 'DAY6', 'SHINee'))
print('나는 {2}, {0}, {1}를 좋아한다.'.format('BTS', 'DAY6', 'SHINee'))

# format 응용 2
num_1 = 1
num_2 = 3
print('{0} 나누기 {1}은 {2}이다.'.format(num_1, num_2, num_1 / num_2))
print('{0} 나누기 {1}은 {2:.2f}이다.'.format(num_1, num_2, num_1 / num_2))
