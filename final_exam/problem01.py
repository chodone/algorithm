def max_score(scores):
    # 여기에 코드를 작성합니다.
    maxScore = 0

    for score in scores:
        if maxScore < score:
            maxScore = score
    return maxScore

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
