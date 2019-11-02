# 3.11.1 
# Collatz序列
def collatz(number):
    if number % 2 == 0:
        j = number // 2
        print(j) 
    else:
        j = 3 * number + 1
        print(j)
    return j
        
def test_collatz():
    print("Enter number: ")
    num = input()
    result = collatz(int(num))
    while(result != 1):
        result = collatz(result)

# 3.11.2
# 输入验证
def input_validation():
    print("Enter number: ")
    try:
        num = input()
        result = collatz(int(num))
        while(result != 1):
            result = collatz(result)
    except ValueError:
        print("You must input an integer!")


if __name__ == '__main__':
    input_validation()