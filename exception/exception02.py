while True:
    try:
        n = input('숫자를 입력하시오 : ')
        n = int(n)
        break
    except ValueError as e:
        print('정수가 아닙니다.: ', e)

print('정수 입력 성공!')