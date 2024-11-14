def solution(num1, num2):
    if((num1 < 0 & num1 > 100) | (num2 < 0 & num2>100)):
        print("잘못된 값을 입력")
        return 0
    else:
        answer = num1 * num2
    return answer