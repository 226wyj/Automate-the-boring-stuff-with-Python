# 4.10.1 逗号代码
def listProcess(listdata):
    result = ""
    count = 0
    for i in listdata:
        result += str(i)
        count += 1
        if count < len(listdata)-1:
            result += ','
        elif count == len(listdata)-1:
            result += ' and '
        else:
            None
    return result

def test_4_10_1():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(listProcess(spam))

# 4.10.2 字符图网格
def charGrid():
    grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]
    i, j = 8, 0
    while j <= 5:
        while i >= 0:
            print(grid[i][j], end='')
            i -= 1
        print('\n')
        i = 8
        j += 1

def test_4_10_2():
    charGrid()

# 运行
if __name__ == '__main__':
    test_4_10_1()
    test_4_10_2()



    