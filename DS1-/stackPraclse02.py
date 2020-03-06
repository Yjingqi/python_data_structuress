'''
使用“除2”算法，将输入的十进制数字转换成8位2进制数字


'''

# from pythonds.basic.stack import Stack

# def divide2(desNumber):
#     s = Stack()
#     while desNumber > 0:
#         rem = desNumber % 2 
#         s.push(rem)
#         desNumber = desNumber//2


from pythonds.basic.stack import Stack

def devide2(desNumber):

    s = Stack()

    while desNumber > 0:
        rem = desNumber % base 
        s.push(rem)
        desNumber = desNumber //base

    binString = ""
    while not s.isEmpty():
        binString = binString + str(s.pop())
    return binString

print(divmod)









