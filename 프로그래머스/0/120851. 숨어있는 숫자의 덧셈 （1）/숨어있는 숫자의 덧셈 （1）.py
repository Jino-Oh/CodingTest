def solution(my_string):
    answer = 0
    my_string = list(my_string)
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer