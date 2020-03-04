#栈抽象数据类型的底层实现采用什么？     list
#确定列表的哪一端是顶部，然后使用aooend和pop来实现操作

#假设列表的尾部是栈的顶部元素，Push


# class Stack:
#     def __init__(self):
#         self.item = []
    

#     def isEmpty(self):
#         return self.items == []


#     def push(self,item):
#         self.items.append(item)
    
#     def pop(self):
#         return self.items.pop()

#     def peek(self):
#         return self.items[len(self.items)-1]

#     def size(self):
#         return len(self.items)
    

# from pythonds.basic.stack import Stack


# s = Stack()

# print(s.isEmpty())


# s.push(4)
# s.push('lalla')

# print(s.peek())

# s.push(True)

# print(s.size())
# print(s.isEmpty())

# s.push(10.9)

# print(s.pop())
# print(s.pop())
# print(s.size())

# sum = (1+2)*(3+4)/(5+6)
# print(sum)

# from pythonds.basic.stack import Stack

# # symbolString  假设  “（（））”
# def parChenker(symbolString):
#     s = Stack()
#     flag = True
#     index = 0

#     while index < len(symbolString) and flag:
#         symbol = symbolString[index]
#         if symbol == "(":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 flag = False
#             else:
#                 s.pop()

#         index = index + 1
#     if flag and s.isEmpty():
#         return True
#     else:
#         return False


# print(parChenker('(())'))#
# print(parChenker('((())'))

#  {[()]}     ([)]



from pythonds.basic.stack import Stack


def parChenker(SyntaxWarning):
    s = Stack()
    flag = True
    index = 0
    while index < len(symbolString) and flag:
        symbol = symbol[index]

        if symbol in "([{":
            s.push(symbol)
        else:
            if symbol in "([{":
                flag = False
            else:
                top = s.pop()
                start = "([{"
                end = ")]}"
               
                if not start.index(top) == end.index(symbol):
                    flag = False

        index = index + 1
    
    
    if flag and s.isEmpty():
        return True
    else:
        return False

print(parChenker"{[()]}")
print(parChenker("{{([][])}()}"))
print(parChenker('[{()]'))














