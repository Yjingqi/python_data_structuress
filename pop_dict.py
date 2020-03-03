import timeit

x = range(2000000)
pop_zero = Timer("x.pop(0)","from __main__ import x")
print("pop_zero ",pop_zero.timeit(number=1000), "seconds")
x = range(2000000)
pop_end = Timer("x.pop()","from __main__ import x")
print("pop_end ",pop_end.timeit(number=1000), "seconds")

('pop_zero ', 1.9101738929748535, 'seconds')
('pop_end ', 0.00023603439331054688, 'seconds')