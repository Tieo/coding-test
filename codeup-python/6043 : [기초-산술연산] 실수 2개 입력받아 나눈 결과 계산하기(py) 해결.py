# 실수 2개 입력받아 f1을 f2로 나눈 값을 출력, 소숫점 넷쨰자리에서 반올림하여 소숫점 셋쨰 자리까지 출력
f1, f2 = map(float, input().split())
# print(round(f1/f2, 3))
print(format(f1 / f2, ".3f"))
