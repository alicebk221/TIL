def myself(name, age, nationality = '한국') :
    print(f'내 이름은 {name}.')
    print('나이는 {}.'.format(age))
    print('국적은 {}.'.format(nationality))


myself('정보경', 27)
print()
myself('정보경', 27, '대한민국')