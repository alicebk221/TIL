import random

answer = random.randint(1, 20)
for i in range(1, 5):
    chance = 5-i
    user = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰 보세요: ".format(chance)))
    print(answer, user)
    if chance > 1:
        if user > answer :
            print("Down")
        elif user < answer:
            print('Up')
        elif user == answer:
            print("축하합니다. {}번 만에 숫자를 맞추셨습니다.".format(i))
            break
    else:
        print("아쉽습니다. 정답은 {}입니다.".format(answer))

# 나중에 for문-break 대신 while문 사용해서 수정해보기