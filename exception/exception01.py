# 예외처리 #1
(x, y) = (2, 0)
try:
    z = x/y
except ZeroDivisionError as e:
    print(e)
