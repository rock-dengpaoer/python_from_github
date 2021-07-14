filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 读取文本文件时，python将其中的所有文本都解读为字符串。读取的是数字，int（）转换为整数，或float（）转换为浮点数