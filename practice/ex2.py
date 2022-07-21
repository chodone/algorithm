total_bull = int(input("게시글의총 갯수를 입력하세요: "))
max_bull = int(input("한 페이지에 필요한 게시글 수를 입력하세요: "))

if total_bull % max_bull > 0:
    page = (total_bull // max_bull) + 1
else:
    page = total_bull // max_bull

print(page)
