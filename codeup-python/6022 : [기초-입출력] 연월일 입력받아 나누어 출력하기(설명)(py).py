# 6자리의 연월일(YYMMDD)을 입력받아 'YY MM DD' 형식으로 출력

date = input()
print(date[0:2], date[2:4], date[4:6], sep=' ')
