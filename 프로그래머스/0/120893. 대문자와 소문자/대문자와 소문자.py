def solution(my_string):
    answer = ''
    for i in my_string:
        if 'a' <= i <= 'z':
            answer += chr(ord(i) - 32)
        elif 'A' <= i <= 'Z':
            answer += chr(ord(i) + 32)
        else:
            answer += i
    return answer
