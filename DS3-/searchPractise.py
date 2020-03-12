'''

写一个函数，该函数需要一个列表和我们正在搜索的项作为参数，
并返回一个是否存在的布尔值，found = False

'''

# def sequetialSearch(alist,item):
#     found = False   
#     pos = 0

#     while pos < len(alist) and not found:
#         if alist[pos] == item:
#             found = True
#         else:
#             pos = pos + 1
#     return found

# testList = [1,2,3,7,23,42,90]
# print(sequetialSearch(testList,90))


# # 从头到尾最好的情况是什么，最差的情况是什么


'''

升序[17,20,26,30,44,54,55,65,77,93]
假设寻找的项在列表中
假设寻找的项不在列表中，50

'''

# def orderSequetiaSearch(alist,item):
#     pos = 0
#     found = False
#     stop = False


#     while pos < len(alist) and not found and not stop:
#         if alist[pos] == item:
#             found = True
#         else:
#             if alist[pos] > item
#                 stop = True
#             else:
#                 pos = pos + 1

#     return found

'''

有序列表
二分查找：每次都从剩余项中的中间元素进行比对

'''


# def binarySeach(alist,item):
#     found = False
#     first = 0
#     last = len(alist) - 1
#     while first <= last and not found:
#         #中间
#         midpoint = (first + last)//2
#         if alist[midpoint] ==item:
#             found = True
#         else:
#             if item < alist[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#     return found

# testList = [0,1,2,3,4,5,6,7,8,9]
# print(binarySeach(testList,6))

#递归实现二分查找

# def binarySeach(alist,item):

#     if len(alist) == 0:
#         return False
#     midoint = len(alist)//2
#     if alist[midoint] > item:
#         return True
#     else:
#         if alist[midoint] > item:
#             return binarySeach(alist[:midoint],item)
#         else:
#             return binarySeach(alist[:midoint + 1],item)



'''

Hash查找

'''












