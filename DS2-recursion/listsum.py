

# def listsum(numList):
#     sum = 0
#     for i in numList:
#         sum = sum + i
    
#     return sum

'''
不能使用while或者for 
使用小学的内容：连加
(1+(3+(5+(7+9))))   第四个数  +  后面的所有数的和
    (1+(3+(5+16)))  第三个数  +  后面的所有数的和
        (1+(3+21))  第二个数  +  后面的所有数的和
            (1+24)  第一个数  +  后面的所有数的和
                25
'''
'''
递归三大定律
1，递归算法必须具有基本情况
    基本情况是算法停止递归的条件，通常是足够小，直接可以求解的问题
    举例：在整数列表的和中，基本情况是长度为1的列表
2，递归算法必须改变其状态并向基本情况靠近


3，递归算法必须以递归的方式调用


'''


# def listSum2(numList):#递归函数  调用自身
#     if len(numList) == 1:
#         return numList[0]

#     else:
#         return numList[0] + listSum2(numList[1:])

# print(listSum2([1,3,5,7,9]))

#练习1
#整数转换成为任意进制字符串

# def toSer(n,base):
#     str1 = '0123456789ABCDEF'

#     if n < base:
#         return str1[n]
#     else:
#         return toSer(n // base,base) + str1[n%base]

#  栈  实现递归 
from pythonds.basic.stack import Stack


rStack = Stack()

def toSer(n,base):
    converStrinig = '0123456789ABCDEF'

    while n > 0 :
        if n < base:
            rStack.push(converStrinig[n])
        else:
            rStack.push(converStrinig[n % base])

        n = n // base
    
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    
    return res

print(toSer(1453,16))

#5AD =   5*16^2 + 10*16^1 + 13*16^0








