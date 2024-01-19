# 정수 3개 받아 합과 평균 출력
a, b, c = map(int, input().split())
sumABC = a + b + c
avgABC = sumABC / 3
print(sumABC, format(avgABC, ".2f"))
