# Reverse a given number and return true if it is the same as the original number

def nth(num1):
    print("original number", num1)
    original_num = num1
    reverse_num = 0
    while num1 > 0:
        reminder = num1 % 10
        reverse_num = (reverse_num * 10) + reminder
        num1 = num1 // 10
    if original_num == reverse_num:
        return True
    else:
        return False


print("The original and reverse number is the same:", nth(131))
