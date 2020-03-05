'''
判断输入的字符是不是：回文字符

'''
from collections import deque
from pythonds.basic.deque import Deque

def palChecker(aString):

    chardeque = Deque()

    for ch in aString:chardeque
        chardeque.addRear(ch)
    flag = True


    while chardeque.size() > 1 and flag:

        first = chardeque.removeFront()
        last = chardeque.removeFront()

        if first != last:
            flag = False

    return flag


