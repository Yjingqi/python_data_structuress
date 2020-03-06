

def listsum(numList):
    sum = 0
    for i in numList:
        sum = sum + i
    
    return sum

'''
不能使用while或者for 
使用小学的内容：连加
(1+(3+(5+(7+9))))   第四个数  +  后面的所有数的和
    (1+(3+(5+16)))  第三个数  +  后面的所有数的和
        (1+(3+21))  第二个数  +  后面的所有数的和
            (1+24)  第一个数  +  后面的所有数的和
                25
'''


def listSum2(numList):#递归函数  调用自身
    if len(numList) == 1:
        return numList[0]

    else:
        return numList[0] + listSum2(numList[1:])

print(listSum2([1,3,5,7,9]))