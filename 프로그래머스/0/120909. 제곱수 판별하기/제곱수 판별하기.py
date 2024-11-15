def solution(n):
    answer = 0
    sqrt_n = int(n ** 0.5)
    if(sqrt_n * sqrt_n == n):
        answer = 1
    else:
        answer = 2
    return answer