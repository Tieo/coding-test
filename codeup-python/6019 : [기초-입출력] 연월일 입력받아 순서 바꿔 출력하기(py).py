#"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
yyyy, mm, dd = map(int, (input().split('.')))
print(dd, mm, yyyy, sep='-')
