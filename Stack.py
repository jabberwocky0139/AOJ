# coding: utf-8

input_line = [str(s) for s in input().split()]
input_line = input_line[::-1]
tmp_number = []
while(len(input_line) != 0):
    tmp = input_line[-1]
    if tmp == "+":
        tmp_number[-2] = tmp_number[-2] + tmp_number[-1]
        tmp_number.pop()
    elif tmp == "-":
        tmp_number[-2] = tmp_number[-2] - tmp_number[-1]
        tmp_number.pop()
    elif tmp == "*":
        tmp_number[-2] = tmp_number[-2] * tmp_number[-1]
        tmp_number.pop()
    else:
        tmp_number.append(int(tmp))
    input_line.pop()
print(tmp_number[0])
