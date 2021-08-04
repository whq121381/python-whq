# 编程实现下列图形的打印
# * 组成的三角形
# 这里设画布长度是21
def draw(n):
    def getLine(long=21):
        list = []
        for i in range(long):
            list.append(' ')
        return list

    for i in range(n+1):
        line = getLine()
        # 奇数
        if i%2:
            for x in range(i):
                # 奇数的偶数项为*
                if not x%2:
                    line[10+x] = '*'
                    line[10-x] = '*'
        # 偶数
        else:
             for x in range(i):
                 # 偶数的奇数项为*
                 if x%2:
                     line[10 + x] = '*'
                     line[10 - x] = '*'
                 pass
        # 直接打印有逗号,不好看print(line)
        for data in line:
            print(data,end='')
        print('')

# 使用while循环实现99乘法表的打印
def multiplication():
    for i in range(1,10):
        for x in range(1,i+1):
            print('%d*%d=%d'%(x,i,x*i),end=' ')
        print('')

# 编程实现99乘法表的倒叙打印
def reverseMultiplication():
    list = [x for x in range(1,10)]
    list.reverse()
    for i in list:
        for x in range(1, i + 1):
            print('%d*%d=%d' % (x, i, x * i), end=' ')
        print('')



if __name__ == '__main__':
    draw(7)
    multiplication()
    reverseMultiplication()