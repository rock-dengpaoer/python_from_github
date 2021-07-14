with open('pi_digits.txt') as file_object:
    # contents = file_object.read()
    for line in file_object:
        print(line.rstrip())

# print(contents.rstrip())
