'''
乱序字符串是指一个字符串只是另一字符串的重新排列
前提：字符串是由26个小写字母集合组成，长度相同
比如：python    typhon    head    deah
目的：
    写一个布尔函数（返回值是布尔值的函数）
    solutionsl('abcd','dbca)

'''
#1，穷举法：排除   原因：如果字符串过长，所写的for循环要写很多
 
#2，检查 第一个字符串是不是出现在第二个字符串中  o(n^2)

# def soultions(s1,s2):
#     alist = list(s2)

#     pos1 = 0
#     flag = True

#     while flag and pos1 < len(s1):
#         pos2 = 0
#         found = False
#         while pos2 < len(s2) and not found:
#             if s1[pos1] == alist[pos2]:
#                 pass
#             else:
#                 pos2 = pos2 + 1


#         if found:
#             alist[pos2] = None

#             pos1 = pos1 + 1
#         else:
#             flag = False

#     return flag

# print(soultions('abcd','dbca'))

#3,计数和比较法         aaaabbbbcccc     ccccaaaabbbb
#计算每个字符出现的次数，

# def solutions2(s1,s2):
#     c1 = [0] * 26 #记录s1中字母出现的次数 [4,4,4,0,0,0,0,0,0,0,0,0,,,,]
#     c2 = [0] * 26 #记录s2中字母出现的次数 [4,4,4,0,0,0,0,0,0,0,0,0,,,,]

#     #ord()    返回的是字符在阿斯克码中的数字

#     for i in range(len(s1)):
#         pos = ord(s1(i)) - ord('a')
#         c1[pos] = c1[pos] + 1

#     for i in range(len(s2)):
#         pos = ord(s1(i)) - ord('a')
#         c2[pos] = c2[pos] + 1

#     count = 0  #字符出现的次数,如果某个字符出现在s1和s2中出现的次数相同那么，content就+1

#     flag = True
#     while count < 26 and flag:
#         if c1[count] == c2[count]:
#             count = count + 1
#         else:
#             flag = False


#     return flag


# print(solutions2('aaaabbbbcccc','ccccbbbbaaaa'))
        
# 4，通过排序和比较   :即使s1,s2不同  他们都是由完全相同的字符组成的。
#我们可以从a-z  排列每一个字符串，如果两个字符串相同，那么这两个字符串就是乱序字符串
#aaaabbbbcccc     bbbbaaaacccc
#算法复杂度：不是o(n) 是o(n^2)

 
def solutions3(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    #排序   o(n^2)
    alist1.sort()
    alist2.sort()
    
    pos = 0

    flag = True
    while pos < len(s1) and flag:

        if alist1[pos] == alist2[pos]:
            pos = pos + 1 
        else:
            flag = False


    return flag


print(solutions3('aaaabbbbcccc','bbbbccccaaaa'))
print(solutions3('python','ythpna'))


