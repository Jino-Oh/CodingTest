def solution(numbers):
    first, second = sorted(numbers, reverse = True)[:2]
    answer = first * second
    return answer