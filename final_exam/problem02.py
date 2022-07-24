def over(scores):
    # 여기에 코드를 작성합니다.
    overScore_cnt = 0
    for score in scores:
        if score >= 60:
            overScore_cnt += 1
    return overScore_cnt 


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
