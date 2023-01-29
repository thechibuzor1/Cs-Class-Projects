# taking user input
# as plain numbers

first_num = abs(
    int(input("Enter the first number (minus(-) is not needed): ")))
second_num = abs(
    int(input("Enter the second number (minus(-) is not needed): ")))


def convertToBinary(num: int):
    res = ""
    while num > 0:
        remainder = num % 2
        res = res + str(remainder)
        num = num // 2

    res = res[::-1]

    if len(res) < 4:
        left = 4 - len(res)
        res = (str(0)*left) + res

    return (res)


def convertToNegative(num: str):
    res = ''
    for i in range(0, len(num)):
        if num[i] == "0":
            res += '1'
        else:
            res += '0'

    # adding one after inverting
    sum = bin(int(res, 2) + int('1', 2))
    return (sum[2:])


def addtion(num1, num2):

    a = num1
    b = num2
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

# Initialize the result
    result = ''

# Initialize the carry
    carry = 0

# Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

    # Compute the carry.
        carry = 0 if r < 2 else 1

    return (result.zfill(max_len))


print(addtion(convertToNegative(convertToBinary(first_num)),
      convertToNegative(convertToBinary(second_num))))
