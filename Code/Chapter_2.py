# 2.11.9 
# 编写代码，如果变量spam中存放1，就打印Hello, 如果存放2，就打印Howdy，如果存放其他值就打印Greetings!
def Fun1(spam):
    if spam == 1:
        print("1")
    elif spam == 2:
        print("Howdy")
    else:
        print("Greetings!")

# 2.11.13 
# 编写一小段程序，利用for循环，打印出从1到10的数字。然后利用while循环，编写一个等价的程序，打印出从1到10的数字
def Fun2():
    for i in range(1, 11, 1):
        print(i)
    j = 1
    while j <= 10:
        print(j)
