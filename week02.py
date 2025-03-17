import random

rnd = random.randint(1, 100)
win = False

for i in range(7):
    print(f"{7 - i}번의 기회가 남았습니다. 숫자 입력(1 ~ 100) : ", end = '')
    answer = int(input())
    if answer == rnd:
        print("정답입니다!")
        win = True
        break
    elif answer > rnd:
        print("입력하신 수는 정답보다 큰 수 입니다.")
    else:
        print("입력하신 수는 정답보다 작은 수 입니다.")

if win:
    print("당신이 이겼습니다!")
else:
    print(f"당신이 졌습니다. 정답은 {rnd} 입니다.")