import time

#求前n个数的和

# def sumOFN(n):
#     start_time = time.time()
#     sun = 0
#     for i in range(1,n+1):
#         sum1 = sum + i
#     end_time = time.time()
#     return sum1,end_time-start_time


# print(sumOFN(10))

#高斯函数

def sumOFN2(n):
    return (n+(n+1))/2
start_time = time.time()
print(sumOFN2(10000))
end_time = time.time()
print(end_time-start_time)
